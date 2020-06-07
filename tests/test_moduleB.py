import pytest
from boost_python_example import moduleB as B

# e = callpolicies.Example() # won't work, constructore not available from python
f = B.PyClass.factory()

print(type(f))


def test_moduleB():
    # e = callpolicies.Example() # won't work, constructore not available from python
    f = B.PyClass.factory()

    assert isinstance(f, B.PyClass)
