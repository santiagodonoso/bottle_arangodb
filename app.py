from bottle import delete, get, post, request, static_file, template
import x
from icecream import ic

##############################
@get("/favicon.ico")
def _():
    return static_file("favicon.ico", ".")

##############################
@get("/app.css")
def _():
    return static_file("app.css", ".")

##############################
@get("/mixhtml.js")
def _():
    return static_file("mixhtml.js", ".")

##############################
@get("/")
def _():
    users = x.db({"query":"FOR user IN users RETURN user"})
    return template("index", users=users["result"])

##############################
@post("/users")
def _():
    user_name = request.forms.get("user_name")
    user = {"name":user_name}
    res = x.db({"query":"INSERT @doc IN users RETURN NEW", "bindVars":{"doc":user}})
    print(res)
    html = template("_user.html", user=res["result"][0])
    return f"""
    <template mix-target="#users" mix-top>
        {html}
    </template>
    """

##############################
@delete("/users/<key>")
def _(key):
    ic(key)
    res = x.db({"query":"""
                FOR user IN users
                FILTER user._key == @key
                REMOVE user IN users RETURN OLD""", 
                "bindVars":{"key":key}})
    print(res)
    return f"""
    <template mix-target="[id='{key}']" mix-replace></template>
    """



















