from sympy import *
from hypothesis import *
import hypothesis.strategies as st

x = Symbol("x")
y = Symbol("y")
z = Symbol("z")

@settings(deadline=None, max_examples=50)
@given(x=st.integers(1,1000), y=st.integers(1,1000))
def test_binomial_ints(x, y):
    assert binomial(x,y) == expand_func(binomial(x,y))

if __name__ == "__main__":
    test_binomial_ints()