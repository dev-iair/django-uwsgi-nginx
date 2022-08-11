## 커스텀 어드민
web/web 폴더의 admin, form, models 참고
## 도커 사용
docker-compose 사용하여 nginx - uwsgi - django 연동 배포 
## 배포 전
python manage.py collectstatic 아래 admin 폴더를 static 폴더로 복사
settings.py 의 INSTALLED_APPS 안에 서버 아이피 입력
## 테스트
python manage.py runserver
uwsgi --http 0.0.0.0:8000 --home {virtualenv경로} --chdir d{jango프로젝트 경로} -w {프로젝트명}.wsgi
## 앱 만들기
python manage.py startapp {앱이름}
settings.py 의 INSTALLED_APPS 안에 '{앱이름}' 추가