
# CRM
Customer Relationship Management(CRM) is a strategy that companies use to manage interactions with customers and potential customers.

## Overview

## Description

- If a customer is not able to get immediate or relatively fast help when on your site, they may not make a purchase.
- CRM can provide deeper insights into customer behavior on and off your site,
- ADVANCED PERSONALIZATION, You can use it to personalize each customer’s experience on your website to better meet their needs.
- I have learnt how to build an user-friendly design for the website.


## Installation
Use the following command to install pip for Python 3:
  
    $ sudo apt install python3-pip


Clone the repository from Github and switch to the new directory:
  
    $ git clone https://github.com/mohammadhosseini3/CRM.git
    $ cd CRM
    
Activate the virtualenv for your project.

    $ pip install virtualenv
    $ virtualenv [name of your new virtual environment]
    $ cd [name of your new virtual environment]
    $ source bin/activate
    $ pip install -r requirements.txt

## How to Run it

First Migrate models to your database:

    $ python manage.py makemigrations
    $ python manage.py migrate
    

Then you can now run the development server:

    $ python manage.py runserver
    $ Go to [http://localhost:8000](http://localhost:8000) to see your CRM version.


## Credits
Followed Tutorial link: 

https://youtube.com/playlist?list=PLOLrQ9Pn6cazhaxNDhcOIPYXt2zZhAXKO

