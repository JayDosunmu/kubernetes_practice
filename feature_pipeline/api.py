import random

from flask import Flask
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

features = ['sentiment', 'spam', 'questions', 'flowers']


class FeaturePipeline(Resource):
    def post(self):
        call_chain = []
        call_chain.append(random.choice(features))
        return {'call_chain': call_chain}

api.add_resource(FeaturePipeline, '/')

if __name__ == '__main__':
    app.run(
        host='0.0.0.0',
        port=11594,
        debug=True
    )
