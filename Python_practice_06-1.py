# 연습문제 06-1
# 문제 1: 빈 리스트를 만들어 그 안에 1,2,3을 넣었다가 순서대로 꺼내는 코드 실행흐름
"""
st=[]
st.append(1)
st.append(2)
st.append(3)
print(st)
st.remove(1)
st.remove(2)
st.remove(3)
print(st)

#문제 2
st = [1,2,3]
st.pop(0) #앞에서 부터 삭제 됨
print(st)
st.pop(-1)  #뒤에서 부터 삭제 됨
"""
#문제 3: for문을 이용하여 1-10까지 넣고 지우기 코드 제작
st=[]
for i in range(10):
	st.append(i+1)    # st[i].append로 제작하면 안됨!!!
print(st)

for i in range(10):
	st.pop(0)    # 맨 앞부터 꺼내기: 0   && 맨 뒤부터 꺼내기: -1
print(st)

#문제 6: 하나의 리스트에 다른 리스트 값 전부를 추가하는 코드
st1 =[1,2]
st1.extend([3,4,5])
print(st1)

st2= [1,2]
st2[2:3]=[3,4,5]
print(st2)