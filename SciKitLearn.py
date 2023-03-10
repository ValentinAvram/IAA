from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error
import numpy as np

def main():
    #Regresion linear usando gradiente descendente y error medio absoluto (MAE)
    data = np.loadtxt("data.txt", delimiter=",")
    X = data[:, :-1]  # todas las columnas excepto la última son las variables independientes
    y = data[:, -1]

    lr = LinearRegression()
    learning_rate = 0.01
    maxIter = 1000

    for i in range(maxIter):
        lr.fit(X, y)
        y_pred = lr.predict(X)
        error = y - y_pred
        lr.coef_ += learning_rate * np.dot(X.T, np.sign(error)) / len(X)

    y_pred = lr.predict(X)
    mae = mean_absolute_error(y, y_pred)

    for i in range(len(y)):
        print("y_pred: %f, y_real: %f" % (y_pred[i], y[i]))
    print("MAE: %f" % mae)

    #Regresion linear usando gradiente descendente y error cuadratico medio (MSE)
    data = np.loadtxt("data.txt", delimiter=",")
    X = data[:, :-1]  # todas las columnas excepto la última son las variables independientes
    y = data[:, -1]

    lr = LinearRegression()
    learning_rate = 0.01
    maxIter = 1000

    for i in range(maxIter):
        lr.fit(X, y)
        y_pred = lr.predict(X)
        error = y - y_pred
        lr.coef_ += learning_rate * np.dot(X.T, error) / len(X)

    y_pred = lr.predict(X)
    mse = mean_squared_error(y, y_pred)

    for i in range(len(y)):
        print("y_pred: %f, y_real: %f" % (y_pred[i], y[i]))
    print("MSE: %f" % mse)



# Ejecutar main
if __name__ == "__main__":
    main()
