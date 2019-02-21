from pigweb import PigWeb
import json

def jsonify(status=200, **kwargs):
    content = json.dumps(kwargs)
    response = PigWeb.Response()
    response.content_type = "application/json"
    response.status_code = status
    response.body = "{}".format(content).encode()
    return response


def validate(d:dict, name:str, type_func, default, func):
    try:
        result = d.get(name, default)  # 判断
        result = type_func(result)
        result = func(result, default)
    except:
        result = default
    return result