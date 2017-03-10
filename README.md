![alt text](http://i.imgur.com/Z5svcte.jpg "Service dashboard screenshot")

This is a very basic service designed for supporting test automation frameworks for products that rely on user accounts that cannot be safely used concurrently.

NOTE: For simplicity's sake, it assumes the test account passwords are pre-known or inferable from the user email.

# Getting started

Install Python 3

Create the virtualenv using `python3.6 -m venv myvenv`

Activate the environment using `source ./myvenv/bin/activate`

Install dependencies using `pip install -r requirements.txt`

Run the service using `python run.py`

# Framework integration

In your startup hook, call GET /user and it will return the first available user account record in the form

`{"date_last_locked": "Fri, 10 Mar 2017 19:50:35 GMT", "email": "test0@google.com", "id": 1, "locked": true}`

and lock it, preventing concurrent access.  Save this to state/context for use in the tests.

To release the account, call DELETE /lock/_userID_ in your teardown hook.  If the framework is stopped during runtime and the teardown hook doesn't fire, you can release the lock through the UI.

# Client Endpoints

### GET /user

Returns an available user record and locks it.  If no user is available, a 404 is returned.

### POST /user

Creates a new user.  Returns 200 if successful.

### DELETE /user/_userID_

Deletes the specified user account.  Returns 200 if successful, 404 if the user is not found.

### POST /lock/_userID_

Locks the specified user account.  Returns 200 if successful, 404 if the user is not found.

### DELETE /lock/_userID_

Unlocks the specified user account.  Returns 200 if successful, 404 if the user is not found.

### /ping

Returns 200 if the service is active.

Tested on Python 3.6