#   What's on your hackathon wish list?

The hackathon managers at Devpost are trying something new! We’re looking to you for ideas, designs, and resources that will help hackers in future hackathons. What do you think would make participating in a hackathon easier and more fun?


##  WHAT TO DO
Submit feedback about hackathons! As a bonus, submit an idea for a new tool or resource to help participants of hackathons. Projects do not have to be working applications! 


# Setup

The first thing to do is to clone the repository:

```sh
$ git clone https://github.com/izudada/devpost_blog_api.git
```

Create a virtual environment to install dependencies and activate it use the link below first to install virtualenv:

[Virtualenv](https://izudada.medium.com/how-to-create-a-virtual-environment-in-python-a47f401506db)

Then install the dependencies:

```sh
$ pip install -r requirements.txt
```

Use migrate command to effect database model:

```sh
$ python manage.py makemigrations
$ python manage.py migrate
```

Start the server with:
```sh
$ python manage.py runserver
```
And navigate to `http://127.0.0.1:8000/`


##  Documentation

Postman documentation can be found [Here](https://documenter.getpostman.com/view/20677030/2s93CNMsnp)


### Import Postman Collection
You can import the postman collection ![Devpost_Blog_API Postman Collection](Devpost_Blog_API.postman_collection.json)
to test the endpoints locally.


##  Test

To run all available tests use:

```sh
$ python manage.py test
```
OR run tests for account app:
```sh
$ python manage.py test account
```
OR run tests for blog app:
```sh
$ python manage.py test blog
```

### Useful resources

- [Medium](https://alicecampkin.medium.com/how-to-set-up-environment-variables-in-django-f3c4db78c55f) - How to use environmental values
- [The Dumbfounds](https://www.youtube.com/watch?v=qwypH3YvMKc&t=8s) - Django Testing Tutorial
- [How to Create a Virtual Environment in Python](https://izudada.medium.com/how-to-create-a-virtual-environment-in-python-a47f401506db)
