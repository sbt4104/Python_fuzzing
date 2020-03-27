from math import sqrt
from hypothesis import *
import hypothesis.strategies as st

@given(st.data())
def calc(data):
    for _ in range(data.draw(st.integers())):
        a, b, c =   data.draw(st.integers()), data.draw(st.integers()), data.draw(st.integers()) 
        area = (sqrt(3) * (a*a + b*b + c*c))/8
        s = (a + b + c)/2
        assume(a+b > c and abs(a - b) < c)
        area += (1.5 * sqrt(s*(s-a)*(s-b)*(s-c)))
        print('%.2f' % area)

if __name__ == "__main__":
    calc()