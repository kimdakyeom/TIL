# web html & css 기초
## 웹 사이트
### 웹 사이트의 구성 요소
- HTML -> 구조
- CSS -> 표현
- Javascript -> 동작
### 웹 사이트와 브라우저
- 웹 사이트는 브라우저를 통해 동작함
- 브라우저마다 동작이 약간씩 달라서 문제가 생기는 경우가 많음(파편화)
- 해결책으로 웹 표준이 등장
  - 웹 표준이란?
  - 웹에서 표준적으로 사용되는 기술이나 규칙
  - 어떤 브라우저든 웹 페이지가 동일하게 보이도록 함(크로스 브라우징)

## 개발 환경 설정
- Visual Studio Code : HTML/CSS 코드 작성을 위한 Visual Studio Code 추천 확장 프로그램
- 크롬 개발자 도구 : 웹 브라우저 크롬에서 제공하는 개발과 관련된 다양한 기능을 제공

## HTML 기초
> HTML : Hyper Text Markup Language, 웹 페이지를 작성(구조화)하기 위한 언어

- Hyper Text란? 참조(하이퍼링크)를 통해 사용자가 한 문서에서 다른 문서로 즉시 접근할 수 있는 텍스트
- Markup Language란? 태그 등을 이용하여 문서나 데이터의 구조를 명시하는 언어

### HTML 기본 구조
- html : 문서의 최상위(root) 요소
- head : 문서 메타데이터 요소
  - 문서 제목, 인코딩, 스타일, 외부 파일 로딩 등
  - 일반적으로 브라우저에 나타나지 않는 내용
  - 메타데이터 : 데이터의 데이터(데이터를 설명하는 데이터)
- body : 문서 본문 요소
  - 실제 화면 구성과 관련된 내용
- title : 페이지의 제목 설정 요소
  - 페이지가 로드되는 브라우저의 탭에 이 제목이 표시
  - 북마크나 즐겨찾기에서 페이지를 설명하는 것으로도 사용

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>Document</title>
</head>
<body>

</body>
</html>
```

#### head 예시
- <title> : 브라우저 상단 타이틀
- <meta> : 문서 레벨 메타데이터 요소
- <link> : 외부 리소스 연결 요소 (CSS 파일, favicon 등)
- <script> : 스크립트 요소 (JavaScript 파일/코드)
- <style> : CSS 직접 작성

### html 주석
> 특수 마커 <!- 및 ->

```html
<!-- <p>주석!</p> -->
```
### 요소(element)
> `<h1>contents</h1>`
>
> HTML의 요소는 태그와 내용(contents)로 구성되어 있다.

- HTML 요소는 시작 태그와 종료 태그 그리고 태그 사이에 위치한 내용으로 구성
  - 요소는 태그로 컨텐츠(내용)를 감싸는 것으로 그 정보의 성격과 의미를 정의
  - 내용이 없는 태그들도 존재(닫는 태그가 없음)
    - `br`, `hr`, `img`, `input`, `link`, `meta`

- 요소는 중첩(nested)될 수 있음
  - 요소의 중첩을 통해 하나의 문서를 구조화
  - 여는 태그와 닫는 태그의 쌍을 잘 확인해야함
    - 오류를 반환하는 것이 아닌 그냥 레이아웃이 깨진 상태로 출력되기 때문에, 디버깅이 힘들어 질 수 있음

```html
<p>내 고양이는 <strong>아주</strong> 고약해.</p>
```

#### 인라인 / 블록 요소
- 인라인(inline)
  - display 속성값이 인라인(inline)인 요소는 새로운 라인(line)에서 시작하지 않는다.
  - 요소의 너비도 해당 라인 전체가 아닌 해당 HTML 요소의 내용(content)만큼만 차지한다.
  - `<span>`, `<a>`, `<img>`

```html
<p>
    <span style="background-color:grey; color:orange">span태그</span>는 display 속성값이 인라인인 요소입니다.
</p>
```

- 블록(block)
  - display 속성값이 블록(block)인 요소는 언제나 새로운 라인(line)에서 시작하며, 해당 라인의 모든 너비를 차지한다.
  - `<p>`, `<div>`, `<h>`, `<ul>`, `<ol>`, `<form>`

```html
<p style="border: 3px solid red">
    p요소는 display 속성값이 블록인 요소입니다.
</p>
```

#### 텍스트 요소
- `<a></a>` : href 속성을 활용하여 다른 URL로 연결하는 하이퍼링크 생성
- `<b></b>`, `<strong></strong>` : 굵은 글씨 요소, 중요한 강조하고자 하는 요소 (보통 긁은 글씨로 표현)
- `<i></i>`, `<em></em>` : 기울임 글씨 요소, 중요한 강조하고자 하는 요소 (보통 기울임 글씨로 표현)
- `<br>` : 텍스트 내에 줄 바꿈 생성
- `<img>` : src 속성을 활용하여 이미지 표현, alt 속성을 활용하여 대체 텍스트
- `<span></span>` : 의미 없는 인라인 컨테이너

#### 그룹 컨텐츠
- `<p></p>` : 하나의 문단 (paragraph)
- `<hr>` : 문단 레벨 요소에서의 주제의 분리를 의미하며 수평선으로 표현됨 (A Horizontal Rule)
- `<ol></ol>`, `<ul></ul>` : 순서가 있는 리스트 (ordered), 순서가 없는 리스트 (unordered)
- `<pre></pre>` : HTML에 작성한 내용을 그대로 표현, 보통 고정폭 글꼴이 사용되고 공백문자를 유지
- `<blockquote></blockquote>` : 텍스트가 긴 인용문, 주로 들여쓰기를 한 것으로 표현됨
- `<div></div>` : 의미 없는 블록 레벨 컨테이너

#### 문자 나타내기
- 제목
  - 제목 요소는 내용의 특정 부분이 제목 또는 내용의 하위 제목임을 구체화 할 수 있게 해준다.

```html
<h1>My main title</h1>
<h2>My top level heading</h2>
<h3>My subheading</h3>
<h4>My sub-subheading</h4>
```

- 문단
  - 일반적인 문자 내용을 나타낸다.

```html
<p>This is a single paragraph</p>
```

- 목록
  - 순서 없는 목록 : `<ul>` 요소로 둘러 쌓여 있다. ex) 쇼핑 목록
  - 순서 있는 리스트 : `<ol>` 요소로 둘러 쌓여 있다. ex) 조리법
  - 목록의 각 항목은 <li> (목록 항목) 요소 안에 놓여야 한다.

```html
<p>At Mozilla, we’re a global community of</p>
<ul>
  <li>technologists</li>
  <li>thinkers</li>
  <li>builders</li>
</ul>
<p>working together ... </p>
```

- 연결
  - 연결을 하기 위해, `<a>` 요소를 사용

```html
<a href="https://www.mozilla.org/en-US/about/manifesto/">Mozilla Manifesto</a>
```

### 속성(attribute)
> `<a href=“https://google.com”>Google</a>`
>
> 태그별로 사용할 수 있는 속성은 다르다.

- 속성을 통해 태그의 부가적인 정보를 설정할 수 있음
- 요소는 속성을 가질 수 있으며, 경로나 크기와 같은 추가적인 정보를 제공
- 요소의 시작 태그에 작성하며 보통 이름과 값이 하나의 쌍으로 존재
- 태그와 상관없이 사용 가능한 속성(HTML Global Attribute)들도 있음

#### HTML Global Attribute
> 모든 HTML 요소가 공통으로 사용할 수 있는 대표적인 속성 (몇몇 요소에는 아무 효과가 없을 수 있음)
- `id` : 문서 전체에서 유일한 고유 식별자 지정
- `class` : 공백으로 구분된 해당 요소의 클래스의 목록 (CSS, JS에서 요소를 선택하거나 접근)
- `data-*` : 페이지에 개인 사용자 정의 데이터를 저장하기 위해 사용
- `style` : inline 스타일
- `title` : 요소에 대한 추가 정보 지정
- `tableindex` :  요소의 탭 순서

### DOM(Document Object Model) 트리
- 텍스트 파일인 HTML 문서를 브라우저에서 렌더링 하기 위한 구조
  - HTML 문서에 대한 모델을 구성
  - HTML 문서 내의 각 요소에 접근 / 수정에 필요한 프로퍼티와 메서드를 제공

![DOM](web_html_css_basic.assets/DOM.png)

## CSS 기초
> Cascading Style Sheets, 스타일을 지정하기 위한 언어

- CSS 구문은 선택자를 통해 스타일을 지정할 HTML 요소를 선택
- 중괄호 안에서는 속성과 값, 하나의 쌍으로 이루어진 선언을 진행
- 각 쌍은 선택한 요소의 속성, 속성에 부여할 값을 의미(`속성:값` 형태로 사용)
  - 속성 (Property) : 어떤 스타일 기능을 변경할지 결정
  - 값 (Value) : 어떻게 스타일 기능을 변경할지 결정

```css
h1 {
  color: blue;
  font-size: 15px;
}
```

### CSS의 자주 사용되는 속성
- width , height : 가로길이, 세로길이
  - auto -> 기본값, 브라우저가 계산한 너비
  - px -> 픽셀
  - % -> 부모 요소에 상대적인 너비
  - initial -> 기본값으로 초기화
  - inherit -> 부모 요소로부터 상속 받은 값
- margin, padding : 바깥쪽 여백, 안쪽 여백
  - auto -> 기본값
  - px -> 픽셀

```css
margin:10px -> 상하좌우 모두 10px 여백
margin:20px 10px -> 상하 20px , 좌우 10px 여백
margin:40px 30px 20px 10px -> 위 40px, 오른쪽 20px, 아래 20px, 왼쪽10px 여백
margin:40px 30px 10px -> 위 40px, 좌우 30px, 아래 10px 여백

margin-top -> 위 여백 지정
margin-bottom -> 아래 여백 지정
margin-left -> 왼쪽 여백 지정
margin-right -> 오른쪽 여백 지정
```

- box-sizing : width 와 height 를 원하는 값으로 지정하여도, padding 이나 border 옵션을 주게 되면 가로길이나 세로길이가 그만큼 더해져서 요소가 커진다. 이는 box-sizing 옵션으로 바꿀 수 있다.
  - content-box -> default값이다. width를 지정하여도 padding이나 다른 속성들이 들어오면 요소가 그만큼 커진다.
  - border-box -> 다른 속성을 주어도 지정해둔 width 와 height의 크기를 벗어나지 않는다.
- color : 글자의 색상 지정
  - inherit -> 기본값, 부모의 색상을 가져온다.
  - red 또는 blue -> 이미 css로 정의된 색상
  - #000 또는 #FFFFFF -> 16진수의 색상코드
  - rgb(255,255,255) -> rgb 색상
  - rgba(200,100,150,0.5) -> 알파(투명도)가 적용된 rgba 색상
- font : 글자의 폰트 정의
  - font-style -> 기울기 등의 스타일 지정
  - font-weight -> 글자 두께
  - font-variant -> 글꼴 변형 (소문자를 대문자로 바꾸는 등)
  - font-size -> 글자 크기
  - line-height -> 줄 간격
  - font-family -> 글꼴
- text-align : 텍스트의 정렬 방향 지정
  - left
  - right
  - center
  - jutify -> 양쪽 정렬
- background : 태그의 배경을 지정
  - background-color -> 배경 색
  - background-image -> 배경 이미지
  - background-repeat -> 배경 이미지 반복 여부
  - background-position -> 배경 이미지 위치
- border : 테두리를 지정
  - border-width -> 테두리의 두께 px 단위사용
  - border-style -> 테두리의 스타일
  - border-color -> 테두리의 색상 .. color 값과 동일함
  - border-top, border-bottom, border-left, border-right
- border-radius : 테두리를 둥글게 만들어주는 속성
  - px와 % 단위 사용
  - 총 4개의 모서리를 각각 다른 값으로 줄 수 있다.
- visibility : 가시화 지정
  - visible -> 보임
  - hidden -> 숨김 (대신 영역은 차지함)
  - collapse -> 겹치도록 지정 (테이블 행과 열 요소만 지정할 수 있으며, 그외 요소 지정 시 hidden으로 해석)
  - inherit -> default 값, 부모 요소의 값을 상속
- display : 요소를 어떻게 보여줄지 지정
  - none -> 보이지 않음
  - block -> 블록 박스 (세로)
  - inline -> 인라인 박스 (가로)
  - inline-block -> 블록과 인라인의 중간 형태

### CSS 정의 방법
- 인라인
  - 해당 태그에 직접 style 속성 활용

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Document</title>
</head>
<body>
  <h1 style="color: blue; font-size: 100px;">Hello</h1>
</body>
</html>
```

- 내부 참조
  - <head> 태그 내에 <style>에 지정

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Document</title>
  <style>
    h1 {
      color: blue;
      font-size: 100px;
    }
  </style>
</head>
<body>
</body>
</html>
```

- 외부 참조
  - 외부 CSS 파일을 <head>내 <link>를 통해 불러오기

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <title>mySite</title>
  <link rel="stylesheet" href="mystyle.css">
</head>
<body>
  <h1> This is my site</h1>
</body>
</html>
```

```css
h1 {
  color: blue;
  font-size: 20px
}
```

### CSS with 개발자 도구
- `styles` : 해당 요소에 선언된 모든 CSS, 취소된 CSS까지 나열됨으로 내용이 굉장히 길고 복잡함

![styles](web_html_css_basic.assets/styles.png)

- `computed` : 해당 요소에 최종 계산된 CSS, 디자인대로 퍼블리싱되었는지 한눈에 확인 가능

![computed](web_html_css_basic.assets/computed.png)

### CSS 기초 선택자
- 요소 선택자
  - HTML 태그를 직접 선택
- 클래스(class) 선택자
  - `마침표(.)`문자로 시작하며, 해당 클래스가 적용된 항목을 선택
- 아이디(id) 선택자
  - `#` 문자로 시작하며, 해당 아이디가 적용된 항목을 선택
  - 일반적으로 하나의 문서에 1번만 사용
  - 여러 번 사용해도 동작하지만, 단일 id를 사용하는 것을 권장
- id > class > 태그 순으로 우선순위
- 같은 레벨이라면 나중에 '선언'된 것이 적용
- 일반적으로 CSS 스타일링은 클래스로만
- id는 문서에서 반드시 한번만 등장

## REFERENCE
- [HTML](https://developer.mozilla.org/ko/docs/Web/HTML)
- [CSS](https://developer.mozilla.org/ko/docs/Web/CSS)
- [DOM](https://ko.wikipedia.org/wiki/%EB%AC%B8%EC%84%9C_%EA%B0%9D%EC%B2%B4_%EB%AA%A8%EB%8D%B8)