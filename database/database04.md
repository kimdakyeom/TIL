# database 04
## CASE
> 특정 상황에서 데이터를 변환하여 활용
>
> ELSE를 생략하는 경우 NULL 값 지정

```sql
CASE
  WHEN 조건식 THEN 식
  WHEN 조건식 THEN 식
  ELSE 식
END
```

## 서브쿼리
> 서브 쿼리는 특정한 값을 메인 쿼리에 반환하여 활용하는 것
>
> 실제 테이블에 없는 기준을 이용한 검색이 가능함
>
> 서브 쿼리는 소괄호로 감싸서 사용하며, 메인 쿼리의 칼럼을 모두 사용할 수 있음
>
> 메인 쿼리는 서브 쿼리의 칼럼을 이용할 수 없음

```sql
SELECT *
FROM 테이블
WHERE 컬럼1 = (
  SELECT 컬럼1
  FROM 테이블
);
```
- 단일행 서브쿼리
  - 서브쿼리의 결과가 0 또는 1개인 경우
  - 단일행 비교 연산자와 함께 사용(=, <, <=, >=, >, <>)
```sql
-- WEHRE에서의 활용
-- users에서 평균 계좌 잔고가 높은 사람의 수
SELECT COUNT(*)
FROM users
WHERE balance > (SELECT AVG(balance) FROM users);

-- SELECT에서의 활용
-- 전체 인원과 평균 연봉, 평균 나이
SELECT
  (SELECT COUNT(*) FROM users) AS 총인원,
  (SELECT AVG(balance) FROM users) AS 평균연봉
  (SELECT AVG(age) FROM users) AS 평균나이;

-- UPDTE에서의 활용
UPDATE users
SET balance = (SELECT AVG(balance) FROM users);
```
- 다중행 서브쿼리
  - 서브쿼리 결과가 2개 이상인 경우
  - 다중행 비교 연산자와 함께 사용(IN, EXISTS 등)
```sql
-- users에서 이은정과 같은 지역에 사는 사람의 수
SELECT COUNT(*)
FROM users
WHERE country IN (
  SELECT country
  FROM users
  WHERE first_name = '은정' AND last_name='이'
);
```
- 다중컬럼 서브쿼리
```sql
-- 특정 성씨에서 가장 어린 사람들의 이름과 나이
SELECT
  last_name,
  first_name,
  age
FROM users
WHERE (last_name, age) IN (
  SELECT last_name, MIN(age)
  FROM users
  GROUP BY last_name)
ORDER BY last_name;
```