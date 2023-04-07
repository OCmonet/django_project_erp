from django.shortcuts import render
from django.http import HttpResponse

#내가 만든 erp 앱! 앞으로 네가 할 일은 이거야.
#1.inventory.html 켜는 url을 받아서 > inventory.html 페이지 보여주기
#  product.html 켜는 url을 받아서 > product.html 페이지 보여주기

#2.inventory.html의 기능들 함수 구현
# 현재 재고량 보여주기 함수들 (보유재 총가격, 후드티들, 청바지들, 양말들, 모자들 수량)
# 입고장치 함수들 (상품, 수량, 입고날짜, 금액 입력하여 제출하면 재고량보여주기 함수에 더하기 적용)
# 출고장치 함수들 (상품, 수량, 입고날짜, 금액 입력하여 제출하면 재고량보여주기 함수에 빼기 적용)

#3.product.html의 기능들 함수 구현
# 홈버튼 > base.html로 이동
# 상품등록 하기 기능
# 등록된 목록 보여주기 기능


# Create your views here.
def base_response(request):
    return HttpResponse("안녕하세요! 장고의 시작입니다!")