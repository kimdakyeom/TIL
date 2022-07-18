# 아래 코드는 1부터 N까지의 숫자에 2를 곱해서 변수에 저장하는 코드입니다.
# 코드에서 오류를 찾아 원인을 적고, 수정하세요.

# answer를 ()로 초기화한 것은 tuple을 의미하지만 튜플에 append를 사용할 수 없다.
# append를 사용하기 위해선 리스트형이여야한다.

N = 10
answer = []
for number in range(N + 1):
    answer.append(number * 2)

print(answer)