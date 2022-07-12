# 1부터 n까지의 합을 구하여 출력하는 코드를 1) while 문 
# 2) for 문으로 각각 작성하시오.
# sum() 함수 사용 금지

n = 10

# 1) while 문
sum = 0
i = 1
while i <= n:
    sum += i
    i += 1
print(sum)

# 2) for 문
sum = 0
for i in range(1, n+1):
    sum += i
print(sum)