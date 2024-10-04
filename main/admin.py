from django.contrib import admin
from main.models import Project,Skill,Qualification
# Register your models here.


class ProjectAdmin(admin.ModelAdmin):
    list_display=('project_image','project_title','des','url')
class SKillAdmin(admin.ModelAdmin):
    list_display=('name','percent','des')
class QualificationAdmin(admin.ModelAdmin):
    list_display=('name','year','grade','percentage','description')
    
admin.site.register(Project)
admin.site.register(Qualification)
admin.site.register(Skill,SKillAdmin)


