# Pytest-Flask-Playground

"Pytest (Flask-playground)"" is an example of what a conftest.py configuration file might look like for our Flask-playground project. It also contains a test file (test_config.py) that uses it.
You can download [Flask-playground](https://github.com/pn141/Flask-playground) and the corresponding Pytest files by following the installation instructions below. 

## Installation instructions:
**Note:** This project requires that "Flask-playground" is first installed. Use the link above to download and install before proceeding with the steps below.

   1. Clone or download "Pytest-Flask-Playground" in a temporary location:

```git clone https://github.com/pn141/Pytest-Flask-Playground```

   2. From the "Pytest-Flask-Playground" directory copy "conftest.py" and "test_config.py" to the root of your "Flask-playground" directory.
   
   3. Edit file "test_config", change the following line with an appropriate entry and save the file:
   ```
   # The entry needs to be changed to the path of the
   # flask_playground folder on your machine
   db_path = ("sqlite:///C:\\path\\to_folder\\"
           "flask_playground\\data-test.sqlite")
   ```
   **Note** There is no need to install Pytest as it is already part of the requirements for Flask_playground and has already been installed.
   
 ## Running Pytest-Flask-Playground
Running "Pytest-Flask-Playground" requires that "Flask-playground" is started in "testing" mode. You can either use [this script](https://github.com/pn141/Changing-environment) or follow the instructions below:

   1. Make sure Flask-playground is stopped then locate file ".env" at the root of folder "Flask-playground"
   
   2. Edit the file, locate entry ```FLASK_ENV = 'development'``` and replace it with ```FLASK_ENV = 'testing'```. Save the file and close it.
   
   3. In the same file, locate the following entry and make sure it matches the entry in "Installation instructions" step 3 above.
   ```
   TEST_DATABASE_URL = 'sqlite:///C:\\path\\to\\flask-playground\\data-test.sqlite'
   ```
   
   3. In the same location, edit file "flask-playground.py". Locate entry ```app = create_app('development')``` and replace it with ```app = create_app('testing')```. Save the file and close it.
   
   4. Start "flask-playground" using command "flask run". The application should now indicate in the shell that it is running in 'testing' mode.
   ```
   (venv) C:\projects\project - github\Flask-playground>flask run
 * Serving Flask app "flask-playground.py"
 * Environment: testing
 * Debug mode: off
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
   ```
   5. In order to run pytest, you need to open a command prompt at the location of your "Flask-directory" folder and activate your virtual environment.
   Linux venv activate: ```source venv/bin/activate```
   Windows venv activate: ```.\venv\Scripts\activate.bat```
   
   6. To run the tests use ```pytest test_config.py```
   The result should be similar to this:
   ```
   (venv) C:\projects\project - github\Flask_playground>pytest test_config.py
================================================= test session starts =================================================
platform win32 -- Python 3.7.1, pytest-5.2.1, py-1.8.0, pluggy-0.13.0
rootdir: C:\projects\project - github\Flask_playground
plugins: cov-2.8.1, flask-0.15.0, flask-sqlalchemy-1.0.2, mock-1.12.0
collected 20 items

test_config.py ....................                                                                              [100%]

================================================= 20 passed in 0.20s ==================================================
   ```
