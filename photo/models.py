from django.db import models

# Create your models here.

# 1. 모델 : 데이터베이스 저장될 데이터가 있다면 해당 데이터를 묘사한다.
# 2. 뷰(기능) : 계산, 처리 - 실제 기능, 화면
# 3. URL 맵핑 : 라우팅 테이블에 기록한다. urls.py에 기록 - 주소를 지정
# 4. 화면에 보여줄 것이있다 : 템플릿작성(html)

# 장고의 기본 유저 모델
# from django.contrib.auth.models import User
from django.conf import settings
from django.db.models.deletion import CASCADE
from django.db.models.fields import IntegerField
from django.urls import reverse

# settings.AUTH_USER_MODEL

# 외래키(ForeignKey) - User 테이블에서 해당 유저를 찾을 수 있는 주키
# 주키(PrimaryKey) - User 테이블에 1 admin x x x x
# User테이블에서 그 유저가 쓴 포토를 어떻게 불러올 것인지

class Photo(models.Model): # 기본적으로 id가 생성되고 id는 primarykey값을 가짐
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT, related_name='user_photos') 
    photo = models.ImageField(upload_to="photos/%y/%m/%d")
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created']

    def __str__(self):
        return self.author.username + " " + self.created.strftime("%y-%m-%d %H:%M:%S")

    def get_absolute_url(self):
        return reverse("photo:photo_detail", args=[self.id])
    
