import numpy as np

Matrix = [[1,   2, 1.03],
          [1,   3, -1.44],
          [2,   3, 4.53],
          [2,   4, 2.24],
          [3,   2, 13.27],
          [3,   5, 5.62],
          [4,   1, 21.53]]


def func3(m1, m2, b, h):
    for i in range(len(Matrix)):
        predicted = m1 * Matrix[i][0] + m2 * Matrix[i][1] + b
        if Matrix[i][2] > predicted:
            m1 = m1 + h * Matrix[i][0]
            m2 = m2 + h * Matrix[i][1]
            b = b + h
        else:
            m1 = m1 - h * Matrix[i][0]
            m2 = m2 - h * Matrix[i][1]
            b = b - h

    return m1, m2, b


def func2(m1, m2, b, h):
    for i in range(len(Matrix)):
        predicted = m1*Matrix[i][0] + m2*Matrix[i][1] + b
        m1 = m1 - (2*h/len(Matrix)) * (predicted - Matrix[i][2]) * Matrix[i][0]
        m2 = m2 - (2*h/len(Matrix)) * (predicted - Matrix[i][2]) * Matrix[i][1]

        b = b - (2*h/len(Matrix)) * (predicted - Matrix[i][2])

    return m1, m2, b

def main():
    b = 1
    m1 = 1
    m2 = 1
    h = 0.01

    for i in range(2000):
        m1, m2, b = func2(m1, m2, b, h)
    # print comparation
    print("Metodo 2 sin regularizacion")
    for i in range(len(Matrix)):
        print("Real value: ", Matrix[i][2], "Predicted value: ", m1 * Matrix[i][0] + m2 * Matrix[i][1] + b)

    #MAE
    mae = 0
    for i in range(len(Matrix)):
        mae += abs(Matrix[i][2] - (m1 * Matrix[i][0] + m2 * Matrix[i][1] + b))
    mae = mae / len(Matrix)
    print("MAE: ", mae)
    print("\n")

    #Metodo 2 L1
    normL1 = abs(m1) + abs(m2)
    print("Metodo 2 L1")
    maeL1 = mae + 0.1 * normL1
    print("MAE L1: ", maeL1)

    #Metodo 2 L2
    normL2 = m1**2 + m2**2
    print("Metodo 2 L2")
    maeL2 = mae + 0.1 * normL2
    print("MAE L2: ", maeL2)

    print("\n")


    #Metodo 3
    b = 1
    m1 = 1
    m2 = 1
    h = 0.01

    for i in range(2000):
        m1, m2, b = func3(m1, m2, b, h)
    # print comparation
    print("Metodo 3 sin regularizacion")
    for i in range(len(Matrix)):
        print("Real value: ", Matrix[i][2], "Predicted value: ", m1 * Matrix[i][0] + m2 * Matrix[i][1] + b)

    #MSE
    mse = 0
    for i in range(len(Matrix)):
        mse += (Matrix[i][2] - (m1 * Matrix[i][0] + m2 * Matrix[i][1] + b))**2
    mse = mse / len(Matrix)
    print("MSE: ", mse)
    print("\n")

    #Metodo 3 L1
    normL1 = abs(m1) + abs(m2)
    print("Metodo 3 L1")
    mseL1 = mse + 0.1 * normL1
    print("MSE L1: ", mseL1)

    #Metodo 3 L2
    normL2 = m1**2 + m2**2
    print("Metodo 3 L2")
    mseL2 = mse + 0.1 * normL2
    print("MSE L2: ", mseL2)




#Ejecutar main
if __name__ == "__main__":
    main()