# algorithm 순열과 조합
> python의 itertools를 이용하면 순열과 조합을 for문 없이 구현할 수 있다.

## 순열
### permutation (nPr)
> 순열이란 몇 개를 골라 순서를 고려해 나열한 경우의 수
>
> 서로 다른 n 개 중 r 개를 골라 순서를 정해 나열하는 가짓수

```python
import itertools

arr = ['A', 'B', 'C']
nPr = itertools.permutations(arr, 2)
print(list(nPr))

# [('A', 'B'), ('A', 'C'), ('B', 'A'), ('B', 'C'), ('C', 'A'), ('C', 'B')]
```

## 조합
### combination (nCr)
> 조합이란 서로 다른 n 개 중 r 개를 취하여 조를 만들 때, 이 하나하나의 조를 n 개 중에서 r 개 취한 조합

```python
import itertools

arr = ['A', 'B', 'C']
nCr = itertools.combinations(arr, 2)
print(list(nCr))

# [('A', 'B'), ('A', 'C'), ('B', 'C')]
```

## 이 외의 유용한 함수들
### `zip()`
- 동일한 개수로 이루어진 iterable한 객체들을 인수로 받아 묶어서 iterator로 반환
```python
z = zip([1, 2, 3], ('A', 'B', 'C'))
print(next(z)) # (1, 'A')
print(next(z)) # (2, 'B')
print(next(z)) # (3, 'C')
```

### `all()`
- iterable한 객체를 인수로 받아서 원소가 모두 참이면 True, 아니면 False를 반환
```python
a = all([1, 2, 3]) # True
a = all([0, 1, 2]) # False
```

### `any()`
- iterable한 객체를 인수로 받아서 원소가 하나라도 참이면 True, 아니면 False를 반환
```python
a = any([0, 1, 2]) # True
a = any([0, False, []] # False
```

### `chain()`
- iterable한 객체들을 인수로 받아 하나의 iterator로 반환
```python
c1 = [1, 2]
ca = ['A', 'B']
c = itertools.chain(c1, ca)
print(next(c)) # 1
print(next(c)) # 2
print(next(c)) # A
print(next(c)) # B
```