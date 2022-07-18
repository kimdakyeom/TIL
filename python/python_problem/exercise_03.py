# 두 수를 Input으로 받아 합을 구하는 코드이다.
# 코드에서 오류를 찾아 원인을 적고, 수정하세요.

# numbers는 문자형이다. 
# 덧셈을 하려면 정수형으루 바꿔야한다.

numbers = map(int, input().split())
print(sum(numbers))