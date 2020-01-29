# running change_app_context with appropriate parameters will
# set Flask to create an app with a test configuration

import pytest
from Flask_playground.flask_playground import app
from Flask_playground.app import db


@pytest.fixture(scope='session')
def app_session_for_module(request):
    """Creates a new db session for a test"""

    # First create an app
    app_ctx = app.app_context()
    app_ctx.push()

    # then connect to our test DB
    connection = db.engine.connect()
    transaction = connection.begin()

    options = dict(bind=connection, binds={})
    session = db.create_scoped_session(options=options)
    db.session = session

    def teardown():
        transaction.rollback()
        connection.close()
        session.remove()
        app_ctx.pop()

    request.addfinalizer(teardown)
    return session
