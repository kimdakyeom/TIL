# 프로젝트 네이버 뉴스 API
> 야구 관련 뉴스를 사이트에 띄워주기 위해 네이버 뉴스 API를 사용했다.

![ezgif com-gif-maker](https://user-images.githubusercontent.com/74820869/203451013-60a277ae-174f-4112-9cec-8f516d3077ce.gif)

## 네이버 공식문서
[네이버 뉴스 API 공식문서](https://developers.naver.com/docs/serviceapi/search/news/news.md)

## 구현
### `news.py`
- 네이버 뉴스 api 가져오기
```pyhon
import os
import sys
import urllib.request
from django.shortcuts import render


def news():
    client_id = "q3xdnYmqL_0__IhS5dX3"
    client_secret = "uBEGX8nUr4"
    encText = urllib.parse.quote("야구")
    url = "https://openapi.naver.com/v1/search/news?query=" + encText # JSON 결과
    # url = "https://openapi.naver.com/v1/search/news.xml?query=" + encText # XML 결과
    request = urllib.request.Request(url)
    request.add_header("X-Naver-Client-Id",client_id)
    request.add_header("X-Naver-Client-Secret",client_secret)
    response = urllib.request.urlopen(request)
    rescode = response.getcode()
    if(rescode==200):
        response_body = response.read()
        # print(response_body.decode('utf-8'))
    else:
        print("Error Code:" + rescode)
    return(response_body.decode('utf-8'))
```

### `views.py`
- news.py 임포트하기
- 뉴스에 포함된 ", ' 등 깨진 상태로 나오기 때문에 문자 치환해주기
- 딕셔너리형 문자열로 가져와진 내용을 json으로 변형한 후 html에 뿌려주기

```python
from news import news

def index(request):
    ex_news = news().replace("<b>", "").replace("<\/b>", "").replace("&quot;", "'").replace("&apos;", "'")
    temp_news = json.loads(ex_news)
    context = {
        "temp_news": temp_news,
    }
    return render(request, "articles/index.html", context)
```

- `index.html`
```html
<div class="col-12 col-md-12 col-xl-12 col-xxl-12 px-4 mt-4">
    <div class="row pt-4" style="background-color:white; border-radius:10px; overflow:hidden; height:100%;">
        <div class="col-12 col-md-12 mb-3" style="text-align:center; display:flex; flex-direction:row; align-items:center;">
            <h2 class="fw-bold" style="margin-bottom:0;">뉴스 기사</h2>
            <p class="ms-3" style="color:gray; font-size:1rem; margin-bottom:0;">최신 뉴스를 확인해보세요📰</p>
        </div>
        <div class="rolling_box mb-3" style="padding-left:0;">
            <ul id ="rolling_box" style="padding-left:0;">
              <li class="card_sliding" id ="first"><p></p></li>
              <li class="" id ="second"><p></p></li>
              <li class="" id ="third"><p></p></li>
            </ul>
        </div>
    </div>
</div>


<script>

let rollingData = [
                    {% for news in temp_news.items %}
                    {
                        title: "{{ news.title }}",
                        link: "{{ news.link }}",
                    },
                    {% endfor %}
                ]
console.log(rollingData)
let timer = 2000 // 롤링되는 주기 (1000 => 1초)

let first = document.getElementById('first')
let second = document.getElementById('second')
let third = document.getElementById('third')
let move = 2
let dataCnt = 1
let listCnt = 1

first.children[0].insertAdjacentHTML(`beforeend`, `<a href="${rollingData[0].link}">${rollingData[0].title}</a>`)

setInterval(() => {
    if(move == 2){
        first.classList.remove('card_sliding')
        first.classList.add('card_sliding_after')

        second.classList.remove('card_sliding_after')
        second.classList.add('card_sliding')

        third.classList.remove('card_sliding_after')
        third.classList.remove('card_sliding')

        move = 0
    } else if (move == 1){
        first.classList.remove('card_sliding_after')
        first.classList.add('card_sliding')

        second.classList.remove('card_sliding_after')
        second.classList.remove('card_sliding')

        third.classList.remove('card_sliding')
        third.classList.add('card_sliding_after')

        move = 2
    } else if (move == 0) {
        first.classList.remove('card_sliding_after')
        first.classList.remove('card_sliding')

        second.classList.remove('card_sliding')
        second.classList.add('card_sliding_after')

        third.classList.remove('card_sliding_after')
        third.classList.add('card_sliding')

        move = 1
    }
    
    if(dataCnt < (rollingData.length - 1)) {
        document.getElementById('rolling_box').children[listCnt].children[0].innerText = ""
        document.getElementById('rolling_box').children[listCnt].children[0].insertAdjacentHTML(`beforeend`, `<a href="${rollingData[dataCnt].link}">${rollingData[dataCnt].title}</a>`)
            dataCnt++
    } else if(dataCnt == rollingData.length - 1) {
        document.getElementById('rolling_box').children[listCnt].children[0].innerText = ""
        document.getElementById('rolling_box').children[listCnt].children[0].insertAdjacentHTML(`beforeend`, `<a href="${rollingData[dataCnt].link}">${rollingData[dataCnt].title}</a>`)
        dataCnt = 0
    }

    if(listCnt < 2) {
        listCnt++
    } else if (listCnt == 2) {
        listCnt = 0
    }

    console.log(listCnt)
}, timer);


</script>
```

## 어려웠던 부분
네이버 api로 가져온 뉴스 결과는 모두 딕셔너리 형태를 띈 문자열이었다. 이 안의 내용을 뿌려주기 위해 json 형태로 변환했다.
json을 디코딩 하던 도중 `JSONDecodeError`라는 에러가 나타났다. 깨진 내용을 대체하기 위해 replace를 했는데, replace 순서를 바꾸니 해당 에러가 사라졌다.
javascript에서 뉴스 내용을 뿌려줄때 insertAdjacentHTML 하기 전 무조건 innerText = ""을 해줘야한다. 아니면 rolling box의 첫번째 내용만 롤링이 된다.