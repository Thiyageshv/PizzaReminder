from django.contrib import admin

# Register your models here.
from .models import userloc
from .models import groupusers
admin.site.register(userloc)
admin.site.register(groupusers)
	
