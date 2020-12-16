# OpenEdu. How to start a project

* Клонувати репозиторій за посиланням
    ```
    git clone https://github.com/AkiroToshiro/OpenEdu.git 
    ``` 

* Cтворити стандартний проект в IDE з зклонованими файлами

* Створити віртуальне середовище , під'єднати до проекту
		
* Вказати в терміналі шлях до папки з файлом requirements.txt
    ```
    cd /шлях/до/папки/з/файлом/requirements.txt
    ```
* Інсталювати залежності
    ```
    pip install -r requirements.txt
    ``` 
* Замінити у файлі settings.py частину коду, а саме на
    ```
   DATABASES = {
'default': {
    'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
    ``` 

* Зкомпілювати файл settings.py

* Вказати в терміналі шлях до папки з файлом manage.py 
		```
    cd /шлях/до/папки/з/файлом/manage.py
    ```
* Створити міграції,щоб синхронізувати базу даних: 
    ```
    python manage.py makemigrations
    ```
    ```
    python manage.py migrate
    ```
   Після здійснених міграцій в папці з файлом manage.py автоматично створиться база даних 'mydatabase'
* Створити суперкористувача:
    ```
    python manage.py createsuperuser
    ``` 
* В терміналі заповнити усі поля для подальшого входу в проект на сайті:
    ```
    -Username (leave blank to use 'yournickname'):
	  -Email address: (необов'язково)
	  -Password:
	  -Password (again):
    ``` 
* Запустити проект: 
    ```
    python manage.py runserver
    ``` 
* Перейти за посиланням ,яке висвітлилося в терміналі 
    ```
    Example: Starting development server at http://127.0.0.1:8000/
    ``` 
* Вказати User'а та Password , які ви вказали при створенні суперкористувача.
   
    
    
    
    
    
    
