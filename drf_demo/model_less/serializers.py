from rest_framework import serializers
from . import yelp
from .models import userloc, groupusers



class groupserializer(serializers.Serializer):
	groupid = serializers.CharField(max_length=200)
	users = serializers.CharField(max_length=200)
	def create(self, validated_data):
         	return groupusers.objects.create(**validated_data)
	def update(self, instance, validated_data):
                instance.groupid = validated_data.get('groupid',instance.groupid)
                instance.users = validated_data.get('users',instance.users)
                instance.save()
                return instance


class locserializer(serializers.Serializer):
	userid = serializers.CharField(max_length=200)
	username = serializers.CharField(max_length=200)
	Lat = serializers.CharField(max_length=200)
	Long = serializers.CharField(max_length=200)
	'''def save(self):
		userid = self.validated_data['userid']
		Lat = self.validated_data['Lat']
		Long = self.validated_data['Long']
	'''	
	def create(self, validated_data):
        	return userloc.objects.create(**validated_data)
	
	def update(self, instance, validated_data):
        	instance.userid = validated_data.get('userid',instance.userid)
		instance.username = validated_data.get('username',instance.username)
		instance.Lat = validated_data.get('Lat', instance.Lat)
		instance.Long = validated_data.get('Long', instance.Long)
		instance.save()
        	return instance




class TaskSerializer(serializers.Serializer):
    #res = serializers.Listfield(child=serializers.CharField(max_length=256))
    name = serializers.CharField(max_length=256)
    res = serializers.CharField(max_length=256)
    #owner = serializers.CharField(max_length=256)
    #status = serializers.ChoiceField(choices=STATUSES, default='New')

    def create(self, validated_data):
        return yelp(name="", **validated_data)

    def update(self, instance, validated_data):
        for field, value in validated_data.items():
            setattr(instance, field, value)
        return instance
