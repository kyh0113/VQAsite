# 관리자 페이지
from django.contrib import admin

# Register your models here.
from .models import Photo
class PhotoAdmin(admin.ModelAdmin):
    list_display=['id', 'created']
    raw_id_fields = ['author']
    list_filter = ['created', 'author'] 

    # forenkey모델 언더바 2개 하면 해당 모델의 하위키값을 검색할 수 있음 
    search_fields = ["author__username"]
    ordering=['-created']

admin.site.register(Photo, PhotoAdmin)