from django.contrib import admin
from .models import apply

class applyAdmin(admin.ModelAdmin):
    fields = ['name','major','student_id','email','phone','body','file','isFinal']

admin.site.register(apply,applyAdmin) # 기본 ModelAdmin으로 등록
# Register your models here.
