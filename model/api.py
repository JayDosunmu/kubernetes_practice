import os
import random
import requests


from flask import Flask
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

model = 'Generic'
version = '0.5.0'

feature_pipeline_url = os.environ.get('FEATURE_PIPELINE_URL')
feature_pipeline_port = os.environ.get('FEATURE_PIPELINE_PORT')

class Model(Resource):
    def post(self):
        call_chain = []
        call_chain.append('predict request')
        res = requests.post('{}:{}/'.format(
            feature_pipeline_url,
            feature_pipeline_port
        ))
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
