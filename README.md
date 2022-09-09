# bannerapi


Technologies and Pratices used in this project

Docker
Python Django
Postgresql - Psytcopg2 libraray
TDD - Test driven development using django default test framework
flake8 for linting
Swagger - Drf_spectacular package


Access URLS
#######################

Admin URL - http://127.0.0.1:8000/admin/

Username - shiyamindia@gmail.com
Password - Qazwsx@123

API Doucmentation URL
#########################

http://127.0.0.1:8000/api/docs


Required Commands
############################
docker-compose build
docker-compose up
docker-compose down
docker-compose run --rm app sh -c "python manage.py test"  ===> Unit Testing
docker-compose run --rm app sh -c "python manage.py makemigrations"
docker-compose run --rm app sh -c "python manage.py migrate"
