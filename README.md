# employee-mgmt

create virtual environment -> python -m venv env

then activate by running this cmd venv\Scripts\activate

dependency installation:
------------------------
pip install -r requirements.txt

to check everything in proper condition run:
--------------------------------------------

python manage.py migrate

python manage.py makemigrations

run application:
-----------------

python manage.py runserver

to test api endpoint:
---------------------
python manage.py test home

to test api endpoint in postman:
-------------------------------
import home/tests/employee-mgmt.postman_collection.json file in postman to look into CRUD endpoints

![get](https://user-images.githubusercontent.com/74130632/227716009-13a64f5b-47b9-417c-87c0-e85f3cb13755.png)
