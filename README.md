# NEIGHBOURHOOD

This is an application that allows users in an area to interact with other people who also live in the same area. The users can look up businesses in that area and also create posts that let the other neighbours know of the happenings in the nieghbourhood.

# Setup/Installation Requirements

Ensure you have Python3.8 installed.

Clone the Neighbourhoods directory.

Create your own virtual environment and activate it using these respective commands python3.8 -m venv --without-pip virtual and source virtual/bin/activate

Install all the necessary dependencies necessary for running the application using this command pip install -r requirements.txt

Open the terminal and run this command psql You can then create a database by running this command CREATE DATABASE hood

Run migrations using these respective commmands python3.8 manage.py makemigrations projects then python3.8 manage.py migrate

Run the app using this command python3.8 manage.py runserver on the terminal.You can then open the app on your browser.


