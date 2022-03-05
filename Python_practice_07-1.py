#문제 1: 프로그램 사용자로부터 정수를 하나 입력받아서, 그 값에 대해 다음 답변
'''
def main():
	num=int(input("입력한 값:"))
	if num>=0:
		print("입력한 값은 0이거나 0보다 큽니다.")
	else:
		print("입력한 값은 0보단 작습니다.")

main()
'''
#문제2: 1보다 크면서 5보다 작은 가를 묻는 문장 만들기 [1<num<5 수식 사용]
'''
num=6
if 1<num<5: print("True")
else: print("False")
'''
#문제3
'''
num=12
if 3<num<10: print("True")
else: print("False")
'''
#문제4
'''
num = 4
if (num%2) == 0 and (num%3)!=0: print("True")
else: print("False")	
'''
#문제5: 정수를 받아 답변 입력

def main():
	num= int(input("값을 입력하시오:"))
	if 10<=num<12:
		print("입력하신 값은 10이상 20미만입니다.")
main()