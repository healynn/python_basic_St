#06-2문제
#문제1: 대문자/ 소문자 출력
str= "The Espresso Spirit"
lcp= str.lower()
ucp =str.upper()
print(lcp,ucp)
#문제2: 주민등록번호에서 필요한 정보 추출하기
p1= "970609-2011345"

def birth_only(pn):   #매개변수에 그냥 아무것나 쓰기
	str =p1.split('-')
	return str[0]
print(birth_only(p1))