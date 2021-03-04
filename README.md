# PierrorZS AnimeService

[![Build Status](https://travis-ci.com/PierrotZS/pierrotweb.svg?branch=master)](https://travis-ci.com/PierrotZS/pierrotweb)

##Website Link
- https://pierrotweb.herokuapp.com

## Team Members
| Name       |      GitHub ID     |
|----------|:-------------:|
| PierrotZS        |      [PierrotZS](https://github.com/PierrotZS)      |
| keyboard2543        |      [keyboard2543](https://github.com/keyboard2543)      |
| james31366 |      [james31366](https://github.com/james31366)      |

## Quick start
## Requirements
* Language: Python 3.8 or more!
* Back-end Framework: Django
    * Taggit 1.3.0
  
### Steps for starting application
1. Clone this project and change directory to be `pierrotweb`.
       
        $ git clone https://github.com/PierrotZS/pierrotweb.git
        $ cd pierrotweb/
    
2. Update python pip to the current version

        $ python -m pip install --upgrade pip
   
3. Install virtualenv

        $ pip install virtualenv
4. Create virtual environment directory using this command.

        $ virtualenv py1

5. Activate virtual environment due to your os.

   For Window:
    
        $ venv\Scripts\activate
        
    For Mac/Linux:
    
        $ source venv/bin/activate

6. Install modules in [requirements.txt](requirements.txt) using 
  
        $ pip install -r requirements.txt

7. Use mysite/sample.env as a template, then create/edit your own
.env file and set their values.

       DEBUG=True
       TEMPLATE_DEBUG=True
       SECRET_KEY=Your-Secret-Key

        
   * You shouldn't be able to login with google
    but you can login to ku-hub by create super user
     following the instruction in Note below

8. Create initial migration, then apply the change 
       
       $ python manage.py makemigrations
       $ python manage.py migrate
       
9. Run this command to run the server

       $ python manage.py runserver
       
Note!:

* When finished running server, deactivate virtual environment using this command

    ```$ deactivate```
    
* To create super user

    ```$ python manage.py createsuperuser```