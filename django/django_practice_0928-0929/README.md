# 0928-0929 Django 실습
## 목표

CRUD 기능을 가진 Todo 서비스를 개발합니다.

## 결과물
![ezgif com-gif-maker (1)](https://user-images.githubusercontent.com/74820869/193289790-9c01ed1b-7a2b-43cb-acb5-75a322e258b3.gif)


## 요구사항

### 모델 Model

모델은 아래 조건을 만족해야 합니다.

다만, 기능 추가를 위해 필드를 추가해도 됩니다.

- 모델 이름 : Todo
- 모델 필드 및 속성
    
    
    | 필드 이름 | 역할 | 필드 | 속성 |
    | --- | --- | --- | --- |
    | content | 할 일 내용 | Char | max_length=80 |
    | completed | 완료 여부 | Boolean | default=False |
    | priority | 우선순위 | Integer | default=3 |
    | created_at | 생성 날짜 | Date | auto_now_add=True |
    | deadline | 마감 기한 | Date | null=True |

### 기능 View

아래 기능을 구현합니다.

- 할 일 추가하기 Create
    - 힌트
        1. create() 메소드를 활용합니다.
        2. 아래 데이터를 사용자에게 입력받아서 데이터를 생성합니다.
            - 내용 / 우선 순위 / 마감 기한
        3. 할 일 목록 페이지로 redirect 합니다.
- 할 일 목록 보기 Read
    - 힌트
        1. 모든 데이터를 id를 기준으로 오름차순으로 정렬해서 불러옵니다.
        2. 불러온 데이터를 템플릿에서 반복문을 사용해 1개씩 화면에 표시합니다.
- 할 일 완료(completed) 여부(True / False) 변경하기 Update
    - 힌트
        1. 삭제할 할 일의 id가 필요합니다.
        2. get() 메소드를 사용하여 변경할 데이터를 불러옵니다.
        3. 불러온 데이터의 상태를 변경 후 저장합니다.
        4. 할 일 목록 페이지로 redirect 합니다.
- 할 일 삭제하기 Delete
    - 힌트
        1. 삭제할 할 일의 id가 필요합니다.
        2. get() 메소드를 사용하여 변경할 데이터를 불러옵니다.
        3. 불러온 데이터를 삭제합니다.
        4. 할 일 목록 페이지로 redirect 합니다.

### 화면 Template

- 할 일 추가 폼 <form>
    - 할 일
        - `<input type = “text”>` 태그를 활용합니다.
        - 최대 입력 길이는 80입니다.
    - 우선 순위
        - `<select>` `<option>` 태그를 활용합니다.
        - 참고 자료 : [https://thrillfighter.tistory.com/572](https://thrillfighter.tistory.com/572)
    - 마감 기한
        - `<input type="date">` 태그를 활용합니다.
    - 할 일 추가 버튼
        - `<input type=”submit”>` 태그를 활용합니다.
    
- 할 일 목록 테이블 `<table>`
    - `<thead>`
        - 우선 순위 / 할 일 내용 / 생성 날짜 / 마감 기한 / 진행 상태 / 상태 변경 / 삭제 를 테이블 헤더로 사용합니다.
    - `<tbody>`
        - id를 기준으로 오름차순으로 정렬한 모든 데이터를 화면에 표시합니다.
    - 변경
        - 버튼을 누르면 해당 할 일의 상태(True / False)가 수정됩니다.
    - 삭제
        - 버튼을 누르면 해당 할 일이 삭제됩니다