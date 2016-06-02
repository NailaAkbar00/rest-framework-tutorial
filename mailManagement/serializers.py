from rest_framework import serializers
from mailManagement.models import actor

class ActorSerializer(serializers.HyperlinkedModelSerializer):
   
    class Meta:
        model = actor
        fields = ('actor_id','first_name','last_name','last_update')