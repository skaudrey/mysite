from django.contrib import admin
from cmdb.models import UserInfo

# Register your models here.
admin.site.register(UserInfo)   #you have to register it if you wanna edit it in the django admin platform