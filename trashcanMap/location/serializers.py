from location.models import Trashcan, Likes, TrashcanDetection
from rest_framework import serializers
from accounts.serializers import UserSerializer

class PinSerializer(serializers.HyperlinkedModelSerializer):
    likes = serializers.SerializerMethodField(read_only=True)
    dislikes = serializers.SerializerMethodField(read_only=True)

    def get_likes(self, obj):
        return obj.likes.count()

    def get_dislikes(self, obj):
        return obj.dislikes.count()
    class Meta:
        model = Trashcan
        fields = ('id', 'latitude', 'longitude', 'likes', 'dislikes')

class TrashcanSerializer(serializers.HyperlinkedModelSerializer):
    author = UserSerializer(read_only=True)
    likes = serializers.SerializerMethodField(read_only=True)
    dislikes = serializers.SerializerMethodField(read_only=True)
    userLikes = serializers.SerializerMethodField(read_only=True)
    userDisLikes = serializers.SerializerMethodField(read_only=True)

    def get_likes(self, obj):
        return obj.likes.count()

    def get_dislikes(self, obj):
        return obj.dislikes.count()

    def get_userLikes(self, obj):
        if obj.likes.filter(id=self.context.get("user_id")):
            return True
        return False
    
    def get_userDisLikes(self, obj):
        if obj.dislikes.filter(id=self.context.get("user_id")):
            return True
        return False
    class Meta:
        model = Trashcan
        fields = ('id','latitude', 'longitude', 'address', 'image', 'description', 'author', 'likes', 'dislikes', 'userLikes', 'userDisLikes')

class TrashcanActionSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    action = serializers.CharField()

    def validate_action(self, value):
        value = value.lower().strip()
        if not value in ['like', 'dislike']:   # actions in list
            raise serializers.ValidationError("not a valid action")
        return value

class TrashcanCheckSerializer(serializers.Serializer):
    class Meta:
        model = TrashcanDetection
        fields = ('image')