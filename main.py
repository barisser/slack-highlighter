from flask import *
import requests
import json
import db
import time
from datetime import datetime

app = Flask(__name__)
app.config['PROPAGATE_EXCEPTIONS']=True

@app.route('/', methods=['GET'])
def home():
        jsonresponse = {}
        jsonresponse['message'] = "hi there!"
        print str(request.form)
        jsonresponse=json.dumps(jsonresponse)
        response=make_response(str(jsonresponse), 200)
        response.headers['Content-Type'] = 'application/json'
        response.headers['Access-Control-Allow-Origin']= '*'
        return response

if __name__ == '__main__':
    app.run()
