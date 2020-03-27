from sympy import *
from hypothesis import *
import hypothesis.strategies as st

x = Symbol("x")
y = Symbol("y")
z = Symbol("z")

def custom_symbol():
    return st.builds(
        Symbol,
        name = st.characters()
    )

"""
#@settings(deadline=None, max_examples=50)
@given(a=st.integ
def test_subs(a,b):
    expr = log(x) + pow(x,b) - x**3
    y = expr.subs(x,a)
"""

if __name__ == "__main__":
    print(custom_symbol().example())