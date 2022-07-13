# 주어진 리스트의 요소 중에서 5의 개수를 출력하시오.

numbers = [7, 17, 10, 5, 4, 3, 17, 5, 2, 5]
ans = 0

for i in range(len(numbers)):
    if numbers[i] == 5:
        ans += 1
print(ans)