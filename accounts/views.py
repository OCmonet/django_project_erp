from django.shortcuts import render
from django.http import HttpResponse

#내가 만든 accounts 앱! 앞으로 네가 할 일은 이거야.
#1.사용자의 첫 접근경로로('/') 로그인 페이지 보여주기
#2.회원가입 버튼 클릭 > 회원가입 경로호출('signup.html') > 회원가입 페이지 보여주기
#3.회원가입 기능 구현
#4.로그인 기능 구현
#5.로그인 성공 시 >  base.html 페이지 보여주기
#6.base.html 페이지에서 > 현재 재고 보기 클릭 시 > erp앱 쪽 inventory.html 켜는 url로 연결
#                     > 상품 목록 보기 클릭 시 > erp앱 쪽 product.html 켜는 url로 연결

def base_response(request):
    return HttpResponse("안녕하세요! 장고의 시작입니다!")