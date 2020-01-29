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
 ## Running Pytest-Flask-Playground
