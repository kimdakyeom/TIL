# 주어진 리스트 numbers에서 두번째로 큰 수를 구하여 출력하시오.
# max() 함수 사용 금지

numbers = [0, 20, 100]
result = []

# 중복제거
for num in numbers:
    if num not in result:
        result.append(num)

# max 찾은 후 max 값 list에서 삭제
max = numbers[0]
for num in numbers:
    if num > max:
        max = num
    num += 1
result.remove(max)

# list에서 max 값 찾기
max = result[0]
for num in result:
    if num > max:
        max = num
    num += 1
print(max)