# Research Project ManagementSystem
This is an online system which can help the user to do the following things:
1. Add research papers
2. Add research projects
3. Register researchers
4. Allow students and other people to download research papers
5. Add internship places available for the students
6. Enable students to add research problems
8. Many more

# Technology used
1. python
2. Flask
3. CSS
4. HTML5

## Installation and Set Up
Prerequisites:
* [Python 3]
* [virtualenv](https://virtualenv.pypa.io/en/stable/)

Clone the repo from GitHub:
```
git clone https://github.com/engineerkintu/Research-Project-Management-System
```

Create a virtual environment for the project and activate it:
```
virtualenv proj
source proj/bin/activate
```

Install the required packages:
```
pip install -r requirements.txt
```

## Database configuration
You will need to create a MySQL user your terminal, as well as a MySQL database. Then, grant all privileges on your database to your user, like so:

```


Note that `dt_admin` is the database user and `dt2016` is the user password. After creating the database, run migrations as follows:

* `flask db migrate`
* `flask db upgrade`

## instance/config.py file
Create a directory, `instance`, and in it create a `config.py` file. This file should contain configuration variables that should not be publicly shared, such as passwords and secret keys. The app requires you to have the following configuration
variables:
* SECRET_KEY
* SQLALCHEMY_DATABASE_URI (`'mysql://dt_admin:dt2016@localhost/dreamteam_db'`)

## Launching the Program
Set the FLASK_APP and FLASK_CONFIG variables as follows:

* `export FLASK_APP=run.py`
* `export FLASK_CONFIG=development`

You can now run the app with the following command: `flask run`

## Testing
First, create a test database and grant all privileges on your test database to your user:

```
$ mysql -u root

mysql> CREATE DATABASE dreamteam_test;

mysql> GRANT ALL PRIVILEGES ON dreamteam_test . * TO 'dt_admin'@'localhost';
```

To test, run the following command: `python tests.py`

## Built With...
* [Flask](http://flask.pocoo.org/)
