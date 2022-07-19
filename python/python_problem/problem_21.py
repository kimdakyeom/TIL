# 주어진 숫자를 뒤집은 결과를 출력하시오. 
# * 문자열이 아닌 숫자로 활용해서 풀어주세요. str() 사용 금지

number = 1234
mod = 1000
list = []

while mod > 0:
    list.append(number// mod)
    number %= mod
    mod = mod // 10
print(*list[::-1], sep='')