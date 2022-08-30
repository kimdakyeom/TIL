# database 01
## 데이터베이스란
- **체계화된 데이터의 모임**
- 여러 사람이 공유하고 사용할 목적으로 통합 관리되는 정보의 집합
- 논리적으로 연관된 (하나 이상의) 자료의 모음으로 그 내용을 고도로 구조화 함으로써 검색과 갱신의 효율화를 꾀한 것
- 몇개의 자료 파일을 조직적으로 통합하여 자료 항목의 중복을 없애고 자료를 구조화하여 기억시켜 놓은 자료의 집합체
### 데이터베이스의 장점
- 데이터 중복 최소화
- 데이터 무결성 (정확한 정보 보장)
- 데이터 일관성
- 데이터 독립성 (물리적/논리적)
- 데이터 표준화
- 데이터 보안 유지
## 관계형 데이터베이스 (RDB, Relational Database)
> 서로 관련된 데이터를 저장하고 접근할 수 있는 데이터베이스 유형
>
> 키(key)와 값(value)들의 간단한 관계(relation)를 표(table) 형태로 정리한 데이터베이스
### 스미카(schema)
- 데이터베이스에서 자료의 구조, 표현방법, 관계 등 전반적인 **명세를 기술**한 것

|column|datatype|
|---|---|
|id|INT|
|name|TEXT|
|address|TEXT|
|age|INT|

### 테이블(table)
- 열(컬럼/필드)과 행(레코드/값)의 모델을 사용해 조직된 데이터 요소들의 집합

|id|name|address|age|
|---|---|---|---|
|1|홍길동|제주|20|
|2|김길동|서울|30|
|3|박길동|부산|40|

### 열(column)
- 각 열에 고유한 데이터 형식 지정
- 열, 컬럼, 필드 등의 이름으로 불림
- 위의 예시에서는 name이란 필드에 고객의 이름(TEXT) 정보가 저장

### 행(row)
- 실제 데이터가 저장되는 형태
- 행, 로우, 레코드 등의 이름으로 불림
- 위의 예시에서는 총 3명의 고객정보가 저장

### 기본키(Primary Key)
- 각 행(레코드)의 고유 값
- 반드시 설정해야 하며, 데이터베이스 관리 및 관계 설정 시 주요하게 활용

## 관계형 데이터베이스 관리 시스템 (RDBMS)
> 관계형 모델을 기반으로 하는 데이터베이스 관리시스템을 의미
>
> ex) mySQL, SQLite, PostgreSQL, ORACLE, SQLServer 등

### SQLite
- 서버 형태가 아닌 파일 형식으로 응용 프로그램에 넣어서 사용하는 비교적 가벼운 데이터베이스이기 때문에 학습을 할 때는 이 시스템을 사용할 것이다.

#### SQLite의 데이터 타입
- NULL
- INTEGER
  - 크기에 따라 0, 1, 2, 3, 4, 6 또는 8바이트에 저장된 부호가 있는 정수
- REAL
  - 8바이트 부동 소수점 숫자로 저장된 부동 소수점 값
- TEXT
- BLOB
  - 입력된 그대로 정확히 저장된 데이터

|Example Typenames From The CREATE TABLE Statement|Resulting Affinity|
|---|---|
|INT, INTEGER, TINYINT, SMALLINT, MEDIUMINT, BIGINT, UNSIGNED BIG INT, INT2, INT8|INTEGER|
|CHARACTER(20), VARCHAR(255), VARYING CHARACTER(255), NCHAR(55), NATIVE CHARACTER(70), NVARCHAR(100), TEXT, CLOB|TEXT|
|BLOB (no datatype specified)|BLOB|
|REAL, DOUBLE, DOUBLE PRECISION, FLOAT|REAL|
|NUMERIC, DECIMAL(10,5), BOOLEAN, DATE, DATETIME|NUMERIC|

## SQL (Structured Query Language)
> 관계형 데이터베이스 관리시스템의 데이터 관리를 위해 설계된 특수 목적으로 프로그래밍 언어
>
> 데이터베이스 스키마 생성 및 수정
>
> 자료의 검색 및 관리
>
> 데이터베이스 객체 접근 조정 관리

- DDL - 데이터 정의 언어(Data Definition Language)
  - 관계형 데이터베이스 구조(테이블, 스키마)를 정의하기 위한 명령어
  - CREATE, DROP, ALTER
- DML - 데이터 조작 언어(Data Manipulation Language)
  - 데이터를 저장, 조회, 수정, 삭제 등을 하기 위한 명령어
  - INSERT: 새로운 데이터 삽입(추가), SELECT: 저장되어있는 데이터 조회, UPDATE: 저장되어있는 데이터 갱신, DELETE: 저장되어있는 데이터 삭제
- DCL - 데이터 제어 언어(Data Control Language)
  - 데이터베이스 사용자의 권한 제어를 위해 사용하는 명령어
  - GRANT, REVOKE, COMMIT, ROLLBACK

### 테이블 생성 및 삭제
- `.database` - 데이터베이스 생성하기
- `.tables` - csv 파일을 table로 만들기
- `.schema table` - 특정 테이블의 스키마 조회
#### CREATE - 테이블 생성
```sql
CREATE TABLE classmates (
    id INTEGER PRIMARY KEY,
    name TEXT
);
```
#### DROP - 테이블 삭제
```sql
DROP TABLE classmates;
```
#### 필드 제약 조건
- NOT NULL : NULL 값 입력 금지
- UNIQUE : 중복 값 입력 금지 (NULL 값은 중복 입력 가능)
- PRIMARY KEY : 테이블에서 반드시 하나. NOT NULL + UNIQUE
- FOREIGN KEY : 외래키. 다른 테이블의 Key
- CHECK : 조건으로 설정된 값만 입력 허용
- DEFAULT : 기본 설정 값

## CURD
### CREATE
- INSERT
```sql
-- 테이블에 단일 행 삽입
INSERT INTO 테이블_이름 (컬럼1, 컬럼2) VALUES (값1, 값2);

-- 테이블에 정의된 모든 컬럼에 맞춰 순서대로 입력
INSERT INTO 테이블_이름 VALUES (값1, 값2, 값3);
```
### READ
- SELECT
  - 테이블에서 데이터를 조회
  - SQLite에서 가장 기본이 되는 문이며 다양한 절과 함께 사용(ORDER BY, DISTINCT, WHERE, LIMIT, GROUP BY …)
```sql
SELECT * FROM 테이블이름 WHERE 조건;
```
- LIMIT
  - 쿼리에서 반환되는 행 수를 제한
  - 특정 행부터 시작해서 조회하기 위해 OFFSET 키워드와 함께 사용하기도 함
-WHERE
  - 쿼리에서 반환된 행에 대한 특정 검색 조건을 지정
- SELECT DISTINCT
  - 조회 결과에서 중복 행 제거
### UPDATE
- UPDATE
  - 기존 행의 데이터를 수정
  - SET cluase에서 테이블의 각 열에 대해 새로운 값 설정
```sql
UPDATE 테이블이름 SET 컬럼1=값1, 컬럼2=값2 WHERE 조건;
```
### DELETE
- DELETE
  - 테이블에서 행을 제거
  - 중복 불가능한(UNIQUE) 값은 rowid를 기준으로 삭제
  - AUTOINCREMENT : SQLite가 사용되지 않은 값이나 이전에 삭제된 행의 값을 재사용하는 것을 방지
```sql
DELETE FROM 테이블이름 WHERE 조건;
```
