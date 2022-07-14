# 문자열 word가 주어질 때, Dictionary를 활용해서
# 해당 문자열에서 등장한 모든 알파벳 개수를 구해서 출력하세요.

word = 'banana'
dict = {}

for i in range(len(word)):
    dict[word[i]] = 0
for i in range(len(word)):
    if word[i] in dict:
        dict[word[i]] += 1
print(dict)