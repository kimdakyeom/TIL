# 주어진 숫자의 평균을 구하는 코드를 작성하시오.
# sum(), len()  함수 사용 금지

numbers = [4, 10, 20]

num = 0
sum = 0
avg = 0
for num in numbers:
    sum += num
    num += 1
avg = sum / 3
print(format(avg, '.0f'))