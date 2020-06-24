import  pytest

@pytest.fixture
def supply():
    aa=20
    bb=30
    cc=40
    return [aa,bb,cc]

def test_compare_aa(supply):
    dd=30
    assert supply[0]==dd

def test_compare_bb(supply):
    dd=30
    assert supply[1]==dd

def test_compare_cc(supply):
    dd=30
    assert supply[2]==dd
