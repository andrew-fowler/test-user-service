# Summary

This is a prototype service for handling test user state for automation.

# Getting started

Install Python 3

Create the virtualenv using `python3.6 -m venv myvenv`

Activate the environment using `source ./myvenv/bin/activate`

Install dependencies using `pip install -r requirements.txt`

Run the service using `python run.py`

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