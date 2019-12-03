# Bookstore based on Django
## overview
The project is to create an online bookstore which include the basic function of an online store including showing products, adding to the cart, buying the product online. Its target customers are buyers who hope to get books, especially well-chosen relaxing book online with ideal price. In fact, the project is based on the incomplete clothes store whose online address is https://github.com/lawiet019/FinalProjectForDB/invitations.

## to run the project
You should use the command ```pip install -r requirements.txt``` firstly
to install all the modules required for this project And then use the command ``` python manage.py runserver``` to start the project

## the structure of the project
```
django-ecommerce-master

├─ .gitignore           the file to determine which not git push to remote
├─ LICENSE              license of the project,use GNU
├─ README.md            the overview of the project
├─ manage.py            the entrance of the whole project
├─ requirements.txt     the module needs to be installed
├─ .env                 the setting of the project, but it does not work since it is production enviroment
├─ db.sqlite3           the database generated of the new_project_name
├─ core                 the only component folder of the project
│    ├─ __init__.py     generated automatical, to initiatize the component
│    ├─ __pycache__
│    ├─ admin.py        generated automatical, the front-end management tool provided by Django
│    ├─ apps.py         to register the component
│    ├─ forms.py        to give the form template that needs to to deliver to templates               
│    ├─ management      add some commaneds to default
│    ├─ migrations      the DDL genenrated by command makemigrates
│    ├─ models.py       define the data structure of database
│    ├─ templatetags    Custom labels and filters
│    ├─ tests.py        the test file for the component
│    ├─ urls.py         the path and its Corresponding view
│    └─ views.py        define all the view
├─ djecommerce          the project setting document
│    ├─ __init__.py     generated automatical, to initiatize the project
│    ├─ __pycache__
│    ├─ settings        the setting documents, the base.py is the common part.development.py is for development enviroment. the production.py is for production enviroment
│    ├─ urls.py         the paths for the project
│    └─ wsgi.py         the deployment project
├─ static_in_env        the static folder to put CSS,JS, image,etc.
└─ templates            the folder to put templates which will generate HTML
```
