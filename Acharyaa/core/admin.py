from django.contrib import admin
from .models import Country
from .models import DietaryNeed
from .models import Language
from .models import Religion
from .models import Subject
from .models import Post, Comment
from .models import Exam
# Register your models here.
from django.conf import settings
from django.contrib import admin
from django.contrib.contenttypes.admin import GenericTabularInline
from .models import Media

admin.site.site_header = settings.APP_NAME
admin.site.site_title = settings.APP_NAME
admin.site.index_title = "Welcome to " + settings.APP_NAME


class MediaInline(GenericTabularInline):
    model = Media
    extra = 1
class ParentAdmin(admin.ModelAdmin):
    list_display = ("username", "email", "first_name", "last_name")
    
    def get_queryset(self, request):
        qs = super().get_queryset(request)
        return qs.filter(groups__name="Parent")   # filter only parents
class TeacherAdmin(admin.ModelAdmin):
    list_display = ("username", "email", "first_name", "last_name")
    search_fields = ("first_name", "last_name", "username",'email')
    def get_queryset(self, request):
        qs = super().get_queryset(request)
        return qs.filter(groups__name="Teacher")   # filter only teacher

class PostCommentInline(admin.TabularInline):  # or StackedInline
    model = Comment
    extra = 0   # number of empty comment forms to show
    fields = ("user", "content", "created_at")
    readonly_fields = ("created_at",)

class PostAdmin(admin.ModelAdmin):   # Unfold styling
    list_display = ("title", "author", "status", "created_at")
    search_fields = ("title", "author__username")
    inlines = [PostCommentInline,MediaInline]

class ExamAdmin(admin.ModelAdmin):
    list_display = ("name", "status", "created_at")
    search_fields = ("name",)
 
class CountryAdmin(admin.ModelAdmin):
    list_display = ("name","iso")
    search_fields = ("name","iso")

class DietaryNeedAdmin(admin.ModelAdmin):
    list_display = ("name",)
    search_fields = ("name",)

class LanguageAdmin(admin.ModelAdmin):
    list_display = ("name",)
    search_fields = ("name",)

class ReligionAdmin(admin.ModelAdmin):
    list_display = ("name",)
    search_fields = ("name",)
class SubjectAdmin(admin.ModelAdmin):
    list_display = ("name","code","status",)
    search_fields = ("name","code","status",)

admin.site.register(Country, CountryAdmin)
admin.site.register(DietaryNeed,DietaryNeedAdmin)
admin.site.register(Language,LanguageAdmin)
admin.site.register(Religion,ReligionAdmin)
admin.site.register(Subject,SubjectAdmin)
admin.site.register(Post, PostAdmin)
admin.site.register(Exam, ExamAdmin)