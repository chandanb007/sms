from django.contrib import admin
from student.models import Student,Performance
from teacher.models import Teacher
from parent.models import Parent
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
   
class StudentPerformance(admin.TabularInline):
    model = Performance
    extra = 0   # number of empty comment forms to show
    fields = ("year","exam","marksObtained","subject","totalMarks","finalGrade")
    readonly_fields = ("created_at",)

class StudentAdmin(admin.ModelAdmin):
    list_display = ("username", "email", "first_name", "last_name")
    search_fields = ("title", "author__username")
    inlines = [StudentPerformance,MediaInline]
    def get_queryset(self, request):
        qs = super().get_queryset(request)
        return qs.filter(groups__name="Student")   # filter only students
class ParentAdmin(admin.ModelAdmin):
    list_display = ("username", "email", "first_name", "last_name")
    
    def get_queryset(self, request):
        qs = super().get_queryset(request)
        return qs.filter(groups__name="Parent")   # filter only parents
class TeacherAdmin(admin.ModelAdmin):
    list_display = ("username", "email", "first_name", "last_name")
    
    def get_queryset(self, request):
        qs = super().get_queryset(request)
        return qs.filter(groups__name="Teacher")   # filter only teacher

class PostCommentInline(admin.TabularInline):  # or StackedInline
    model = Comment
    extra = 0   # number of empty comment forms to show
    fields = ("user", "content", "created_at")
    readonly_fields = ("created_at",)

class PostAdmin(admin.ModelAdmin):   # Unfold styling
    list_display = ("title", "author", "created_at")
    search_fields = ("title", "author__username")
    inlines = [PostCommentInline,MediaInline]

class ExamAdmin(admin.ModelAdmin):
    list_display = ("name", "status", "created_at")
 

admin.site.register(Country)
admin.site.register(DietaryNeed)
admin.site.register(Student, StudentAdmin)
admin.site.register(Teacher, TeacherAdmin)
admin.site.register(Parent, ParentAdmin)
admin.site.register(Language)
admin.site.register(Religion)
admin.site.register(Subject)
admin.site.register(Post, PostAdmin)
admin.site.register(Performance)
admin.site.register(Exam, ExamAdmin)