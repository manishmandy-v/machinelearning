import pandas as pd
import numpy
import math
csv = pd.read_csv("./3_gradient_descent/Exercise/test_scores.csv")


def gradient_descent(x,y):
    m_curr = b_curr = 0
    iterations = 1000000
    learning = 0.0002111
    n = len(x)
    for i in range(iterations):
        y_predicted = m_curr*x+b_curr
        cost = (1/n)*sum([val**2 for val in (y-y_predicted)])
        md = -(2/n)*sum(x*(y-y_predicted))
        bd = -(2/n)*sum(y-y_predicted)
        m_curr = m_curr-learning*md
        b_curr = b_curr-learning*bd
        print(f'm{m_curr} , b{b_curr} , cost{cost} , iter{i}')

x = numpy.array(csv.math)
y = numpy.array(csv.cs)
gradient_descent(x,y)
