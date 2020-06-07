import pytest
from boost_python_example import moduleA as A

# e = callpolicies.Example() # won't work, constructore not available from python
f = A.PyClass.factory()

print(type(f))


def test_moduleA():
    # e = callpolicies.Example() # won't work, constructore not available from python
    f = A.PyClass.factory()

    assert isinstance(f, A.PyClass)
