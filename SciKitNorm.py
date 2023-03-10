from sklearn.linear_model import LinearRegression, Lasso, Ridge
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

    # Aplicar L1 regularization
    lasso_reg = Lasso(alpha=0.1)
    lasso_reg.fit(X, y)
    y_pred = lasso_reg.predict(X)
    mae = mean_absolute_error(y, y_pred)

    for i in range(len(y)):
        print("y_pred: %f, y_real: %f" % (y_pred[i], y[i]))
    print("MAE L1: %f" % mae)

    print("\n")

    # Aplicar L2 regularization
    ridge_reg = Ridge(alpha=0.1)
    ridge_reg.fit(X, y)
    y_pred = ridge_reg.predict(X)
    mae = mean_absolute_error(y, y_pred)

    for i in range(len(y)):
        print("y_pred: %f, y_real: %f" % (y_pred[i], y[i]))
    print("MAE L2: %f" % mae)

    print("\n")

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

    #Aplicar L1 regularization
    lasso_reg = Lasso(alpha=0.1)
    lasso_reg.fit(X, y)
    y_pred = lasso_reg.predict(X)
    mse = mean_squared_error(y, y_pred)

    for i in range(len(y)):
        print("y_pred: %f, y_real: %f" % (y_pred[i], y[i]))
    print("MSE L1: %f" % mse)

    print("\n")

    #Aplicar L2 regularization
    ridge_reg = Ridge(alpha=0.1)
    ridge_reg.fit(X, y)
    y_pred = ridge_reg.predict(X)

    mse = mean_squared_error(y, y_pred)

    for i in range(len(y)):
        print("y_pred: %f, y_real: %f" % (y_pred[i], y[i]))
    print("MSE L2: %f" % mse)






# Ejecutar main
if __name__ == "__main__":
    main()
