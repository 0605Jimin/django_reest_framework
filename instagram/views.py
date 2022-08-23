from django.shortcuts import render
from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework.views import APIView
from .serializers import PostSerializer
from .models import Post

# generics.ListAPIView
# generics.CreateAPIView

# generics.ListCreateAPIView

# generics.DestroyAPIView
# generics.UpdateAPIView

# class PublicPostListAPIView(generics.ListAPIView):
#     queryset = Post.objects.filter(is_public=True)
#     serializer_class = PostSerializer

# class PublicPostListAPIView(APIView):
#     def get(self, request):
#         qs = Post.objects.filter(is_public=True)
#         serializer = PostSerializer(qs, many=True)
#         return Response(serializer.data)

# public_post_list = PublicPostListAPIView.as_view()

@api_view(['GET'])
def public_post_list(request):
    qs = Post.objects.filter(is_public=True)
    serializer = PostSerializer(qs, many=True)
    return Response(serializer.data)

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


# @csrf_exempt
# def post_list(request):
#     pass

# def post_list(request):
#     pass

# post_list = csrf_exempt(post_list) 