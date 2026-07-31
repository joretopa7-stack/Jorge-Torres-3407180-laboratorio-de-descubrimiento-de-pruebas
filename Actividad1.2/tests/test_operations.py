from app.operations import add

def test_add_two_positive_numbers():
    assert add(5, 7) == 12
