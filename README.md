
# Manual Cronjob

> One paragraph statement about the project.

![screenshot](./cronjob.jpg)

Additional description about the project and its features.

## Built With

- Python
- Django
- Bootstrap



## Getting Started

****
**Cronjob enables you to automate API calls to your preferred endpoints at specified intervals. In this project, we have created a Manual Cronjob web app which enables you to run checks on your specified endpoints manual and log the response from the url.**


To get a local copy up and running follow these simple example steps.

### Prerequisite
Ensure you have a virtual environment activated and you are running on Python 3 or later.

### Install

1. Clone Repository

    ```sh
    git clone https://github.com/helixpy/cronjob.git
    ```
2. Install packages

    ```sh
    pip install -r requirement.txt
    ```
3. Migrations: Navigate to project folder, and run;
    ```sh
    python manage.py makemigrations
    ```
    and completion of making migrations;
    ```sh
    python manage.py migrate
    ```
4. Create superuser: While in project folder, run;
    ```sh
    python manage.py createsuperuser
    ```
    follow the prompt and enter a username, email and password.
    On completion, run;
    ```sh
    python manage.py runserver
    ```
    navigate the locahostaddress/admin

### Usage
Navigate to the registration page, enter your credentials and proceed to login page. Once logged in, commence your API calls and tests. <br>
This project is suitable for carrying out activeness test on servers as well as knowing if the error state of a particular server. <br> Users
can also clone this repository for practise purposes.

## Authors

👤 **Unubi Opaluwa**

- GitHub: [@githubhandle](https://github.com/HelixPy/)
- Twitter: [@twitterhandle](https://twitter.com/unubi_)
- LinkedIn: [LinkedIn](https://linkedin.com/in/unubi-opaluwa)

