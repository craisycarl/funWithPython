class MotherClass(object):
    def __init__(self):
        print 'mother class just got called'
        self.instance_var_parent = 49


class MyClass(MotherClass, object):
    def __init__(self):
        super(MyClass, self).__init__()
        print 'MyClass class just got called', self.instance_var_parent
        self.instance_var_child = 0

    class_variable = 4

    @staticmethod
    def set_class_var(value):
        MyClass.class_variable = value

    @staticmethod
    def get_class_var():
        return MyClass.class_variable

C = MyClass()  # Create an instance of the MyClass object
print C.instance_var_child  # What is the value of 'instance_var_child'?
print C.class_variable  # What is the value of class_variable?
C.set_class_var(10)  # Using 'set_class_var', write a new value.
print MyClass.class_variable  # Print that new value.

D = MyClass()  # Create a new instance of the MyClass object
print MyClass.class_variable  # What is the value of class_variable? Still 4?
D.set_class_var(555)  # Using 'set_class_var', write a new value.
print MyClass.class_variable  # What is the value of class_variable?
print D.get_class_var()  # What is the value of class_variable using the function 'get_class_var'
D.instance_var_child = 100  # Set the instance variable
print D.instance_var_child  # What is the updated instance variable?


print C.get_class_var()  # What is the value of class_variable using the function 'get_class_var'
print C.instance_var_child  # What is the instance variable for C? Still 0?
