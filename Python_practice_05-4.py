#연습문제 05-4
#문제1: 리스트에 모든 값의 합 계산하여 반환하는 값
def sum_all(st):
	sum=0
	for i in range(len(st)):
		sum+=st[i]
	return sum
print("문제 1번 정답:" ,sum_all([1,2,3,4,5]))


#문제 2: 리스트에 저장되어 있는 값을 역순으로 출력하는 함수 
def show_reverse(st1):
	for x in range(len(st1)):
		print(st1[(x+1)* -1],end = '')

show_reverse([1,2,3,4])