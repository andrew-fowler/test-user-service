# Summary

This is a prototype service for handling test user state for automation.

# Getting started

Install Python 3

Create the virtualenv using `python3.6 -m venv myvenv`

Active the environment using `source ./myvenv/bin/activate`

Install dependencies using `pip install -r requirements.txt`

Run the service using `python run.py`

# Endpoints

### /

Displays the overview dashboard.  From here you can see all of the currently available user accounts, and lock, unlock and delete them.

### /getuser

Returns a json representation of an available user account including email and id and flags the account as locked.
If no accounts are currently available/unlocked, it will return [409 Conflict](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.10).

### /delete/_userID_

Removes a user account from the datastore.
If the user is not found, a 404 is returned.

### /lock/_userID_

Flags an account as locked.
If the user is not found, a 404 is returned.

### /unlock/_userID_

Flags an account as unlocked.
If the user is not found, a 404 is returned.

### /create

Displays a UI for creating a new test user.

### /bulkcreate

Displays a UI for bulk creating a number of test users.  Currently, the users are created using a _prefix_[incremental number]@_domain_ pattern.

### /ping

Returns 200 if the service is active.

Tested on Python 3.6