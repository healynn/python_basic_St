#문제 1: 정수를 입력하면, 그 수의 거듭제곱 값을 출력& 정수가 아닌 것을 입력하면 "정수가 아닙니다"를 출력
def main():
	num=int(input("정수를 입력하세요: "))
	if num>0: print(num**2)
	else: print("정수가 아닙니다.")
main()	