import django_filters
import json
from rest_framework import filters 
from rest_framework import generics 
from rest_framework.response import Response
from rest_framework import viewsets, status
from auth import getresponse
from . import serializers
from . import yelp
from .serializers import locserializer, groupserializer
from .models import userloc, groupusers

# Global variable used for the sake of simplicity.
# In real life, you'll be using your own interface to a data store
# of some sort, being caching, NoSQL, LDAP, external API or anything else
global tasks
tasks = {}
def findobjects(term,userlist,userid):
    global tasks 
    tasks = {}
    for i,u in enumerate(userlist):
	print u,userid
	if int(u)==int(userid):
		continue 
	userlocob = userloc.objects.get(userid=u)
	x = userlocob.Lat
	y = userlocob.Long
    	items = getresponse(term,x,y)
	un = userlocob.username
	#print items
	if items is None:
		items = []
	resitem = json.dumps(items)
    	#print resitem
	tasks[i] = yelp(name=un,res=resitem)
    print tasks

def get_next_task_id():
    return max(tasks) + 1

class groupviewset(viewsets.ModelViewSet):
    serializer_class = groupserializer
    queryset = groupusers.objects.all()
    #user = get_object_or_404(queryset, pk=pk)
    def list(self, request):
        queryset = groupusers.objects.all()
        groupid = int(request.GET.get('groupid',False))
	groupob = groupusers.objects.get(groupid=groupid)
        serializer = serializers.groupserializer(groupob,partial=True)
        return Response(serializer.data)
    def create(self, request):
        groupid = request.GET.get('groupid')
	request.data['users']=json.dumps(request.data['users'])
        serializer = serializers.groupserializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def put(self,request):
        groupid = int(request.GET.get('groupid'))
	request.data['users']=json.dumps(request.data['users'])
	updateob = groupusers.objects.get(groupid=groupid)
        serializer=groupserializer(updateob,data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)	


class userlocviewset(viewsets.ModelViewSet):
    serializer_class = locserializer
    queryset = userloc.objects.all() 
    #user = get_object_or_404(queryset, pk=pk)
    def list(self, request):
        queryset = userloc.objects.all()
        userid = request.GET.get('userid')
        serializer = serializers.locserializer(queryset, many=True)
        return Response(serializer.data)
    def create(self, request):
        userid = request.GET.get('userid')
        Lat = request.GET.get('Lat')
        Long = request.GET.get('Long')
        serializer = serializers.locserializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def put(self,request):
        ruserid = str(request.GET.get('userid'))
        updateob = userloc.objects.get(userid=request.data['userid'])
        #user = get_object_or_404(updateob, pk=pk)
	serializer=locserializer(updateob,data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class TaskViewSet(viewsets.ViewSet):
    #Required for the Browsable API renderer to have a nice form.
    serializer_class = serializers.TaskSerializer
    def list(self, request):
        global tasks
        term = request.GET.get('term')
	groupid = request.GET.get('groupid',False)
	userid = request.GET.get('userid')
	print term,groupid,userid
	userob = groupusers.objects.get(groupid=groupid)
	userlist = json.loads(userob.users)
	print userob.users
	if userid not in userob.users:
		return Response(status=status.HTTP_400_BAD_REQUEST)
        findobjects(term,userlist,userid)
        serializer = serializers.TaskSerializer(instance=tasks.values(), many=True)
        return Response(serializer.data)

    def create(self, request):
        global tasks
        serializer = serializers.TaskSerializer(data=request.data)
        if serializer.is_valid():
            task = serializer.save()
            task.id = get_next_task_id()
            tasks[task.id] = task
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk=None):
        global tasks
        try:
            task = tasks[int(pk)]
        except KeyError:
            return Response(status=status.HTTP_404_NOT_FOUND)
        except ValueError:
            return Response(status=status.HTTP_400_BAD_REQUEST)

        serializer = serializers.TaskSerializer(instance=task)
        return Response(serializer.data)

    def update(self, request, pk=None):
        global tasks
        try:
            task = tasks[int(pk)]
        except KeyError:
            return Response(status=status.HTTP_404_NOT_FOUND)
        except ValueError:
            return Response(status=status.HTTP_400_BAD_REQUEST)

        serializer = serializers.TaskSerializer(data=request.data, instance=task)
        if serializer.is_valid():
            task = serializer.save()
            tasks[task.id] = task
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def partial_update(self, request, pk=None):
        global tasks
        try:
            task = tasks[int(pk)]
        except KeyError:
            return Response(status=status.HTTP_404_NOT_FOUND)
        except ValueError:
            return Response(status=status.HTTP_400_BAD_REQUEST)

        serializer = serializers.TaskSerializer(data=request.data,instance=task,partial=True)
        if serializer.is_valid():
            task = serializer.save()
            tasks[task.id] = task
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None):
        global tasks
        try:
            task = tasks[int(pk)]
        except KeyError:
            return Response(status=status.HTTP_404_NOT_FOUND)
        except ValueError:
            return Response(status=status.HTTP_400_BAD_REQUEST)

        del tasks[task.id]
        return Response(status=status.HTTP_204_NO_CONTENT)

