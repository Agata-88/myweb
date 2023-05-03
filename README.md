# myweb

## What is this program?

This is a website built using django workframe as one of the capstone project for my Software Enginering bootcamp.Site uses databse driven component.

## Table of Contents

- [Are there any prerequisites?](#are-there-any-prerequisites?)
- [How can this program be run?](#how-can-this-program-be-run?)
- [What does this program do specifically?](#what-does-this-program-do-specifically?)
- [Credits](#credits)
- [Comments](#comments)

## Are there any prerequisites?

This program uses Python verion 3.7.
All requirements are listed in requirements.txt file.

## How can this program be run?
All you need to do is to copy this repository with all its files and run it on your machine.

## How can you build this app in virtual environment:
# Starting new project:
In command line type:
1. > python -m pip install pip
2. > pip install virtualenv
3. > mkvirtualenv my_django
4. >pip install django
5. >django-admin startproject <projectname> - this will start your project and create new directory with several subfolders.
6. >python manage.py runserver - this command will start your project server.
7.  Go to http://127.0.0.1:8000/ via your web browser and you will see "Welcome to Django" page which confirms that your installation was sucessfull.

#Starting new app
1. >python manage.py startapp <appname> - this command created additional directory in your initial project directory. 

2. Go to settings.py file and add name of your application in INSTALLED_APPS. At this poing it should look like this:

![image](https://user-images.githubusercontent.com/118485184/236036168-cc3e087f-429f-42c6-8393-8ae46f566cbe.png)

3. Open urls.py file and update it as per below:

![image](https://user-images.githubusercontent.com/118485184/236036557-a9794e1e-0b6d-4631-8c88-e860d029128b.png)

4. Go to your new app directory and create new file called urls.py. Paste below code into this file:

![image](https://user-images.githubusercontent.com/118485184/236037242-468f909c-36a0-414c-a53a-0ad6c1beeed7.png)

5. Go to views.py in your app directory and define index function as per below

![image](https://user-images.githubusercontent.com/118485184/236038588-25159b3b-5233-4b34-9ffc-d41c881dc062.png)

6. Import HttpsResponse by pasting below code to the top of your your views.py file.

![image](https://user-images.githubusercontent.com/118485184/236038911-48b31cd1-6786-488e-aa7d-d874e898182d.png)

7. >python manage.py runserver - this command will start development server

8. Go to http://127.0.0.1:8000/ - you should be able to see "Hello World" printed.

# Rendering HTML
1. Inside your app directory create new folder called templates. This is where all html files for this app will be stored


## What are the features of this website?
Website allows user to view content and move between few html functions. User is abale to login into the website shop to see its content. Login details are authenticated.

## Login authentication
Program uses login authentication to allow user to access shop.

![login](https://user-images.githubusercontent.com/118485184/236028132-e7f3dc55-b326-4bff-99fb-7d6ad4d6ab09.gif)

Authentication is managed by django administration where user names are stored in the database - this is a basis for authentication.

![image](https://user-images.githubusercontent.com/118485184/236030050-84c4f053-8ddb-47de-b8be-2931139ac419.png)



## Comments:
Please note that registration function is not yet working and this is the next step in this project.
