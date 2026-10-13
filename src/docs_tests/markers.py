import pytest

def get_length(string:str)->int:
    return len(string)

@pytest.mark.skip
def test_get_len():
    assert get_length("hello") == 5


@pytest.mark.skipif('2*2 == 5')
def test_get_length():
    assert get_length("hello") == 5


def gen_sequence(n:int)->list:
    return list(range(1,n+1))

@pytest.mark.xfail
def test_gen_sequence():
    assert gen_sequence(-1)




