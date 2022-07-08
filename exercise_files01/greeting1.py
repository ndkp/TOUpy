def hello():
    print("こんにちは")
def bye():
    print("さようなら")
def greeting(func):
    print("みなさん")
    func()

greeting(bye)

