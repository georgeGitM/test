from flask import Flask
from flask.ext import restful
from flask import render_template
import urllib2
import Model
import couchdb

app = Flask(__name__)
api = restful.Api(app)


@app.route('/')
def index():
    city = 'Toronto'
    result = make_request('localhost:5000/Api/Get_All_Document')
    return render_template('Index.html', city = city, rows = rows)


def make_request(url):
    url = url
    try:
        response = urllib2.urlopen(url).read()
        print(response)
    except urllib2.HTTPError as e:
        print(e.message)


def count_scenario():
    return 3
db = Model.setup_couchdb('')

class Documents(restful.Resource):
    def get(self):
        num_of_scenario = count_scenario()
        map_fun = '''function(doc) {
            if(doc.id)
            emit(doc.id, doc);
            }'''
        rows = Model.get_temp_view(db,map_fun).rows
        return rows

api.add_resource(Documents, '/Api/Get_All_Document')

if __name__ == '__main__':
    app.run(debug=api)
