# python 심화 함수
## Comprehension
### List Comprehension
> 표현식과 제어문을 통해 특정한 값을 가진 리스트를 간결하게 생성하는 방법

`[<expression> for <변수> in <iterable>]`

`[<expression> for <변수> in <iterable> if <조건식>]`

**예제**

**1~3의 세제곱의 결과가 담긴 리스트**

- 원래 썼던 방법
```python
list = []
for number in range(1, 4):
    list.append(number**3)
```
- List Comprehension
```python
[number**3 for number in range(1, 4)]
# 리스트에 append할 원소
            # 반복할 for문
```
## Dictionary Comprehension
> 표현식과 제어문을 통해 특정한 값을 가진 딕셔너리를 간결하게 생성하는 방법

`{key: value for <변수> in <iterable>}`

`{key: value for <변수> in <iterable> if <조건식>}`

**예제**

**1~3의 세제곱의 결과가 담긴 딕셔너리**
- 원래 썼던 방법
```python
dict = {}
for number in range(1, 4):
    dict[number] = number**3
```
- Dictionary Comprehension
```python
{number: number**3 for number in range(1, 4)}
# 딕셔너리에 추가할 원소
                   # 반복할 for문
```
## 람다(lambda) 형식
> 표현식을 계산한 결과값을 반환하는 함수로, 이름이 없는 함수여서 익명함수라고도 불린다.

`lambda [parameter] : 표현식`
- return문을 가질 수 없다.
- 간편 조건문 외 조건문이나 반복문을 가질 수 없다.
- 함수를 정의해서 사용하는 것보다 간결하게 사용이 가능하다.
- def를 사용할 수 없는 곳에서도 사용이 가능하다.

**예제**

**두 수를 더하는 함수**
- 원래 썼던 방법
```python
def sum(x, y):
    return x + y
```
- lambda 형식
```python
(lambda x,y: x + y)(10, 20)
```
### 람다를 이용하는 여러 가지 함수들
- `map(function, iterable)`
> 반복 가능한 것들의 모든 요소에 함수를 적용시킨 결과물이다.
>
> map object로 반환한다.

**예제**

**제곱 수 구하기**
- 원래 썼던 방법
```python
result = []
for i in range(5):
    result.append(i*i)
print(result)
```
- lambda 형식
```python
list(map(lambda x: x ** 2, range(5)))
```
- `filter(function, iterable)`
> 순회 가능한 데이터구조의 모든 요소에 함수를 적용하고, 그 결과가 True인 것들을 filter object로 반환한다.

**예제**

**홀수 구하기**
- 원래 썼던 방법
```python
def odd(n):
    return n % 2
numbers = [1, 2, 3]
result = filter(odd, numbers)
list(result)
```

- lambda 형식
```python
list(filter(lambda x: x % 2, range(1, 3)))
```