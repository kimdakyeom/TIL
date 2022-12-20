# 프로젝트 drf 시리얼라이저
## Serializer
> 직렬화? : 클라이언트로 모델 인스턴스(복잡한 데이터)를 보낼 때 JSON 타입(스트링 형태)으로 변환하는 것
>
> <-> deserializer : 클라이언트의 스트링 데이터를 받을 때 파이썬 기본 데이터 유형으로 받기 위해 변환하는 것

- 모델의 데이터를 직렬화시키기 때문에 그에 맞게 필드를 조정해야한다.

## 읽기만 하는 필드 (read_only)
- 할 일(todo)에 로그인 되어 있는 user의 email을 db에 저장하고, url로 넘어온 project pk로 프로젝트를 db에 저장 후, 시리얼라이저로 api에서 출력해준다.
- 원래 있던 comment 시리얼라이저 내용을 api로 함께 출력해준다.

### views.py
```python
project = Project.objects.get(pk=project_pk)

if request.user.email == member.user:
    if serializer.is_valid():  # 유효성 검사
        # 할일에 프젝정보랑 유저정보 넣어줌
        serializer.validated_data["project"] = project
        serializer.validated_data["user"] = request.user
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
```
### serializers.py
1. 모델에 정의하지 않아 새로 정의해야하는 필드
```python
class TodoSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source="user.email")
    project = serializers.ReadOnlyField(source="project.title")
    class Meta:
        model = Todo
        fields = "__all__"
```
- 필드를 이미 ReadOnlyField로 정의했기때문에 Char인지 Text인지 따로 선언할 필요가 없다.
- user 필드의 email와 project의 title을 가져오기 위해서 source에 적어준다. (특정 필드만 끌어올 때)

2. 모델에 정의한 필드
```python
class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        read_only_fields = ('id')
```
- api로 GET만 하고 POST나 PUT은 하지 않을 필드의 경우에는 Meta 클래스에서 read_only_fields로 정의한다.
- id 값은 읽어오기만 가능하고 새로 만들거나 수정하는 것은 불가능하다.

3. 시리얼라이저 자체를 직렬화
```python
class TodoSerializer(serializers.ModelSerializer):
    comments = CommentSerializer(read_only=True, many=True)
    class Meta:
        model = Todo
        fields = "__all__"
```
- comment serializer를 api로 read only 형태로 보내면 된다.
- 댓글은 여러 인스턴스가 있을 수 있으므로 many=True로 설정해준다.

## 쓰기만 하는 필드 (write_only)
- 모델에는 없지만 api에서 입력은 넘겨야하는 필드
- 보통 쓰기만 하는 필드는 모델에 정의할 일이 없거나 password처럼 기존에 AbstractUser 같은 곳에 이미 기본적으로 정의가 되어 있다.
- password가 대표적이다.
- read_only 필드처럼 write_only_fields에 몰아넣을 수 없다.

```python
password = serializers.CharField(wrtie_only=True)
```

## 둘 다 하는 필드
- 모델에 쓴 필드 그대로 사용이 가능해서 serializer에 아무것도 넣지 않아도 된다.

## 회고
시리얼라이저를 효율적으로 잘 쓴다면 따로 api를 새로 만들고 수정할 필요 없이 프론트가 필요한 데이터를 유용하게 보내줄 수 있다. drf의 핵심은 시리얼라이저라는 생각이 들었고, 이 시리얼라이저를 다루는 연습을 더 해야할 것같다. 프로젝트 초반에는 이 시리얼라이저가 뭔지도 잘 모르겠고 익숙치 않았는데 프론트 팀원들이 추가로 요구하는 데이터를 시리얼라이저를 통해 주고받으면서 시리얼라이저의 중요성을 계속 깨닫고 있다.