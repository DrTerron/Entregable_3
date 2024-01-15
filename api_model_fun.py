import os
import pickle
import numpy
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_restx import Api, Resource, fields
from werkzeug.middleware.proxy_fix import ProxyFix
from database import db
from db_models import Prediction

app = Flask(__name__)
app.wsgi_app = ProxyFix(app.wsgi_app)

def configure_app():
    db_uri = 'sqlite:///' + os.path.abspath(os.path.join(os.path.dirname(__file__), 'prods_datos.db'))
    app.config['SQLALCHEMY_DATABASE_URI'] = db_uri
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

def configure_db():
    with app.app_context():
        db.create_all()

def load_predictive_model():
    return pickle.load(open('simple_model.pkl', 'rb'))

def create_api():
    api = Api(
        app,
        version='1.0',
        title='API REST',
        description='API REST entregable 3 Daniel Terron',
    )
    return api

def create_namespace(api):
    ns = api.namespace('entregable3', description='entregable3')
    return ns

def create_observation_model(api):
    return api.model('Observacion', {
        'sepal_length': fields.Float(description="Longitud del sépalo"),
        'sepal_width': fields.Float(description="Anchura del sépalo"),
        'petal_length': fields.Float(description="Longitud del pétalo"),
        'petal_width': fields.Float(description="Anchura del pétalo"),
    })

def create_prediction_response(prediction):
    model_data = {
        'sepal_length': prediction.sepal_length,
        'sepal_width': prediction.sepal_width,
        'petal_length': prediction.petal_length,
        'petal_width': prediction.petal_width,
        "class": str(prediction.predicted_class)
    }
    response = {
        "api_id": prediction.prediction_id,
        "created_date": prediction.created_date.isoformat(),
        "prediction": model_data
    }
    return response

def get_predictions():
    return [create_prediction_response(prediction) for prediction in Prediction.query.all()], 200

def post_prediction(payload):
    prediction = Prediction(representation=payload)
    model_data = [numpy.array([
        prediction.sepal_length, prediction.sepal_width,
        prediction.petal_length, prediction.petal_width,
    ])]
    prediction.predicted_class = str(predictive_model.predict(model_data)[0])

    db.session.add(prediction)
    db.session.commit()

    response = {
        "class": prediction.predicted_class,
        "api_id": prediction.prediction_id
    }
    return response, 201

def marshall_prediction(prediction):
    return create_prediction_response(prediction)

def trunc(number, digits):
    import math
    stepper = 10.0 ** digits
    return math.trunc(stepper * number) / stepper

if __name__ == '__main__':
    configure_app()
    configure_db()
    predictive_model = load_predictive_model()
    api = create_api()
    ns = create_namespace(api)
    observacion_repr = create_observation_model(api)

    @ns.route('/', methods=['GET', 'POST'])
    class PredictionListAPI(Resource):
        def get(self):
            return get_predictions()

        @ns.expect(observacion_repr)
        def post(self):
            return post_prediction(api.payload)

    app.run(debug=True)
