from sympy import *
from hypothesis import *
import hypothesis.strategies as st

x = Symbol("x")
y = Symbol("y")
z = Symbol("z")

#@settings(deadline=None, max_examples=50)
@given(a=st.integers(), b=st.integers())
@example(-2,1)
def test_subs(a,b):
    expr = log(x) + pow(x,b) - x**3
    y = expr.subs(x,a)

if __name__ == "__main__":
    test_subs()