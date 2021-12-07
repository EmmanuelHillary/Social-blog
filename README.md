# Social-blog
a social blog with CRUD functionalities and authentication system 

## Setup

The first thing to do is to clone the repository:

```sh
$ git clone https://github.com/EmmanuelHillary/Social-blog.git
$ cd Social-blog
```

Create a virtual environment to install dependencies in and activate it:

```sh
$ py -3 -m venv env
$ env\Scripts\activate
```
Then install the dependencies:

```sh
(env)$ pip install -r requirements.txt
```
Note the `(env)` in front of the prompt. This indicates that this terminal
session operates in a virtual environment 

if you run into the following error below:

```sh
error: Microsoft Visual C++ 14.0 is required. Get it with "Microsoft Visual C++ Build Tools": http://landinghub.visualstudio.com/visual-cpp-build-tools
```
1. Go to: [https://www.visualstudio.com/downloads/#build-tools-for-visual-studio-2017](https://www.visualstudio.com/downloads/#build-tools-for-visual-studio-2017).
2. Select the free download under Visual Studio Communitym
     - This will download the installer
     - Run the installer
3. Now the most important step is to select what you need under the workload tab:
     - Under Windows there are 3 choices. ONLY check "Desktop development with C++"
     - Under Web & Cloud there are 7 choices. ONLY check Python development (I believe this is optional but I still did it).
4.  Now go to your cmd and install the package:
```sh
(env)$ pip3 install misaka
```
![This is an image](https://i.stack.imgur.com/8gcXo.jpg)

**Note** that if you already installed Visual Studio then when you run the installer, you can modify it (click the modify button under Visual Studio Community 2017) and do steps 3 and

![This is an image](https://i.stack.imgur.com/ApebY.jpg)

Once `pip` has finished downloading the dependencies:

```sh
(env)$ cd project
```
make make migrations and push the migrations

```sh
(env)$ python manage.py makemigrations
(env)$ python manage.py migrate

```

create an admin user

```sh
(env)$ python manage.py createsuperuser
```

then run the server

```sh
(env)$ python manage.py runserver
```
And navigate to `http://127.0.0.1:8000/`

**Homepage**
![Alt](https://github.com/EmmanuelHillary/Social-blog/blob/main/images/homepage.png)

**Registration Page**
![Alt](https://github.com/EmmanuelHillary/Social-blog/blob/main/images/sign%20up.png)

**Login Page**
![Alt](https://github.com/EmmanuelHillary/Social-blog/blob/main/images/login.png)

**User's posts**
![Alt](https://github.com/EmmanuelHillary/Social-blog/blob/main/images/users's%20posts.png)









