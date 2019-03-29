# subject_rate

Web application in python for rating univeristy courses.

[Live Version](https://knu-subject-rate.herokuapp.com/
)

## Getting Started


These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Prerequisites

everything from Pipfile

### Installing

Download source code

```
git clone https://github.com/mixnix/subject_rate
```

Go into subject_rate directory and create new virtual environment

```
pipenv shell
```

Install dependencies

```
pipenv install
```

Open .env.template and modify values to it to your own. Enter your secret key and your username and password to sendgrid or mailgun or other mail service.

Rename .env.template to .env

Run server

```
py manage.py runserver
```

## Authors

* **Michał Nielipiński** 

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details