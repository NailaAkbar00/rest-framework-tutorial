from django.shortcuts import render
from rest_framework import viewsets
from mailManagement.serializers import ActorSerializer
from mailManagement.models import actor
import pymysql, json
from contextlib import closing
from rest_framework.response import Response
from rest_framework.decorators import detail_route
# Create your views here.
class ActorViewSet(viewsets.ModelViewSet):
    
    serializer_class = ActorSerializer
    queryset = actor.objects.all()
    
    @detail_route(methods=['get'])
    def actorByName(self, request, pk=None):
        res = actor.objects.filter(first_name=pk)
        serializer = ActorSerializer(res, many=True)
        return Response(serializer.data)
#     def list(self, request):
#         # Note the use of `get_queryset()` instead of `self.queryset`
#         #queryset = self.get_queryset()
#         conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='apl/1234', db='sakila')
#         cur = conn.cursor(pymysql.cursors.DictCursor)
#         cur.execute("SELECT  actor_id, first_name, last_name, last_update FROM actor")
#         #queryset = json.dumps(list(cur))
#         serializer = ActorSerializer(cur, many=True)
#         return Response(serializer.data)
         
     #   return Response(json.dumps(list(cur)))
#    
#     def get(self):
#         conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='apl/1234', db='sakila')
#         cur = conn.cursor()
#         cur.execute("SELECT  actor_id, first_name, last_name FROM actor where actor_id = (%d)" % 1)
#          
#         return Response(json.dumps(list(cur)))
#         queryset = self.get_queryset()
#         serializer = ActorSerializer(queryset, many=True)
#         return Response(serializer.data)