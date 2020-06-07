#!/usr/bin/env python
import pytest
from boost_python_example import callpolicies as policies


def test_callpolicies():
    # e = callpolicies.Example() # won't work, constructore not available from python
    f = policies.Example.factory()
    assert isinstance(f, policies.Example) and str(f) == "factory"
