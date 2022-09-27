# ORM 실습 문제
## 실습 모델 정보
- 모델 이름 : Todo
- 모델 필드 : 

|필드 이름|역할|필드|속성|
|----|----|----|----|
|id|기본키||||
|content|할 일 내용|Char|max_length=80|
|completed|완료 여부|Boolean|default=False|
|priorty|우선순위|Integer||
|created_at|생성 날짜|Date|auto_now_add=True|
|deadline|마감 기한|Date|null=True|

1. 아래 내용의 데이터 추가하기.
    - content : 실습 제출
    - priority : 5
    - deadline : 2022-09-27

2. 모든 데이터를 id를 기준으로 오름차순으로 정렬해서 가져오기.
 
3. 모든 데이터를 deadline을 기준으로 내림차순으로 정렬해서 가져오기.

4. 모든 데이터를 priority가 높은 순으로 정렬해서 가져오기.

5. priority가 5인 모든 데이터를 id를 기준으로 오름차순으로 정렬해서 가져오기.

6. completed가 True인 모든 데이터를 id를 기준으로 오름차순으로 정렬해서 가져오기.

7. priority가 5인 데이터의 개수.

8. id가 1인 데이터 1개 가져오기.
        
9. id가 1인 데이터 삭제하기.
        
10. id가 10인 데이터의 priority 값을 5로 변경하기.