# 1부터 n까지의 곱을 구하여 출력하는 코드를 1) while 문 
# 2) for 문으로 각각 작성하시오.

n = 5

# 1) while 문
mul = 1
i = 1
while i <= n:
    mul *= i
    i += 1
print(mul)

# 2) for 문
mul = 1
for i in range(1, n+1):
    mul *= i
print(mul)