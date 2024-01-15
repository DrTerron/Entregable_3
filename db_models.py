# =======================================================================================
#                       IEXE Tec - Maestría en Ciencia de Datos 
#                       Productos de Datos. Proyecto Integrador
# =======================================================================================
import math
from datetime import datetime
from database import db

class Prediction(db.Model):
    """ Una predicción en la base de datos.
    """
    __tablename__ = 'prediction'  # Nombre de la tabla en la base de datos

    prediction_id = db.Column('id', db.Integer, primary_key=True)

    sepal_length = db.Column('sepal_length', db.Float, nullable=False)
    sepal_width = db.Column('sepal_width', db.Float, nullable=False)
    petal_length = db.Column('petal_length', db.Float, nullable=False)
    petal_width = db.Column('petal_width', db.Float, nullable=False)
    predicted_class = db.Column('class', db.Text, nullable=False)
    # score = db.Column('score', db.Float, nullable=False)
    created_date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

    # -----------------------------------------------------------------------------------
    def __init__(self, representation=None):
        """ Construye una Prediccion nueva usando su representación REST
        """
        super(Prediction, self).__init__()
        self.sepal_length = representation.get('sepal_length')
        self.sepal_width = representation.get('sepal_width')
        self.petal_length = representation.get('petal_length')
        self.petal_width = representation.get('petal_width')

    # -----------------------------------------------------------------------------------
    def __repr__(self):
        """ Convierte una Predicción a una cadena de texto
        """
        template_str = '<Prediction [{}]: sepal_length={}, sepal_width={}, petal_length={}, petal_width={}, class={}>'
        return template_str.format(
            str(self.prediction_id) if self.prediction_id else 'NOT COMMITED', 
            self.sepal_length, self.sepal_width, self.petal_length, self.petal_width,
            self.predicted_class or 'No calculado'
        )