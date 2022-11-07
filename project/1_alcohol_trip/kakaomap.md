# Django 카카오 맵
> 크롤링으로 긁어온 데이터들 중 주소 데이터가 있어서 해당 주소에 대해 지도에 장소를 찍어보았다.

## kakao developers에 접속
- 앱 추가 후 javascript키를 가져온다.

## 지도 생성하기
- 지도를 생성하는 가장 기본적인 예제

[kakao api 지도 생성하기](https://apis.map.kakao.com/web/guide/#step2)
```html
<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8">
    <title>지도 생성하기</title>
    
</head>
<body>
<!-- 지도를 표시할 div 입니다 -->
<div id="map" style="width:100%;height:350px;"></div>

<script type="text/javascript" src="//dapi.kakao.com/v2/maps/sdk.js?appkey=발급받은 APP KEY를 사용하세요"></script>
<script>
var mapContainer = document.getElementById('map'), // 지도를 표시할 div 
    mapOption = { 
        center: new kakao.maps.LatLng(33.450701, 126.570667), // 지도의 중심좌표
        level: 3 // 지도의 확대 레벨
    };

// 지도를 표시할 div와  지도 옵션으로  지도를 생성합니다
var map = new kakao.maps.Map(mapContainer, mapOption); 
</script>
</body>
</html>
```
## 주소로 장소 표시하기
- 내가 구현하려고 했던 내용이 공식 문서에 친절히 설명되어 있다.
- 서버단에서 받아온 restaurant의 DB 내용으로 구현하였다.

[kakao api 주소로 장소 표시하기](https://apis.map.kakao.com/web/sample/addr2coord/)

```html
<h1 id="name">{{ restaurant.name }}</h1>
<p>주소: <span id="addr">{{ restaurant.address }}</span></p>


<script type="text/javascript" src="//dapi.kakao.com/v2/maps/sdk.js?appkey=6a80656638a5303b90499a7641382145&libraries=services,clusterer,drawing"></script>

<script>
  var mapContainer = document.getElementById('map'), // 지도를 표시할 div 
    mapOption = {
        center: new kakao.maps.LatLng(33.450701, 126.570667), // 지도의 중심좌표
        level: 3 // 지도의 확대 레벨
    };  

// 지도를 생성합니다    
var map = new kakao.maps.Map(mapContainer, mapOption); 

// 주소-좌표 변환 객체를 생성합니다
var geocoder = new kakao.maps.services.Geocoder();

// 주소로 좌표를 검색합니다
geocoder.addressSearch($("#addr").text(), function(result, status) {

    // 정상적으로 검색이 완료됐으면 
     if (status === kakao.maps.services.Status.OK) {

        var coords = new kakao.maps.LatLng(result[0].y, result[0].x);

        // 결과값으로 받은 위치를 마커로 표시합니다
        var marker = new kakao.maps.Marker({
            map: map,
            position: coords
        });

        // 인포윈도우로 장소에 대한 설명을 표시합니다
        var infowindow = new kakao.maps.InfoWindow({
            content: '<div style="width:150px;text-align:center;padding:6px 0;">{{ restaurant.name }}</div>'
        });
        infowindow.open(map, marker);

        // 지도의 중심을 결과값으로 받은 위치로 이동시킵니다
        map.setCenter(coords);
    } 
});    
</script>
```

## 구현하며 어려웠던 부분
라이브러리를 불러올 때 
```html
<script type="text/javascript" src="//dapi.kakao.com/v2/maps/sdk.js?appkey=APIKEY&libraries=LIBRARY"></script>
<script type="text/javascript" src="//dapi.kakao.com/v2/maps/sdk.js?appkey=APIKEY&libraries=services"></script>
<script type="text/javascript" src="//dapi.kakao.com/v2/maps/sdk.js?appkey=APIKEY&libraries=services,clusterer,drawing"></script>
```
세 개의 라이브러리가 모두 필요한 줄 알고 다 넣어줬지만 에러가 났다.

세번째 라이브러리만 넣어줬더니 잘 작동 되었다.