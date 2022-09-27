# 실습 문제

1. 아래 내용의 데이터 추가하기.
   - content : 실습 제출
   - priority : 5
   - deadline : 2022-09-27

```py
Todo.objects.create(content='실습 제출',
priority=5,
deadline='2022-09-27')
```

2. 모든 데이터를 id를 기준으로 오름차순으로 정렬해서 가져오기.

```py
todos = Todo.objects.order_by('id')
for i in todos:
   print(i.id, i.content, i.priority, i.completed, i.created_at, i.deadline)
```

3. 모든 데이터를 deadline을 기준으로 내림차순으로 정렬해서 가져오기.

```py
todo = Todo.objects.order_by('-deadline')
for i in todo:
   print(i.id, i.content, i.priority, i.completed, i.created_at, i.deadline)
```

4. 모든 데이터를 priority가 높은 순으로 정렬해서 가져오기.

```py
todo = Todo.objects.order_by('priority')
for i in todo:
   print(i.id, i.content, i.priority, i.completed, i.created_at, i.deadline)
```

5. priority가 5인 모든 데이터를 id를 기준으로 오름차순으로 정렬해서 가져오기.

```py
todo = Todo.objects.filter(priority=5).order_by('id')
for i in todo:
   print(i.id, i.content, i.priority, i.completed, i.created_at, i.deadline)
```

6. completed가 True인 모든 데이터를 id를 기준으로 오름차순으로 정렬해서 가져오기.

```py
todo = Todo.objects.filter(completed=True).order_by('id')
for i in todo:
   print(i.id, i.content, i.priority, i.completed, i.created_at, i.deadline)
```

7. priority가 5인 데이터의 개수

```py
count = Todo.objects.filter(priority=5).count()
print(count)
```

```python
15
```
8. id가 1인 데이터 1개 가져오기.

```py
todo = Todo.objects.get(id=1)
print(todo.id)
```

9. id가 1인 데이터 삭제하기.

```py
todo = Todo.objects.get(id=1)
todo.delete()
```

10. id가 10인 데이터의 priority 값을 5로 변경하기.

```py
todo = Todo.objects.get(id=10)
todo.priority = 5
todo.save()
```
