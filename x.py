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