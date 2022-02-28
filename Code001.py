# python 문장 출력 방식

#방법1
print ("나는 %s색과 %s생을 좋아해요"%("파란","빨강"))

#방법2
print("나는 {0}색과 {1}색을 좋아해요".format("파란","빨간"))

#방법3
print("나는 {age}살이며, {color}색을 좋아해요".format(age = 20, color = "빨간"))

#방법4
age= 20
color="빨간"
print(f"나는 {age}살이며, {color}색을 좋아해요")

#줄바꿈
print("백문이 불여일견 \n 백견이 불여일타")  

#따음표 표시하는 법
print("저는 \"나도코딩\"입니다")  

# \r: 커서를 맨 앞으로 이동
# \b: 커서를 맨 앞으로 이동
# \t: 탭

# 사이트별로 비밀번호를 만들어주는 프로그램을 작성하시오.

url = "http://naver.com"
my_str= url.replace("http://","")
print(my_str)
my_str= my_str[:my_str]