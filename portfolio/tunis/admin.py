from django.contrib import admin
from .models import *

# Register your models here.


class UserSelfAdmin(admin.ModelAdmin):
    list_display = ['vacancy', 'phone', 'mail', 'work_experience', 'is_active']
    list_filter = ['vacancy', 'is_active']


class ProgressAdmin(admin.ModelAdmin):
    list_display = ['progress', 'number', 'is_active']
    list_filter = ['is_active']


class SkillsAdmin(admin.ModelAdmin):
    list_display = ['name', 'percentage', 'is_active']
    list_filter = ['is_active']


class ExperienceAdmin(admin.ModelAdmin):
    list_display = ['title', 'type_exp', 'year', 'is_active']
    list_filter = ['type_exp', 'is_active']


class ContactAdmin(admin.ModelAdmin):
    list_display = ['vk_link', 'tg_link', 'WhatsApp_link', 'gitHub_link', 'is_active']
    list_filter = ['is_active']


class FeedBackAdmin(admin.ModelAdmin):
    list_display = ['company', 'mail', 'time_create', 'name']
    list_filter = ['time_create']


class TypeProjectAdmin(admin.ModelAdmin):
    list_display = ['name']


class RoleAdmin(admin.ModelAdmin):
    list_display = ['name']


class ProjectAdmin(admin.ModelAdmin):
    list_display = ['name', 'type_project', 'stack', 'role', 'time']
    list_filter = ['type_project', 'time', 'role']


admin.site.register(UserSelf, UserSelfAdmin)
admin.site.register(Progress, ProgressAdmin)
admin.site.register(Skills, SkillsAdmin)
admin.site.register(Experience, ExperienceAdmin)
admin.site.register(Contact, ContactAdmin)
admin.site.register(FeedBack, FeedBackAdmin)
admin.site.register(Role, RoleAdmin)
admin.site.register(TypeProject, TypeProjectAdmin)
admin.site.register(Project, ProjectAdmin)

