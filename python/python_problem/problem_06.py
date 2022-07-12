# 주어진 리스트 numbers에서 최댓값을 구하여 출력하시오.
# max() 함수 사용 금지

numbers = [0, 20, 100]

num = 0
max = numbers[0]
for num in numbers:
    if num > max:
        max = num
    num += 1
print(max)