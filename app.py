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
@post("/users")
def _():
    try:
        user_name = x.validate_user_name()
        user = {"name":user_name}
        res = x.db({"query":"INSERT @doc IN users RETURN NEW", "bindVars":{"doc":user}})
        print(res)
        html = template("_user.html", user=res["result"][0])
        return f"""
        <template mix-target="#users" mix-top>
            {html}
        </template>
        """
    except Exception as ex:
        ic(ex)
        if "user_name" in str(ex):
            return f"""
            <template mix-target="#message">
                {ex.args[1]}
            </template>
            """            
    finally:
        pass


##############################
@delete("/users/<key>")
def _(key):
    try:
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
    except Exception as ex:
        ic(ex)
    finally:
        pass


















