# DjangoBlog
Take home test SmallCloud Technologies
********
python -V    (check the python version)
pip freeze   (check what it is installed, and particularily virtualenv)


pip install virtualenv   (install virtual environment)


virtualenv .   (tell to create the virtual env in the current directory)

./Scripts/activate   (run the virtual env) we can turn off with deactivate

pip freeze will show that nothing is installed in the new virtual env

pip install django  (will install django, we can install particular version pip install django==2.2)

pip freeze (will show the version of django installed)

mkdir src (create the app source folder)

django-admin.py startproject blog_app .  (create the blog-app project)

inside that directory we will have manage.py (important file to execute django commands)

*********
python manage.py runserver   (run the server)

python manage.py migrate (install the unapplied migrations and database setup, can access to admin)

python manage.py createsuperuser   (create superuser to access the admin panel)

********
Django is MVT pattern 

python manage.py startapp blog  (create an app)

// has to be done everytime we create or edit model classes
python manage.py makemigrations   (after creating model to create in DB the table)
python manage.py migrate    (need to be also done after model creation)

python manage.py shell  (we will have the shell of django)

*************
from blog.models import BlogPost
obj = BlogPost.objects.get(title='this is my title)


To have image and use in model ImageField we need to install Pillow
pip install pillow

*****************Views/Functionality asked to be implemented
List view of posts (this should be the home page)     DONE
Detail view of each post      DONE
Create a post with a simple html form (title, description, author, created date)   DONE
Editing a post    DONE
Posts should persist using a database to store them (use the default database,
SQLite)    DONE
Allow toggle draft and published status of blog posts when editing   DONE

Post Model has
- Title
- Image
- Slug
- Content
- Publish date

The User is linked through the Django User.

*****************FUNCTIONALITY IMPLEMENTED
- On Menu we have
    - Home : We can see all the posts             
    - Blog : ONLY USER AUTHENTICATED AND STAFF We can see the blog owned by the user
    - Post : ONLY USER AUTHENTICATED AND STAFF can see this menu item and post a new post

- Edit Post : ONLY USER AUTHENTICATED AND STAFF
- Cancel Post : ONLY USER AUTHENTICATED AND STAFF
- Search : it searches the title and the content for only published posts
- Visitor can see only published posts
- Post owner can convert draft posts to published post
- Draft posts have warning border.

**************FUNCTIONALITY NOT IMPLEMENTED
- Add Comment to the post (have to create a comment model and add foreignKey in BlogPost model)
- Categorize the posts    (have to create a category model and add foreignKey in BlogPost model)
