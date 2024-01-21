## Python Django Web Framework - Full Course for Beginners

[视频教程网址](https://www.youtube.com/watch?v=F5mRW0jo-U4&t=38s)

[django官网](https://www.djangoproject.com/)

[教程示例项目](https://github.com/codingforentrepreneurs/Try-Django)

### 安装

### 为Django设置虚拟环境
`virtualenv` 

```
$ virtualenv -p python3 .
Running virtualenv with interpreter /usr/local/bin/python3
Using base prefix '/usr/local/Cellar/python/3.7.0/Frameworks/Python.framework/Versions/3.7'
/usr/local/lib/python3.7/site-packages/virtualenv.py:1041: DeprecationWarning: the imp module is deprecated in favour of importlib; see the module's documentation for alternative uses
  import imp
New python executable in /Users/andyron/myfield/PythonDev/trydjango/bin/python3.7
Also creating executable in /Users/andyron/myfield/PythonDev/trydjango/bin/python
Installing setuptools, pip, wheel...done.
$ source bin/activate
(trydjango) $ pip install django==2.2.4

```

`source bin/activate` 进入虚拟环境

`deactivate`  命令结束虚拟环境

```shell
$ pip3 freeze
six==1.12.0
$ source bin/activate
(trydjango) $ pip3 freeze
Django==2.2.4
pytz==2019.2
sqlparse==0.3.0
```



### Create a Blank Django Project

`django-admin`

```shell
$ mkdir src
$ cd src
$ django-admin startproject trydjango .
$ ls
manage.py trydjango 
$ python manage.py runserver
```

![](images/image-20190820185402844.png)





### Setup Your Code Text Editor



### Setting





settings.py**

![](images/image-20190820185110776.png)



`$ python manage.py migrate`



### Built-In Components

```shell
$ pwd
PythonDev/trydjango/src
$ python manage.py createsuperuser
```



### Your First App Component

```shell
(trydjango) $ python manage.py startapp products
(trydjango) $ python manage.py startapp blog
(trydjango) $ python manage.py startapp profiles
(trydjango) $ python manage.py startapp cart
```

![](images/image-20190820193448011.png)

要删除Component，直接删除目录就行了



在setting.py文件的`INSTALLED_APPS`中添加组件名称



`$ python manage.py createsuperuser`



`$ python manage.py makemigrations`

```shell
$ python manage.py migrate
Operations to perform:
  Apply all migrations: admin, auth, contenttypes, products, sessions
Running migrations:
  Applying products.0002_product_summary... OK
```



### Create Product Objects in the Python Shell

```shell
$ python manage.py shell
Python 3.7.0 (default, Sep 16 2018, 19:30:42)
[Clang 9.1.0 (clang-902.0.39.2)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
(InteractiveConsole)
>>> from products.models import Product
>>> Product.objects.all()
<QuerySet [<Product: Product object (1)>, <Product: Product object (2)>]>
>>> Product.objects.create(title='New product 3', description='sweet', price='123', summary="awesome")
<Product: Product object (3)>
>>> Product.objects.create(title='New product 4', description='sweet', price='123', summary="awesome")
<Product: Product object (4)>
```



### New Model Fields

删除 `products/migrations` 中的`__pycache`和000开头的文件，以及数据库文件db.sqlit3

[Field types](https://docs.djangoproject.com/en/2.2/ref/models/fields/#field-types)



`$ python manage.py makemigrations`

`$ python manage.py migrate`

`$ python manage.py createsuperuser`



### Change a Model

`$ python manage.py makemigrations`

`$ python manage.py migrate`



### Default Homepage to Custom Homepage

`urls.py`

```python
from django.contrib import admin
from django.urls import path

from pages.views import home_view

urlpatterns = [
	path('', home_view, name='home'),
    path('admin/', admin.site.urls),
]

```



### URL Routing and Requests

`pages/views.py`

```python
def home_view(request, *args, **kwargs):
	return HttpResponse("<h1>Hello World</h1>")   

def contact_view(request, *args, **kwargs):
	return HttpResponse("<h1>Contact View</h1>")

def about_view(request, *args, **kwargs):
	return HttpResponse("<h1>About View</h1>")

def social_view(request, *args, **kwargs):
	return HttpResponse("<h1>Social View</h1>")
```

`urls.py`

```python
from pages.views import home_view, contact_view, about_view, social_view

urlpatterns = [
	path('', home_view, name='home'),
	path('home/', home_view, name='home'),
	path('contact/', contact_view),
	path('about/', about_view),
	path('social/', social_view),
  path('admin/', admin.site.urls),
]
```

### Django Templates



### Django Templating Engine Basics

`base.html`

```html
{% block content %}
		replace me
{% endblock content %}
```

`about.html`

```html
{% extends 'base.html' %}

{% block content %}
	<h1>About View</h1>
	This is templates
{% endblock content %}
```



### Include Template Tag

`	{% include 'navbar.html' %}`



### Rendering Context in a Template

`views.py`

```python
def about_view(request, *args, **kwargs):
	my_context = { 
		'my_text': 'This is about us',
		'my_number': 123456
	}
	return render(request, "about.html", my_context)
```

`about.html`

```html
	<p>
		{{ my_text }}, {{ my_number }}
	</p>	
```



### For Loop in a Template

```html
<ul>
{% for my_sub_item in my_list %}
	<li>{{ forloop.counter }} - {{ my_sub_item }}</li>
{% endfor %}
</ul>
```

### Using Conditions in a Template

```html
<ul>
{% for my_sub_item in my_list %}
	{% if my_sub_item == 33 %}
		<li>{{ forloop.counter }} - {{ my_sub_item|add:3 }}</li>
	{% else if my_sub_item == 24 %}
		<li> This is Kobe Num</li>
	{% else %}
		<li>{{ forloop.counter }} - {{ my_sub_item }}</li>
	{% endif %}
	
{% endfor %}
</ul>
```



### Template Tags and Filters

[Built-in template tags and filters](https://docs.djangoproject.com/en/2.2/ref/templates/builtins/)



### Render Data from the Database with a Model



### How Django Templates Load with Apps



### Django Model Forms

