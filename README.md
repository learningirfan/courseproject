
# Final Project for ComIT Python Course


## Project Summary:


A web app written in Python using Django framework to input/record, track/organize, and view/analyze everyday expenses.
User will be able to;
* input expense related particulars i.e., date, amount, type etc. 
* edit and delete data.
* view data in tabular form.
* sort data.

## Method:
* MySQL as backend database
* Modules written using Python
* HTML/CSS frontend

### Future Updates
* select data from data ranges, additional sorting capabilities.
* analysing data using numpy/pandas librairies.
* view data in graphical form.
* ability to add multiple users.


### Usage Instructions
* clone repository or download the zip file
* open the project folder and start virtual envrionment by 'pipenv shell'.
* use 'pip freeze' to see currently installed packages instide the virtual environment
* you might have to install Django and MySQL client.
* apply migrations through 'python manage.py makemigrations' and and 'python manage.py migrate'.
* run through the debugger or through 'python manage.py runserver 0.0.0:8000'
