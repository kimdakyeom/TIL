# 마크다운

> plain text 기반의 마크업 언어

## 제목/소제목(Heading)

#의 개수에 따라 h1~h6까지 표현 가능하다.

## 목록(list)

### 순서가 없는 리스트 : -(hyphen), *(asterisk)

목록 활용시 단계를 tab, shift+tab으로 조절

- -
  - tab
- shift+tab

### 순서가 있는 리스트 : 1.

1. 1번 내용
2. 2번 내용
   1. tab 2-1번 내용


## 코드블록

### Fanced Code Block

- `(backtick) 기호 3개 활용해 작성

- //```+언어

- 특정 언어를 명시하면 Syntax highlighting 기능이 적용

  ``` python
  print('hello')
  # 주석
  ```

  ```html
  <h1>
      제목
  </h1>
  <!-- 주석 -->
  ```

### Inline Code Block

` print` 는 파이썬에서 출력하는 함수이다.

backtick 기호로 감싸준다.

## 링크

ctrl+click하면 들어갈 수 있다.

[실라버스 링크](https://syllabus.com)

현재 디렉토리의 파일에 접근하려면 ./(현재 디렉토리 접근) + 파일명

[] 안에 문자 () 안에 url 링크

## 이미지

- 아래의 이미지는 나오지 않음
  - 절대경로이기때문(C://~)

![snoopy](markdown.assets/snoopy.jpg)

- 아래의 이미지는 나옴
  - 상대경로
  - 마크다운.assets을 같이 공유하면

![snoopy](markdown.assets/snoopy-16569886330561.jpg)

## 인용문

> Life is short, you need python.

정의할 때 사용

## Table

타이포라 기능 적극 활용

본문 > 표 > 표 삽입(ctrl + t)

|      |      |      |
| ---- | ---- | ---- |
|      |      |      |
|      |      |      |
|      |      |      |

## 텍스트

**굵게(볼드체)** : `**` (ctrl+b)

*기울임(이탤릭체)* : `*` (ctrl+i)

***둘 다*** : `***`

~~취소선~~ : `~~`

### 수평선

`***`

***

## 기타 정리

띄어 쓰기 있는 것

- 제목(#)
- 목록(-, 1.)

띄어 쓰기 없는 것

`inline code bock` *기울임*  **굵게**

