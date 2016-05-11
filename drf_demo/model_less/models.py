from django.db import models
import ast


# Create your models here.
class userloc(models.Model):
	#groupid = models.CharField(max_length=200)
	userid = models.CharField(max_length=200)
	username = models.CharField(max_length=200, default="kabali")
	Lat = models.CharField(max_length=200)
	Long = models.CharField(max_length=200)
	


class ListField(models.TextField):
	__metaclass__ = models.SubfieldBase
    	description = "Stores a python list"

    	def __init__(self, *args, **kwargs):
        	super(ListField, self).__init__(*args, **kwargs)

    	def to_python(self, value):
        	if not value:
            		value = []

        	if isinstance(value, list):
            		return value

       		return ast.literal_eval(value)

    	def get_prep_value(self, value):
    		if value is None:
           		 return value

        	return unicode(value)

    	def value_to_string(self, obj):
    		value = self._get_val_from_obj(obj)
        	return self.get_db_prep_value(value)





class groupusers(models.Model):
	groupid=models.CharField(max_length=200, null=True)
	users=models.CharField(max_length=200, null=True)
	
	def setusers(self,x):
		self.users=json.dumps(x)
	def getusers(self):
		return json.loads(self.users)	
	
