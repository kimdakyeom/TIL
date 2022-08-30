# algorithm 이차원 리스트 02
## 이차원 리스트
### 순회
- 이중 for문을 이용한 **행 우선 순회**
```python
matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 0, 1, 2]
]

# 행 탐색
for i in range(3):
    # 열 탐색
    for j in range(4):
        print(matrix[i][j], end=" ")
    print()

# 1 2 3 4
# 5 6 7 8
# 9 0 1 2
```
- 이중 for문을 이용한 **열 우선 순회**
```python
matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 0, 1, 2]
]

# 열 탐색
for i in range(4):
    # 행 탐색
    for j in range(3):
        print(matrix[j][i], end=" ")
    print()

# 1 5 9
# 2 6 0
# 3 7 1
# 4 8 2
```
### 전치
> 전치(transpose)란 행렬의 행과 열을 서로 맞바꾸는 것을 의미

![transpose](algorithm_2d_list02.assets/transpose.PNG)

```python
matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 0, 1, 2]
]

# 전치 행렬을 담을 이차원 리스트 초기화
# 행과 열의 크기가 반대
transposed_matrix = [[0] * 3 for _ in range(4)]

# 행 탐색
for i in range(4):
    # 열 탐색
    for j in range(3):
        # 행, 열 맞바꾸기
        transposed_matrix[i][j] = matrix[j][i]

"""
transposed_matrix = [
    [1, 5, 9],
    [2, 6, 0],
    [3, 7, 1],
    [4, 8, 2]
]
"""
```
### 회전
> 문제에서 이차원 리스트를 왼쪽, 오른쪽으로 90도 회전하는 경우 존재

![rotation](algorithm_2d_list02.assets/rotation.PNG)
- 왼쪽으로 90도 회전하기
```python
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

n = 3
rotated_matrix = [[0] * n for _ in range(n)]

for i in range(n):
    for j in range(n):
        rotated_matrix[i][j] = matrix[j][n-i-1]

"""
rotated_matrix = [
    [3, 6, 9],
    [2, 5, 8],
    [1, 4, 7]
]
"""
```

- 오른쪽으로 90도 회전하기
```python
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

n = 3
rotated_matrix = [[0] * n for _ in range(n)]

for i in range(n):
    for j in range(n):
        rotated_matrix[i][j] = matrix[n-j-1][i]

"""
rotated_matrix = [
    [7, 4, 1],
    [8, 5, 2],
    [9, 6, 3]
]
"""
```
## 잡담
점점 어려워지는 알고리즘 ..... 🔥