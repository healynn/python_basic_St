#문제1: 구구단 중에서 7단 출력(그 결과값이 짝수만 출력하기)
'''
for i in range(1,10):
 if (7*i) % 2: continue
print (7*i, end= ' ')
'''
#문제2: 2이상 100 미만의 정수 중에서 2와 3으로 둘다 안 나눠지는 수를 찾아서 출력
'''
i=2
while i<100:
	i+=1
	if i%2 ==0 or i%3 ==0:  #위의 조건을 "피해서" 출력한다
		continue
	print(i, end= ' ')

'''
#문제3: 문제 2의 결과에서 contiue를 사용하지 않고 출력해보기

i=2
while i<100:
	i+=1
	if i%2 !=0 and i%3 !=0: 
		print(i, end= ' ')