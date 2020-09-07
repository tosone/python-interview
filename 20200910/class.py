def foo(x):
    print("executing foo(%s)", (x))


class A(object):
    def __init__(self):
        print("13")

    def foo(self, x):
        print("executing foo(%s,%s)", (self, x))

    @classmethod
    def class_foo(cls, x):
        print("executing class_foo(%s,%s)" % (cls, x))
        cls.static_foo(x)

    @staticmethod
    def static_foo(x):
        print("executing static_foo(%s)" % x)


a = A()

a.static_foo("hello")

A.class_foo("hello")
