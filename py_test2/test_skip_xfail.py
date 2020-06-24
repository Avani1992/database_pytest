import pytest

@pytest.mark.skip
def test_add1():
    assert 100+200==400

@pytest.mark.skip
def test_add2():
    assert 100+200==300

@pytest.mark.xfail
def test_add3():
    assert 100+200==400

@pytest.mark.xfail
def test_add4():
    assert 100+200==300


def test_add5():
    assert 100+200==400

def test_add6():
    assert 100+200==300
