# Medical Appointment
This is a REST API that allows patients and doctors book appointments and manage availability respectively.


[![Medical Appointment](https://github.com/Resa-Obamwonyi/med_appointment/workflows/Med%20Appointment/badge.svg)](https://github.com/Resa-Obamwonyi/med_appointment/actions)

## Technologies

* [Python 3.9](https://python.org) : Base programming language for development
* [Bash Scripting](https://www.codecademy.com/learn/learn-the-command-line/modules/bash-scripting) : Create convenient script for easy development experience
* [PostgreSQL](https://www.postgresql.org/) : Application relational databases for development, staging and production environments
* [Django Framework](https://www.djangoproject.com/) : Development framework used for the application
* [Django Rest Framework](https://www.django-rest-framework.org/) : Provides API development tools for easy API development
* [Github Actions](https://docs.github.com/en/free-pro-team@latest/actions) : Continuous Integration and Deployment
* [Docker Engine and Docker Compose](https://www.docker.com/) : Containerization of the application and services orchestration


### How to use and Test this application hosted on Heroku
- Follow the documentation at: https://documenter.getpostman.com/view/11737108/TW6wJTvg
- Test the login endpoints with either a doctor or patient credential,

```
Doctor 1:
email: mudia@gmail.com
password: mudiareal

Doctor 2:
email: sandy@gmail.com
password: sandyreal

Patient 1:
email: markessien@gmail.com 
password: patientonereal

Patient 2:
email: yinka@gmail.com
password: patienttworeal
```
- Test the other endpoints, as directed in the documentation, using the credentials above.

### How to Use and Test this Application on your computer
- Clone the Repository
- Create a .env file and use the supplied env variables.
- Run `docker-compose up --build`
- run migrations `docker-compose exec web python manage.py makemigrations`
- run `docker-compose exec web python manage.py migrate`
- run tests `docker-compose exec web python manage.py test`
- Using `docker-compose exec web python manage.py shell`, enter into the shell and manually add a doctor and patient.
- Test Login with doctor or patient email and password
- Hit the /calender endpoint to set available days and time as a doctor.
- Hit the /book-appointment endpoint as a Patient to book an appointment with a specific doctor.

### Link to API Documentation
https://documenter.getpostman.com/view/11737108/TW6wJTvg

### Link to Heroku
https://cura-med-appointment.herokuapp.com/api

### Comments
send an email to theresaobamwonyi@gmail.com if there are any questions.