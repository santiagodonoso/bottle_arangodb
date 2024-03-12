from bottle import request
import re
import requests

##############################

def db(query):
    try:
        url = "http://host.docker.internal:8529/_api/cursor"
        res = requests.post( url, json = query )
        return res.json()
    except Exception as ex:
        print("#"*50)
        print(ex)
    finally:
        pass


##############################
USER_NAME_MIN = 2
USER_NAME_MAX = 20
USER_NAME_REGEX = "^.{2,20}$"

def validate_user_name():
    error = f"user_name {USER_NAME_MIN} to {USER_NAME_MAX} characters"
    user_name = request.forms.get("user_name", "")
    user_name = user_name.strip()
    if not re.match(USER_NAME_REGEX, user_name): raise Exception(400, error)
    return user_name


