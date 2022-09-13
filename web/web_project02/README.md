## 목표

- HTML를 통한 웹 페이지 마크업
- CSS를 통한 선택자 활용 및 속성 부여
- 시맨틱 태그를 활용한 기본 레이아웃 구성
- 영화 추천 사이트 메인 레이아웃 구성

## 준비 사항

1. **(필수)** HTML/CSS 환경 구성
2. **(필수)** Bootstrap

## 요구 사항

### 01_nav_footer.html

![nav_footer](web_project02.assets/nav_footer.png)

- navbar 좌측에는 영화 로고가 배치됩니다.
- 항목은 Home, Community, Login로 구성되어 있습니다.
    - Home은 02_home.html으로 링크를 구성합니다.
    - Community는 03_community.html으로 링크를 구성합니다.
    - Login은 Modal이 팝업됩니다.
        
        ![nav_footer2](web_project02.assets/nav_footer2.png)
        
- footer는 컨텐츠 최하단에 배치됩니다. 내용은 자유롭게 구성합니다.

### 02_home.html

![home](web_project02.assets/home.png)

- 01_nav_footer.html에서 작성한 Navigation bar & Modal & Footer 코드를 적절한 위치에 사용합니다.
- Carousel을 활용하여 이미지가 자동으로 전환될 수 있도록 합니다.
    - 이미지는 적절한 이미지를 찾아 변경 가능합니다.
- Boxoffice 문구는 `h2` 태그를 활용합니다.
- 영화 목록의 카드 배치는 반응형으로 합니다.
    - Viewport의 가로 크기가 576px 미만일 경우 한 행에 1개씩 표시됩니다.
        
        ![home2](web_project02.assets/home2.png)
        
    - Viewport의 가로 크기가 576px 이상일 경우 한 행에 2개 이상 표시됩니다.(자유롭게 설정 가능)
        
        ![home3](web_project02.assets/home3.png)
        
        ![home4](web_project02.assets/home4.png)
        

### 03_community.html

- 992px 이상
    
    ![community](web_project02.assets/community.png)
    
- 992px 미만
    
    ![community2](web_project02.assets/community2.png)
    
- 01_nav_footer.html에서 작성한 Navigation bar & Modal & Footer 코드를 적절한 위치에 사용합니다.
- Community 페이지는 크게 게시판 목록과 게시판으로 이루어져 있으며 반응형입니다.
- 게시판 목록(`aside`)은 클릭 가능하지만 연결된 링크는 없습니다.
    - Viewport의 가로 크기가 992px 미만일 경우 HTML main 요소 영역 전체만큼의 너비를 가집니다.
    - Viewport의 가로 크기가 992px 이상일 경우 HTML main 요소 영역 기준으로 좌측 1/6 만큼의 너비를 가집니다.
    - Viewport의 가로 크기 별 반응형 디자인은 스크린 샷 예시를 참고하여 일치하도록 합니다.
- Section (게시판)
    - 게시판은 Viewport의 가로 크기에 따라 전혀 다른 레이아웃으로 구성됩니다.
    - Viewport의 가로 크기가 992px 미만일 경우 게시판은 카드 형식으로 구성됩니다.
    - Viewport의 가로 크기가 992px 이상일 경우 테이블 형식으로 구성되며, HTML main 요소 영역 기준으로 우측 5/6 만큼의 너비를 가집니다.

## 후기 ✨
- 페어 프로그래밍을 진행하면서 해결되지 않는 문제에 대해 짝과 함께 여러 방법을 모색하는 경험이 정말 좋았다. 네비게이터가 되어서 짝에게 구현 방법을 설명해 주면서 나의 지식을 더 견고히 하는 느낌을 받았다.
- 반응형 웹 서비스를 위해 `d-none`, `d-block`을 사용해서 레이아웃을 숨기고 나타내는 방법을 이번 프로젝트를 통해 알게 되었다. 이 클래스를 통해 더 다양한 프로젝트를 진행할 수 있을 거라고 기대된다.
- 이번 프로젝트를 진행하면서 grid system의 `row`, `col` 클래스에 대해 확실히 이해할 수 있었다. 반응형 웹 서비스를 만들 때 자유자제로 사용할 수 있을 거라는 확신이 들었다.