# 프로젝트 알람 기능
> 다른 유저가 댓글을 달면 알람이 오도록 하는 기능, 읽으면 해당 프로젝트로 들어가지고 알람은 사라진다.

## 서버 설계
### DB 설계
- 댓글을 단 사람, 받은 사람을 user를 외래키로 사용한다. 읽음 여부는 boolean 필드를 사용한다. 어느 프로젝트와 todo 글에 달렸는지도 저장한다.
```python
class Notification(models.Model):
    send_user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="send_user"
    )
    receive_user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="receive_user"
    )
    is_read = models.BooleanField(default=0)
    todo = models.ForeignKey(Todo, related_name="noti_todo", on_delete=models.CASCADE)
    project = models.ForeignKey(
        Project, related_name="noti_project", on_delete=models.CASCADE
    )
```

### view 설계
- GET 요청
  - `notification/`
  - 로그인한 유저가 댓글 받은 유저이고, 읽지 않은 알림을 응답한다.
```python
class NotificationList(APIView):
    def get(self, request):
        notifications = Notification.objects.filter(
            receive_user_id=request.user.pk, is_read=0
        )

        serializer = NotificationSerializer(notifications, many=True)
        return Response(serializer.data)
```
- POST 요청
  - `<int:project_pk>/todo/<int:todo_pk>/comment/`
  - comment에 대해 post 요청시 serializer를 통해 유효성 검사를 할때 notification에 데이터를 저장한다.
```python
class Commentlist(APIView):
    permissions_classes = [IsAuthenticated]

    def post(self, request, project_pk, todo_pk):
        serializer = CommentSerializer(data=request.data)
        project = Project.objects.get(pk=project_pk)
        todo = Todo.objects.get(pk=todo_pk)
        if serializer.is_valid():  # 유효성 검사
            serializer.validated_data["user"] = request.user
            serializer.validated_data["project"] = project
            serializer.validated_data["todo"] = todo
            serializer.save()  # 저장
            Notification.objects.create(
                send_user=request.user,
                receive_user=todo.user,
                todo=todo,
                project=project,
            )
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
```

- put 요청
  - `isread/<int:pk>/`
  - 해당 알림을 클릭하면 notification db에서 is_read 필드를 읽음처리해준다.
```python
class Isread(APIView):
    def put(self, request, pk, format=None):
        notification = Notification.objects.get(pk=pk)
        notification.is_read = 1
        notification.save()
        serializer = NotificationSerializer(notification)
        return Response(serializer.data)
```

## 클라이언트 설계
- 알림에 갯수와 알림에 해당하는 자세한 정보들을 가져온다.
```js
NotificationGet().then((response) => {
  this.noCnt = response.data.length
  for (let i = 0; i < response.data.length; i++) {
    this.comment.push([
      response.data[i].send_user.email,
      response.data[i].project.id,
      response.data[i].id,
      response.data[i].project.title,
      response.data[i].todo.id
    ])
  }
})
```

- 알림을 클릭하면 해당 프로젝트로 이동한다.
```js
clickRouter(dataId, todoId) {
  this.$router.push(
    {
      name: 'projectdetail',
      params: {id:dataId},
      hash: `#${todoId}`
    }
  )
}
```
- 읽음 처리
```js
async isRead(event) {
  const dataId = event.target.getAttribute('data-id')
  await isRead(dataId)
}
```

## 힘들었던 점
알림을 클릭하면 해당 프로젝트에 들어가서 모달까지 띄우려고 했으나 모달의 아이디로 자동으로 모달을 띄워주는 방법을 찾지 못했다. 그래서 해당 모달이 있는 곳까지 자동 드래그 하는 기능을 구현했지만 데이터를 불러오기 전에 드래그가 되어서 데이터가 보이지 않는 상황이 발생했다.(데이터를 불러오는데에 시간이 오래 걸렸다.) 지연 시간을 많이 주어도 가끔 그런 현상이 나타나서 그 기능은 빼기로 했다.