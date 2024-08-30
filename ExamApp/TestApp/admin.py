from django.contrib import admin
from TestApp.models import *

# class CandidatedetailsAdmin(admin.ModelAdmin):
#     list_display = ['Username' , 'Department_name', 'access_key']

# admin.site.register(HOD , HODdetailsAdmin)

admin.site.register(Candidate)
admin.site.register(Question)
admin.site.register(Result)

# Register your models here.
