from rest_framework import serializers
from snippets.models import Snippet, LANGUAGE_CHOICES, STYLE_CHOICES
from django.contrib.auth.models import User
from django.db import models


class SnippetSerializer(serializers.ModelSerializer):
    #owner = models.ForeignKey('auth.User', related_name='snippets')
    owner = serializers.ReadOnlyField(source='owner.username')
    highlight = serializers.HyperlinkedIdentityField(view_name='snippet-highlight', format='html')
     
    class Meta:
        model = Snippet
        #fields = ('owner','id', 'title', 'code', 'linenos', 'language', 'style')
        fields = ('url', 'highlight', 'owner',
                  'title', 'code', 'linenos', 'language', 'style')

class UserSerializer(serializers.ModelSerializer):
#   snippets = models.ForeignKey('auth.User', related_name='snippets')
#  snippets = serializers.PrimaryKeyRelatedField(many=True, queryset=Snippet.objects.all())
    
    snippets = serializers.HyperlinkedRelatedField(many=True, view_name='snippet-detail', read_only=True)
     
    class Meta:
        model = User
        #fields = ('id', 'username', 'snippets')
        fields = ('url', 'username', 'snippets')
#     def create(self, validated_data):
#         """
#         Create and return a new `Snippet` instance, given the validated data.
#         """
#         return Snippet.objects.create(**validated_data)
# 
#     def update(self, instance, validated_data):
#         """
#         Update and return an existing `Snippet` instance, given the validated data.
#         """
#         instance.title = validated_data.get('title', instance.title)
#         instance.code = validated_data.get('code', instance.code)
#         instance.linenos = validated_data.get('linenos', instance.linenos)
#         instance.language = validated_data.get('language', instance.language)
#         instance.style = validated_data.get('style', instance.style)
#         instance.save()
#         return instance