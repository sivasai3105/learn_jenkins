class Learn:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __enter__(self):
        print("enter method")
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("exit method")

    def fun(self):
        return self.a + self.b

    def do(self):
        return self.fun()
