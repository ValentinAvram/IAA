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
    add = 0
    add2 = 0
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

    #menu to select method
    print("Select method:")
    print("1. Method 2 Cuadratic")
    print("2. Method 3 Absolute")
    print("0. Exit")

    #get user input
    option = int(input("Enter option: "))
    while option != 0:
        if option == 1:
            m1 = 1
            m2 = 1
            b = 1

            print("2000 Iterations Cuadratic")
            for i in range(2000):
                m1, m2, b = func2(m1, m2, b, h)
            # print comparation
            for i in range(len(Matrix)):
                print("Real value: ", Matrix[i][2], "Predicted value: ", m1 * Matrix[i][0] + m2 * Matrix[i][1] + b)
        elif option == 2:
            m1=1
            m2=1
            b=1

            print("2000 Iterations Absolute")
            for i in range(2000):
                m1, m2, b = func3(m1, m2, b, h)
            # print comparation
            for i in range(len(Matrix)):
                print("Real value: ", Matrix[i][2], "Predicted value: ", m1 * Matrix[i][0] + m2 * Matrix[i][1] + b)
        option = int(input("\n\nEnter option: "))

#Ejecutar main
if __name__ == "__main__":
    main()