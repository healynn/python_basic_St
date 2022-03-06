#09-1: 튜플과 레인지
#문제1: 튜플을 인자로 전달하면, 이를 리스트로 바꿔주는 함수 만들기

def to_list(t):   #to_list함수 선언: 매개변수 있음
	st = []       #st 리스트형 변수선언
	for i in t:   # t의 길이까지 반복 
		st.append(i) #append: 마지막에 추가한다
	return st

ds=("Hello")
ds= to_list(ds)
print(ds)