# python 제어문

> 제어문이란?
>
> 파이썬은 기본적으로 위에서 아래로 순차적으로 명령을 수행한다.
>
> 특정 상황에 따라 코드를 선택적으로 실행하거나 계속해서 반복하는 제어가 필요하다.

## 조건문

> 조건문은 참/거짓을 판단할 수 있는 조건식과 함께 사용

#### 기본 형식

- expression에는 참/거짓에 대한 조건식
  - 조건이 참인 경우 이후 들여쓰기 되어있는 코드 블럭 실행

  - 이외의 경우 else 이후 들여쓰기 되어있는 코드 블럭 실행

    ```python
    if <조건>:
        # Run this code block
    else:
        # Run this code block
    ```

### 복수 조건문

```python
if <조건>:
	# Run this code block
elif <expression>:
    # Run this code block
elif <expression>:
    # Run this code block
else: # else 생략 가능
    # Run this code block
```

### 중첩 조건문

> 조건문은 다른 조건문에 중첩되어 사용 될 수 있다.

```python
if <조건>:
	# Run this code block
		if <조건>:
		# Run this code block
else:
	# Run this code block
```

### 조건표현식

> 조건 표현식을 일반적으로 조건에 따라 값을 할당할 때 활용한다.

```python
<true인 경우 값> if <조건> else <false인 경우 값>
```

## 반복문

> 특정 조건을 도달할 때까지 계속 반복되는 일련의 문장

### while문

> 조건식이 참인 경우 반복적으로 코드 실행

- 조건이 참인 경우 들여쓰기 되어 있는 코드 블록이 실행된다.
- 코드 블록이 모두 실행되고, 다시 조건식을 검사하며 반복적으로 실행된다.
- while문은 무한 루프를 하지 않도록 종료조건이 반드시 필요하다.

```python
while <조건>:
    # Run this code block
```

### for문

> 시퀀스(string, tuple, list, range)를 포함한 순회가능한 객체 요소를 모두 순회한다.

- 처음부터 끝까지 모두 순회하므로 별도의 종료조건이 필요하지 않다.

```python
for <변수명> in <iterable>:
    # Run this code block
```

#### 1. 문자열 순회

```python
chars = input()
# 문자열 순회
for char in chars:
    print(char)
# range를 활용하여 문자열 순회
for idx in range(len(chars)):
    print(chars[idx])
```

#### 2. enumerate 순회

> 인덱스와 객체를 쌍으로 담은 열거형 객체 반환
>
> (index, value) 형태의 tuple

```python
members = ['민수', '영희', '철수']
for i in range(len(members)):
print(f’{i} {members[i]}')
# enumerate 순회
for i, member in enumerate(members):
print(i, member)
```

#### 3. 딕셔너리 순회

> key를 순회하며 key를 통해 값 활용

```python
grades = {'john': 80, 'eric': 90}
for name in grades:
print(name, grades[name])
# john 80
# eric 90
```

### 반복문 제어

#### 1. beak

> break문을 만나면 반복문은 종료된다.

#### 2. continue

> continue 이후의 코드 블록은 수행하지 않고, 다음 반복을 수행한다.

#### 3. for-else

> 끝까지 반복문을 실행한 이후에 else문을 실행한다
>
> break를 통해 중간에 종료되는 경우에는 else문은 실행되지 않는다.
