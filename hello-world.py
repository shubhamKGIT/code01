from nose.tools import assert_equal

def print_hello():
    "fucntion to print hello"
    return "hello"

def test_code():
    assert print_hello() == "hello"
    assert_equal(print_hello(), "hell")

if __name__=='__main__':
    print_hello()
    test_code()