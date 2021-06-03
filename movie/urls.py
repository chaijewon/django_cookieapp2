from django.urls import path
from movie import views
# 사용자가 URL을 보내면 => 해당 URL의 처리하는 함수 호출
# 화면 이동 => views.py <=> models.py
'''
     데이터베이스 목록 => 튜플 ()  => 수정이 불가능 
     브라우저 데이터 출력 => 딕트 {키:값} => Map
     튜플이 여러개 , 딕트가 여러개 => 리스트 [(),()] [{},{},{}] => ArrayList
     =====> COOKIES => {} 딕트  => get(key)
     
     movie_list =>  detail_before => movie_detail
         이미지 클릭   쿠키 저장   이동 
     movie_detail  => movie_list에서 쿠키에 저장된 데이터 출력  
        목록이동 
        
     쿠키 설정 
       response.set_cookie("키","데이터",저장기간(초단위))
       
     쿠키 읽기 
       request.COOKIES 
       => {}
       for => 원하는 키를 설정후에 데이터를 읽기 시작 
                 request.COOKIES.get("key")
      쿠키 삭제 
       response.delete_cookie("키")
       
       단점 : 문자열만 저장이 가능 
       장점 : 중복이 없다 => m영화번호
'''
urlpatterns=[
    path('',views.movie_list),
    path('detail/',views.movie_detail),
    path('before/',views.detail_before)
]