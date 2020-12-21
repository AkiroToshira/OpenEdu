# OpenEdu. How to start a project

* Clone repository
    ```
    git clone https://github.com/AkiroToshiro/OpenEdu.git 
    ``` 

* Create default project with cloned files 
* Create default virtual environment
		
* Enter path to "requirements.txt" and install dependencies
    ```
    cd /path/to/requirements.txt
    ```
    ```
    pip install -r requirements.txt
    ``` 
* Set in "settings.py" your database(Any you want).Or leave it default
    ```
   DATABASES = {
	'default': {
    'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
   ```

* Enter path to "manage.py"
    ```
    cd /path/to/manage.py
    ```
* Create migrations, to sync database
    ```
    python manage.py makemigrations
    ```
    ```
    python manage.py migrate
    ```
  (ONLY IF DEFAULT SQLITE3)
  After migrations , a database file 'mydatabase' will automatically create in folder with manage.py
* Create superuser
    ```
    python manage.py createsuperuser
    ``` 
* Enter your data in terminal for future log in project
    ```
	-Username (leave blank to use 'yournickname'):
	-Email address: (not must)
	-Password:
	-Password (again):
    ``` 
* Start project 
    ```
    python manage.py runserver
    ``` 
* Copy the link highlighted in the terminal
    ```
    Example:   Starting development server at http://127.0.0.1:8000/
    ``` 
    p.s: if you follow this url address you will enter a main page of project(website)
* Change copied url address to
    ```
    Example:  Starting development server at http://127.0.0.1:8000/admin
    ``` 
* Enter User and Password ,created earlier
* Using 'Django Administration' fill database
* Enjoy using
   
    
    
    
    
    
    
