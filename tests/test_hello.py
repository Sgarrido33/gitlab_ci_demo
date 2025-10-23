"""
Tests unitarios para hello.py
test
"""
import pytest
from hello import greet, add

def test_greet_default():
    assert greet() == "Hello, World!"

def test_greet_custom():
    assert greet("DevOps") == "Hello, DevOps!"

def test_add():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0
    assert add(0, 0) == 0