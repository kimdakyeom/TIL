# 헤로쿠와 s3 연동
> AWS S3?
>
> Simple Storage Service의 약자이며 인터넷 스토리지 서비스

## IAM
> AWS 서비스 접근을 위한 사용자를 추가한다.

### 사용자 추가
- AWS 좌측 상단 검색창에 IAM 을 입력해서 IAM 페이지 이동 - 사용자 메뉴 클릭
- 사용자 추가 버튼을 클릭해서 사용자 추가를 시작한다.
#### MFA?
> AWS의 이중보안 시스템

### 사용자 세부 정보 설정
- 사용자 이름을 작성 / AWS 자격 증명 유형 - 액세스 키 선택
### 권한 설정
- 기존 정책 직접 연결 - `AmazonS3FullAccess` 검색 후 선택

### 태그 추가(선택 사항)
### 검토
- 사용자 만들기 클릭
### 액세스 정보(.csv) 다운로드

## S3
### 버킷 추가
- S3 검색 - 페이지 진입 - 버킷 만들기 클릭

### 버킷 설정
- 버킷 이름 작성 
- AWS 리전 선택 
- 모든 퍼블릭 액세스 차단 해제 - 해제 확인) 
- 버킷 생성
### 버킷 정책 생성
- 생성한 버킷 클릭 - 권한 탭 이동
- 버킷 정책 편집 - 정책 생성기

```
*Select Type of Policy - S3 Bucket Policy
Effect - Allow
Principal - *
Actions 
- DeleteObject
- GetObject
- GetObjectAcl
- PutObject
- PutObjectAcl
Amazon Resource Name
- arn:aws:s3:::[버킷이름]/*

- 예시) arn:aws:s3:::kdt-django-s3/*
```

## Django S3
### 패키지 설치
```bash
pip install python-dotenv
pip install django-storages
pip install boto3
pip freeze > requirements.txt
```
### settings.py 설정
```python
BASE_DIR(manage.py가 있는 폴더)에 .env 파일 생성 후 아래 값 작성

AWS_ACCESS_KEY_ID = [IAM 사용자 Access key ID]
AWS_SECRET_ACCESS_KEY = [IAM 사용자 Secret access key]
AWS_STORAGE_BUCKET_NAME = [S3 버킷 이름]


# 예시
AWS_ACCESS_KEY_ID = 21390ujskladjlask
AWS_SECRET_ACCESS_KEY = 21oi3uqwjd09asoi
AWS_STORAGE_BUCKET_NAME = kdt-django-s3
```
```python
# 최상단에 아래 3줄을 추가.
from dotenv import load_dotenv
import os
load_dotenv() # .env 파일에서 환경 변수를 불러옵니다.


INSTALLED_APPS = [
	"storages", # storages 추가
	# ... 이하 생략
]

"""
기존 MEDIA 설정 주석
MEDIA_ROOT = ...
MEDIA_URL = ...
"""

# 아래 코드 추가
DEFAULT_FILE_STORAGE = "storages.backends.s3boto3.S3Boto3Storage"

AWS_ACCESS_KEY_ID = os.getenv("AWS_ACCESS_KEY_ID")
AWS_SECRET_ACCESS_KEY = os.getenv("AWS_SECRET_ACCESS_KEY")
AWS_STORAGE_BUCKET_NAME = os.getenv("AWS_STORAGE_BUCKET_NAME")

AWS_REGION = "ap-northeast-2"
AWS_S3_CUSTOM_DOMAIN = "%s.s3.%s.amazonaws.com" % (
    AWS_STORAGE_BUCKET_NAME,
    AWS_REGION,
)
```
### 테스트
- 로컬 서버에서 미디어 파일이 정상적으로 업로드 및 조회가 되는지 확인
### 개발 & 배포 환경 분리
- 개발 환경에서는 기존 설정(MEDIA_URL / MEDIA_ROOT)이 작동하도록
배포 환경에서는 S3 설정이 작동하도록 설정을 분리
```
.env에 DEBUG 값 추가

DEBUG = True
```
```python
# settings.py

"""
기타 환경에 따라 설정 분리가 필요한 경우 코드를 분리해서 추가로 작성합니다. 
"""

DEBUG = os.getenv("DEBUG") == "True"

if DEBUG: 
    MEDIA_URL = "/media/"
    MEDIA_ROOT = BASE_DIR / "media"

else:   
    DEFAULT_FILE_STORAGE = "storages.backends.s3boto3.S3Boto3Storage"

    AWS_ACCESS_KEY_ID = os.getenv("AWS_ACCESS_KEY_ID")
    AWS_SECRET_ACCESS_KEY = os.getenv("AWS_SECRET_ACCESS_KEY")
    AWS_STORAGE_BUCKET_NAME = os.getenv("AWS_STORAGE_BUCKET_NAME")

    AWS_REGION = "ap-northeast-2"
    AWS_S3_CUSTOM_DOMAIN = "%s.s3.%s.amazonaws.com" % (
        AWS_STORAGE_BUCKET_NAME,
        AWS_REGION,
    )
```
### 헤로쿠 배포 시 환경변수 설정
- 헤로쿠로 배포할 경우 S3에 대한 환경 변수를 추가로 설정
  - `AWS_ACCESS_KEY_ID`, `AWS_SECRET_ACCESS_KEY`, `AWS_STORAGE_BUCKET_NAME`

### 배포 후 이미지 업로드 테스트
- 문제 없이 이미지 업로드 및 출력이 되는지 확인

# DB 데이터 이동
> 로컬에서 구축한 데이터베이스의 데이터를 배포 후 데이터베이스로 복사하는 방법

## [로컬 환경] 데이터 추출
- 로컬 데이터베이스(sqlite3)에서 특정 앱의 데이터를 추출
- 데이터가 저장 된 파일이름.json 파일이 생성

```bash
python -Xutf8 manage.py dumpdata 앱이름 > 파일이름.json

# 예시
python -Xutf8 manage.py dumpdata articles > articles.json
```

## 서비스 배포
- `파일이름.json` 을 포함하여 서비스를 재배포

## [배포 환경] 데이터 저장
- 추출한 데이터를 배포 환경의 데이터베이스에 저장
```bash
# 헤로쿠 배포를 한 경우, 로컬 환경 터미널에서 입력
heroku run python manage.py loaddata 파일이름.json


# 배포 서버 터미널에서 직접 입력할 때
python manage.py loaddata 파일이름.json
```

## 주의 사항
- 배포 환경에서 데이터베이스를 마이그레이트(migrate)를 한 상태여야한다.
- 배포 환경에서 데이터 추가를 하지 않은 상황이어야 한다.(동일 pk 오류 발생 가능)
- 데이터 추가를 한 적이 있다면 아래 명령어로 데이터베이스를 리셋
  - 주의, 데이터가 모두 삭제된다.
  ```bash
  heroku run python manage.py flush
  ```