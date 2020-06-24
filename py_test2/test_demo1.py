import pytest

def test_file1_method1():
    x=5
    y=6
    assert x+1==y,"Test-failed"
    assert x==y,"Test-failed"
    assert x+2==y
def test_file1_method2():
    x=5
    y=6
    assert x+1==y,"test-failed"