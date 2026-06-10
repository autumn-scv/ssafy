# artists/views.py
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import ArtistSerializer

@api_view(['POST']) # POST 요청만 받겠다!
def artist_list(request):
    # 1. 사용자가 보낸 데이터(request.data)를 시리얼라이저에 넣습니다.
    serializer = ArtistSerializer(data=request.data)
    
    # 2. 데이터가 유효한지(비어있진 않은지, 형식은 맞는지) 검사합니다.
    if serializer.is_valid():
        # 3. 유효하다면 DB에 저장합니다.
        serializer.save()
        # 4. 요구사항대로 생성된 데이터와 201 상태코드를 반환합니다.
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    # 5. 유효하지 않다면(잘못된 정보) 400 상태코드를 반환합니다.
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)