# Git/GitHub 02
## 원격저장소 - github

> github은 버전을 관리한다.
>
- 로컬 저장소의 버전을 원격저장소로 보낸다.

![computer-16571176011124](git_github02.assets/computer-16571176011124.PNG)![right_arrow](git_github02.assets/right_arrow.png)![github-16571175921563](git_github02.assets/github-16571175921563.PNG)

```bash
$ git push '파일명'
```

- 원격저장소의 버전을 로컬 저장소로 가져온다.

![github](git_github02.assets/github.PNG)![right_arrow-16571230494651](git_github02.assets/right_arrow-16571230494651.png)![computer-16571176011124-16571230964142](git_github02.assets/computer-16571176011124-16571230964142.PNG)

```bash
$ git pull '파일명'
```

## github에서 원격 저장소 만들기

- New Repository -> 저장소에서 이름/설명/공개 여부 설정 -> github 주소 확인 후

```bash
$ git remote add origin https://github.com/kimdakyeom/0706.git
```

## 원격저장소 git 활용 명령어

```bash
$ git clone <url> // 원격저장소 복제
$ git remote -v // 원격저장소 정보 확인
$ git remote add <원격저장소> <url> // 원격저장소 추가(default:origin)
$ git remote rm <원격저장소> // 원격저장소 삭제
$ git push <원격저장소> <브랜치> // 원격저장소에 push
$ git pull <원격저장소> <브랜치> // 원격저장소로부터 pull
```

## git branch

### 1. branch 관련 명령어

```bash
// git branch를 위해 root-commit을 발생시키고 진행해야 한다.
$ touch README.md
$ git add .
$ git commit -m 'init'
// branch 생성
$ git branch {브랜치명}
// branch 이동
$ git checkout {브랜치명}
// branch 생성 및 이동 한번에
$ git checkout -b {브랜치명}
// branch 삭제
$ git branch -d {브랜치명}
// branch 목록
$ git branch
// branch 병합(master 브랜치에서 {브랜치명}을 병합)
$ git merge {브랜치명}
```

### 2. branch 병합 시나리오

> **branch의 다양한 시나리오는 3가지로 나뉜다.**

#### 상황 1. fast-foward

> feature 브랜치가 생성된 이후 master 브랜치에 변경 사항이 없는 상황(**master만 변경**)

![1](git_github02.assets/1.PNG)

1. feature/home branch 생성 및 이동

```bash
(master) $ git branch feature/home
(master) $ git checkout feature/home
```

2. 작업 완료 후 commit

```bash
(feature/home) $ touch home.txt
(feature/home) $ git add .
(feature/home) $ git commit -m 'Add home.txt'
(feature/home) $ git log --oneline
b534a34 (HEAD -> feature/home) Complete Home!!!!
e89616a (master) Init
```

3. master 이동

```bash
(feature/home) $ git checkout master
(master) $ git log --oneline
```

4. master에 병합

```ba
(master) $ git merge feature/home 
Updating e89616a..b534a34
Fast-forward
 home.txt | 0
 1 file changed, 0 insertions(+), 0 deletions(-)
 create mode 100644 home.txt
```

5. 결과

```bash
(master) $ git log --oneline
b534a34 (HEAD -> master, feature/home) Complete Home!!!!
e89616a Init
```

6. branch 삭제

```bash
(master) $ git branch -d feature/home 
Deleted branch feature/home (was b534a34).
```


***


#### 상황 2. merge commit

> 서로 다른 commit을 merge하는 과정에서 서로 다른 파일이 수정되어 있는 상황
>
> git이 auto merging을 진행하고, commit 발생

![2](git_github02.assets/2.PNG)

1. feature/about branch 생성 및 이동

```bash
(master) $ git checkout -b feature/about
(feature/about) $
```

2. 작업 완료 후 commit

```bash
(feature/about) $ touch about.txt
(feature/about) $ git add .
(feature/about) $ git commit -m 'Add about.txt'
(feature/about) $ git log --oneline
5e1f6de (HEAD -> feature/about) 자기소개 페이지 완료!
b534a34 (master) Complete Home!!!!
e89616a Init
```

3. master 이동

```bash
(feature/about) $ git checkout master
(master) $
```

4. master에 추가 commit 이 발생시키기!!
   - 다른 파일을 수정 혹은 생성하세요!

```bash
(master) $ touch master.txt
(master) $ git add .
(master) $ git commit -m 'Add master.txt'
(master) $ git log --oneline
98c5528 (HEAD -> master) 마스터 작업....
b534a34 Complete Home!!!!
e89616a Init
```

5. master에 병합

```bash
(master) $ git merge feature/about
```

6. 결과 -> 자동으로 merge commit 발생
7. 커밋 및 그래프 확인하기

```bash
$ git log --oneline --graph
*   582902d (HEAD -> master) Merge branch 'feature/about'
|\
| * 5e1f6de (feature/about) 자기소개 페이지 완료!
* | 98c5528 마스터 작업....
|/
* b534a34 Complete Home!!!!
* e89616a Init
```

8. branch 삭제

```bash
$ git branch -d feature/about 
Deleted branch feature/about (was 5e1f6de).
```


***


#### 상황3. merge commit 충돌

> 서로 다른 commit을 merge하는 과정에서 **같은 파일의 동일한 부분**이 수정되어 있는 상황
>
> git이 auto merging을 하지 못하고, 충돌 메시지가 뜬다.
>
> 해당 파일의 위치에 표준형식에 따라 표시 해준다.
>
> 원하는 형태의 코드로 직접 수정을 하고 직접 commit을 발생시켜야한다.

![3](git_github02.assets/3.PNG)

1. feature/test branch 생성 및 이동

```bash
(master) $ git checkout -b feature/test
```

2. 작업 완료 후 commit

```bash
# README.md 파일 열어서 수정
(feature/test) $ touch test.txt
(feature/test) $ git add .
(feature/test) $ git commit -m 'Add test.txt'
(feature/test) $ git log --oneline
95fad1c (HEAD -> feature/test) README 수정하고 test 작성하고
582902d (master) Merge branch 'feature/about'
98c5528 마스터 작업....
5e1f6de 자기소개 페이지 완료!
b534a34 Complete Home!!!!
e89616a Init
```

3. master 이동

```bash
$ git checkout master
```

4. master에 추가 commit 발생시키기

```bash
# README.md 파일 열어서 수정
(master) $ git add README.md
(master) $ git commit -m 'Update README.md'
```

5. master에 병합

```bash
(master) $ git merge feature/test 
Auto-merging README.md
CONFLICT (content): Merge conflict in README.md
Automatic merge failed; fix conflicts and then commit the result.
```

6. 결과 -> merge conflict 발생
   - git status 명령어로 충돌 파일 확인

```bash
(master|MERGING) $ git status
On branch master
You have unmerged paths.
  (fix conflicts and run "git commit")        
  (use "git merge --abort" to abort the merge)

Changes to be committed:
        new file:   test-1.txt
        new file:   test-2.txt
        new file:   test.txt

Unmerged paths:
  (use "git add <file>..." to mark resolution)
        both modified:   README.md
```

7. 충돌 확인 및 해결

```bash
<<<<<<< HEAD
# 마스터에서 작업함...
=======
# 테스트에서 작성
>>>>>>> feature/test
```

8. merge commit 진행

```bash
(master|MERGING) $ git add .
(master|MERGING) $ git commit
```

* vim 편집기 화면이 나타납니다.

     * 자동으로 작성된 커밋 메시지를 확인하고, `esc`를 누른 후 `:wq`를 입력하여 저장 및 종료를 합니다.
     * `w` : write
     * `q` : quit
* vs code 편집기에서 메시지보고 닫아주세요~!

9. 커밋 및 확인하기

```bash
(master) $ git log --oneline --graph
*   bc1c0cd (HEAD -> master) Merge branch 'feature/test'
|\  
| * 95fad1c (feature/test) README 수정하고 test 작성하고
* | 2ecad28 리드미 수정
|/  
*   582902d Merge branch 'feature/about'
|\  
| * 5e1f6de 자기소개 페이지 완료!
* | 98c5528 마스터 작업....
|/  
* b534a34 Complete Home!!!!
* e89616a Init
```

10. branch 삭제

```bash
(master) $ git branch -d feature/test
```

## Pull Request

> push 권한이 없는 오픈 소스 프로젝트에 기여할 때 사용한다.
>
> 당황스러운 코드 충돌을 줄일 수 있다.

### 방법

#### 1. Fork

Upstream Repository를 자신의 저장소로 Fork(Origin Repository)한다.

#### 2. clone

fork로 생성한 Repository에서 `clone or download` 버튼을 누르고 나오는 URL을 복사한다.

```bash
$ git clone <복사한 URL>
```

#### 3. 내 컴퓨터에 생성된 로컬저장소에 원격저장소 추가

```bash
$ git remote add origin <원본 저장소 URL>
// 원격 저장소 확인
$ git remote -v
```

#### 4. branch 생성

```bash
// 브랜치 생성 및 이동
$ git checkout -b <branch 이름>
// 브랜치 리스트
& git branch
```

#### 5. 코드 작업 후 add/commit/push

```bash
$ git add .
$ git commit -m 'massege'
$ git push origin develop
```

#### 6. Pull Request 생성

- github 저장소 상단에 `Compare & pull request` 버튼이 활성화 된다.

- 버튼을 누르고, PR 메세지를 작성하여 `Cretae pull request` 버튼을 누르면 풀 리퀘스트를 생성하게 된다.

#### 7. Merge Pull Request

- Pull Request를 받은 원본 저장소 관리자는 코드 변경 내용을 확인하고 Merge 여부를 결정한다.

- 원작자가 승인을 하면 Merge Confirm으로 원본 저장소에 변경된 사항이 반영되고, pull request의 상태는 closed로 변경된다.

- 원작자가 거절하면 Reject된다.

#### 8. Merge 이후 branch 삭제

```bash
$ git branch -d develop
```

## git & github 전체 동작 과정

<img src="git_github02.assets/whole.PNG" alt="whole" style="zoom:150%;" />