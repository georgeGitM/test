from flask import Flask
from flask.ext import restful
from flask import render_template
import urllib
import requests
import Model
import couchdb
import json

app = Flask(__name__)
api = restful.Api(app)

db = Model.setup_couchdb('')

class Documents(restful.Resource):
    def get(self):
        num_of_scenario = 3
        map_fun = '''function(doc) {
            if(doc.id)
            emit(doc.id, doc);
            }'''
        rows = Model.get_temp_view(db,map_fun).rows
        return rows

api.add_resource(Documents, '/Api/Get_All_Document')

@app.route('/')
def index():
    city = 'Toronto'
    result = make_request('http://localhost:5000/Api/Get_All_Document')
    #result = [1, 'foo']
    return render_template('Index.html', city = city, result = json.dumps(result))


def make_request(url):
    url = url
    response = requests.api.get(url)
    result = response.json()
    return result

if __name__ == '__main__':
    app.run(host='localhost' ,port=4444, debug=True)
