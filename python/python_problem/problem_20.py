# 정수 number가 주어질 때, 각 자릿수의 합을 구해서 출력하세요. 

number = 123
str_num = str(number)
sum = 0

for i in range(len(str_num)):
    sum += int(str_num[i])
print(sum)