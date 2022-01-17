from django.shortcuts import get_object_or_404, render
from rest_framework import viewsets
from location.serializers import TrashcanSerializer, PinSerializer, TrashcanActionSerializer, TrashcanCheckSerializer
from accounts.serializers import UserSerializer, UserDetailSerializer
from location.models import Trashcan, Likes
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import permissions
from location.permissions import *
from rest_framework.authtoken.models import Token
from accounts.models import CustomUser
from rest_framework.views import APIView
from django.contrib.auth import authenticate
from rest_framework.decorators import action, permission_classes
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated, AllowAny
import jwt
from location.models import TrashcanDetection
from django.conf import settings

class PinView(viewsets.ModelViewSet):
    queryset = Trashcan.objects.all()
    serializer_class = PinSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    #http_method_names = ['get', 'post']

class TrashcanViewSet(viewsets.ModelViewSet):
    queryset = Trashcan.objects.all()
    serializer_class = TrashcanSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    #http_method_names = ['get', 'post']
    
    # detail에서 user_id를 받아와야됨
    # obj = Trashcan.objects.filter(id=pk).first()

    # 해서 serializer = TrashcanSerializer(obj, context={'user_id':request.data.get('user_id')}) 반환

    def perform_create(self, serializer):
        print(self.request.user)
        serializer.save(author=self.request.user)

    def retrieve(self, request, pk=None):
        queryset = Trashcan.objects.all()
        obj = get_object_or_404(queryset, pk=pk)

        serializer = TrashcanSerializer(obj, context={'user_id':request.GET.get('user_id')})
        return Response(serializer.data, status=200)
    
class TrashcanActionViewSet(viewsets.ModelViewSet):
    serializer_class = TrashcanSerializer
    permission_classes = [AllowAny]

    def action(self, request):
        serializer = TrashcanActionSerializer(data=request.POST)
        if serializer.is_valid(raise_exception=True):
            data = serializer.validated_data
            trashcan_id = request.POST.get('id')
            action = request.POST.get('action')
            queryset = Trashcan.objects.filter(id=trashcan_id)

            if not queryset.exists():
                return Response({"message": "Queryset Does not Exist"}, status=404)
            obj = queryset.first()

            # like했을때 이미 like이 되어있으면 like없앰
            # dislike했을때 like가 되어있으면 like없애고 dislike추가
            if action == 'like':
                if obj.likes.filter(id=request.data.get('user_id')):
                    print("remove")
                    obj.likes.remove(request.POST.get('user_id'))
                else:
                    if obj.dislikes.filter(id=request.data.get('user_id')):
                        obj.dislikes.remove(request.POST.get('user_id'))
                    obj.likes.add(request.POST.get('user_id'))

            elif action == 'dislike':
                if obj.dislikes.filter(id=request.data.get('user_id')):
                    obj.dislikes.remove(request.POST.get('user_id'))
                else:
                    if obj.likes.filter(id=request.data.get('user_id')):
                        obj.likes.remove(request.POST.get('user_id'))
                    obj.dislikes.add(request.POST.get('user_id'))

            serializer = TrashcanSerializer(obj, context={'user_id':request.data.get('user_id')})
            return Response(serializer.data, status=200)


class UserViewSet(viewsets.ModelViewSet):
    permission_classes = [AllowAny]
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer

class TrashcanCheckViewSet(viewsets.ModelViewSet):
    serializer_class = TrashcanCheckSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def is_trashcan(self, request):
        serializer = TrashcanCheckSerializer(data=request.data)
        if serializer.is_valid():
            image = TrashcanDetection.objects.create(image=request.data['image'])

            # settings.py 에 정의되어있는 DETECTION_MODEL에서 object detection에 필요한 model을 불러옴
            model = getattr(settings, 'DETECTION_MODEL')
            results = model(['./media/' + str(image.image)])
            print(results.pandas().xyxy)

            resList = [[] for _ in range(len(results.pandas().xyxy[0]['name']))]
            for i in range(len(results.pandas().xyxy[0]['name'])):
                resList[i].append(results.pandas().xyxy[0]['name'][i])
                resList[i].append(results.pandas().xyxy[0]['confidence'][i])
            for item in resList:
                if item[0] == 'trash_can' and item[1] >= 0.60:
                    return Response(True, status=200)

        return Response(False, status=200)

class SignupView(APIView):
    def post(self, request):
        if(4< len(request.data['username']) <= 12 and len(request.data['password']) >= 8):
            user = User.objects.create_user(username=request.data['username'], password=request.data['password'])

            user.save()

            token = Token.objects.create(user=user)
            return Response({"Token": token.key})
        else:
            return Response({"error": "id or password invalied"})
        

class SigninView(APIView):
    def post(self, request):
        user = authenticate(username=request.data['username'], password=request.data['password'])
        if user is not None:
            token = Token.objects.get(user=user)
            return Response({"Token": token.key})
        else:
            return Response({'error': 1})