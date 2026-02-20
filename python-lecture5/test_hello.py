from hello import hello
def test_hello():
 assert hello("jose") == "hello, jose"
 assert hello() == "hello, world"
