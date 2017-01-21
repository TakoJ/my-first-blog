from django.db import models
from django.utils import timezone

#object(= model) = 속성 + 행동(methods)
#class = define 'object(=model)', Post= name of model(항상 대문자시작)
class Post(models.Model):#(models.Model) = Post가 장고 모델임을 의미
    author = models.ForeignKey('auth.User') #다른 모델에 대한 링크
    title = models.CharField(max_length=200) #글자수가 제한된 텍스트 정의
    text = models.TextField()# 글자수 제한 없는 긴 텍스트
    created_date = models.DateTimeField(
            default = timezone.now)
    published_date = models.DateTimeField(
            blank = True, null = True)

    def publish(self): #method
        self.published_date = timezone.now()

    def __str__(self):
        return self.title
# Create your models here.
