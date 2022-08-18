-- GROUP BY

-- 성별 갯수
SELECT last_name, COUNT(*)
FROM users
GROUP BY last_name;

-- GROUP BY에서 활용하는 컬럼을 제외하고는
-- 집계함수를 쓰세요.
SELECT last_name, AVG(age), COUNT(*)
FROM users
GROUP BY last_name;

-- 참고...
SELECT last_name, age
FROM users
WHERE last_name = '곽';
-- last_name  age
-- ---------  ---
-- 곽          25
-- 곽          30
-- 곽          28
-- 곽          15

-- GROUP BY는 결과가 정렬되지 않아요. 기존 순서와 바뀜
-- 원칙적으로 내가 정렬해서 보고 싶으면 ORDER BY!

SELECT *
FROM users
LIMIT 5;
-- first_name  last_name  age  country  phone          balance       
-- ----------  ---------  ---  -------  -------------  -------       
-- 정호          유          40   전라북도     016-7280-2855  370    
-- 경희          이          36   경상남도     011-9854-5133  5900   
-- 정자          구          37   전라남도     011-4177-8170  3100   
-- 미경          장          40   충청남도     011-9079-4419  250000 
-- 영환          차          30   충청북도     011-2921-4284  220  

SELECT last_name, COUNT(*)
FROM users
GROUP BY last_name
LIMIT 5;

-- last_name  COUNT(*)
-- ---------  --------
-- 강          23
-- 고          10
-- 곽          4
-- 구          2
-- 권          17

-- GROUP BY WHERE를 쓰고 싶다.
-- 100번 이상 등장한 성만 출력하고 싶음. 
SELECT last_name, COUNT(last_name)
FROM users
WHERE COUNT(last_name) > 100
GROUP BY last_name;
-- 오류 발생!
-- Parse error: misuse of aggregate: COUNT()
--   LECT last_name, COUNT(last_name) FROM users WHERE COUNT(last_name) > 100 GROUP

-- 조건에 따른 GROUP 하시려면
-- HAVING을 쓴다!
SELECT last_name, COUNT(last_name)
FROM users
GROUP BY last_name
HAVING COUNT(last_name) > 100;