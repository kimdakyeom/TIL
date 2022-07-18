# 아래 코드는 평균을 구하는 논리적으로 오류가 있는 코드입니다. 
# 코드에서 오류를 찾아 원인을 적고, 수정하세요.

# count를 for문 밖에 설정해서 count가 올라가지 않는다.
# count를 for문 안으로 변경했다.
# //는 몫을 구하는 연산이므로 /를 사용해서 값이 제대로 나오게 변경했다.

number_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

total = 0
count = 0

for number in number_list:
    total += number
    count += 1

print(total / count)