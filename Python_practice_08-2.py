#08-2문제
#문제1: 6과 45의 최소공배수를 구하는 코드를 while루프 기반으로 작성해보자. (참고로 6과 45로 나눠지는 제일 작은값: 최소공배수)
'''
cm=0
mix=45
while True:
    if mix %6 ==0 and mix% 45 ==0:
      cm=mix
      break
    mix=mix+1

print(cm)
'''
#문제2:  42와 120의 최대공약수를 구하는 코드 while루프 기반으로 작성해보자 
gcm = 0 
mix=42
while True:
	if 42% mix ==0 and 120% mix ==0:
		gcm = mix
		break
	mix-=1
print(gcm)

