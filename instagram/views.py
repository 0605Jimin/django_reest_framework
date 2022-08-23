from sysconfig import is_python_build
from django.shortcuts import render
from rest_framework import generics
from rest_framework.viewsets import ModelViewSet
from .serializers import PostSerializer
from .models import Post

class PublicPostListAPIView(generics.ListCreateAPIView):
    queryset = Post.objects.all() # filter(is_public=True)
    serializer_class = PostSerializer

class PostViewSet(ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    # 이 하나의 클래스가 아래의 두 개의 함수를 지원함

    # def dispatch(self, request, *args, **kwargs):
    #     print("request.body :", request.body) # print 비추천 logger 추천
    #     print("request.POST :", request.POST)
    #     return super().dispatch(request, *args, **kwargs)


# def post_list(request):
#     # 2개 분기
#     pass

# def post_detail(request, pk):
#     # request.method # => 3개 분기
#     pass