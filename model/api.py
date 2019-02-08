import random
import requests

from flask import Flask
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

model = 'Generic'
version = '0.4.0'


class Model(Resource):
    def post(self):
        call_chain = []
        call_chain.append('predict request')
        res = requests.post('100.70.37.130:11594/')
        call_chain.append(*res.data['call_chain'])
        call_chain.append('predict response: {}'.format(random.randrange(0, 1000)))
        return {
            'model': model,
            'version': version,
            'call_chain': call_chain
        }

api.add_resource(Model, '/predict')
if __name__ == '__main__':
    app.run(
        host='0.0.0.0',
        port=9001,
        debug=True
    )
