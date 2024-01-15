# =======================================================================================
#                       IEXE Tec - Maestría en Ciencia de Datos 
#                       Productos de Datos. Proyecto Integrador
#
# Debes de adaptar este script para integrar tu modelo predictivo.
# =======================================================================================
from pandas import read_csv
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
import pickle


# =======================================================================================
def create_simple_model():
    """ Función para entrenar un modelo simple usando los datos de prueba de tipos de flores
        Consulta la documentación de este famoso conjunto de datos:
        https://en.wikipedia.org/wiki/Iris_flower_data_set

        Modifica esta función para integrar el modelo predictivo que quieres integrar a
        tu API REST.
    """

    names = ['sepal-length', 'sepal-width', 'petal-length', 'petal-width', 'class']
    dataset = read_csv('iris.csv', names=names)
    array = dataset.values
    X = array[:,0:4]
    y = array[:,4]
    X_train, X_validation, Y_train, Y_validation = train_test_split(
        X, y, test_size=0.20, random_state=1, shuffle=True
    )

    # Para este ejemplo creamos un modelo de regresión logística simple
    model = LogisticRegression(solver='liblinear', multi_class='ovr')
    model.fit(X_train, Y_train)

    # ----------------------------------------------------------------------
    # Esta línea crea un archivo "pickle" que contiene el modelo predictivo,
    # este archivo nos va a servir para usarlo en el API REST.
    # ----------------------------------------------------------------------
    pickle.dump(model, open('simple_model.pkl','wb'))


# =======================================================================================
if __name__ == '__main__':
    """ Esta función ejecuta el programa de Python cuando se invoca desde 
        línea de comando.
    """
    create_simple_model()
