# Pytest-Flask-Playground

#fixtures
Pytest is a mature Python testing framework. One of the cool things about Pytest is that you can create "fixtures" for setup and teardown functions and use them in your unit test activities. A simple example will help to clarify those different terms.

Let's say I have an application with functionality to authenticate users working as follow:
  1- Users register with the application by providing a valid email address as well as a username and password of their choice. The combination of username/password will be used to login to the application once the registration process is complete.
  2- The application stores users information in its database and sends a confirmation email as extra security to confirm users identity. The registration process  is complete once users have performed the actions listed in the confirmation email.

In order to test this functionality, we would need to setup a database connection so that we can create users, make sure their password cannot be returned or that using the wrong password will return an error (setup example). Since the registration process also require to send a confirmation email that the user must respond to, it would also be necessary to setup and verify smtp communication (another setup example). Last but not least, once the test has completed the smtp connection should be closed and the database entry removed (examples of teardown).
Fixtures are Pytest functions that will setup the different objects required to connect to a database or to enable smtp connection and pass them to the actual test function.

Implementing the fixture for the smtp connection and the function that will test it, could be done as follow:

```fixture example:```
#test_smptsimple.py

import pytest
import smtplib

@pytest.fixture
def smtp_connection():
    return smtplib.SMTP("smtp.gmail.com", 587, timeout=5)


def test_ehlo(smtp_connection):
    response = smtp_connection.ehlo()
    assert response == 250

#conftest.py: sharing fixture functions.
We might realize while writing our test functions that we need to share fixture. For example, a fixture for a database connection might need to be shared between the functions that will test users creation and those that will test sending an email to those users since the email addresses are stored in the database. "conftest.py" is a Pytest configuration file that helps centralizing fixtures that need to be shared.

"Pytest (Flask-playground)"" is an example of what a conftest.py configuration file might look like for our Flask-playground project. It also contains a test file (test_config.py) that uses it.
You can download Flask-playground <here> and corresponding Pytest files for Flask-playground below.
