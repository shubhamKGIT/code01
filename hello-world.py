from nose.tools import assert_equal

def print_hello():
    "fucntion to print hello"
    print("Say hello to the world below")
    said_stuff = input()
    test_code(said_stuff)
    return said_stuff

def test_code(said_stuff):
    assert said_stuff == "hello"
    assert_equal(said_stuff, "hello")

if __name__=='__main__':
    myHello = print_hello()
    print(f"you said: {myHello}")