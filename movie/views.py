from django.shortcuts import render,redirect
from movie import models

# Create your views here.
def movie_list(request):
    # if(page==null)page="1";
    try:
         page=request.GET['page']
    except Exception as e:
        page="1"
    curpage=int(page)
   #  영화 목록 데이터 받기
    movie_list=models.movie_list(curpage)
   # 총페이지
    totalpage=models.movie_totalpage()
   # 딕트로 변환 => 데이터 전송
    block=5
    startPage=((curpage-1)//block*block)+1
    endPage=((curpage-1)//block*block)+block
    '''
      startPage ==> curpage 1,2,3,4,5 => 1
                          curpage 6,7,8,9,10 => 6
      endPage ==> curpage 1,2,3,4,5 => 5
                        curppage 6,7,8,9,10 => 10 
    '''
    if endPage > totalpage:
        endPage=totalpage

    md=[]
    for m in movie_list:
        mod={"mno":m[0],"title":m[1],"poster":m[2]}
        md.append(mod)
    # COOKIES출력
    cookie_data=request.COOKIES #쿠키 전체 데이터 읽기
    cd=[]
    if cookie_data : #값이 존재  => None , 0 => False
        for key in cookie_data:  # key값만읽어 온다
            if key.startswith('movie'): #key시작이 movie인가
                data=request.COOKIES.get(key) #key에 해당되는 값을 가지고 와라
                info_data=models.movie_info(int(data)) #영화번호에 해당되는 영화정보
                id={"mno":info_data[0],"poster":info_data[1]}
                cd.append(id)

    return render(request,'movie/list.html',{"block":block,"startPage":startPage,"cd":cd,
                    "endPage":endPage,"curpage":curpage,"totalpage":totalpage,"md":md,"range":range(startPage,endPage+1)})

def movie_detail(request):
    mno=request.GET['mno']
    dd=models.movie_detail(int(mno))
    temp={"mno": dd[0],"poster": dd[1],"title":dd[2],"genre":dd[3],"grade":dd[4],
             "score":dd[5],"regdate":dd[6],"time":dd[7],"story":dd[8],"nation":dd[9],"key":dd[10]}
    return render(request,'movie/detail.html',temp)

def  detail_before(request):
    mno=request.GET['mno']
    response=redirect('/movie/detail/?mno='+str(mno))
    response.set_cookie("movie"+str(mno),str(mno),60*60*24)
    return response
