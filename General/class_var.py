class ParentClass(object):
    def __init__(self):
        print 'Parent class just got called'
        self.instance_var_parent = 49


class ChildClass(ParentClass, object):
    def __init__(self):
        super(ChildClass, self).__init__()
        print 'Child class just got called', self.instance_var_parent
        self.instance_var_child = 0

    class_variable = 4

    @staticmethod
    def set_class_var(value):
        ChildClass.class_variable = value

    @staticmethod
    def get_class_var():
        return ChildClass.class_variable

C = ChildClass()  # Create an instance of the MyClass object
print C.instance_var_child  # What is the value of 'instance_var_child'?
print C.class_variable  # What is the value of class_variable?
C.set_class_var(10)  # Using 'set_class_var', write a new value.
print ChildClass.class_variable  # Print that new value.

D = ChildClass()  # Create a new instance of the MyClass object
print ChildClass.class_variable  # What is the value of class_variable? Still 4?
D.set_class_var(555)  # Using 'set_class_var', write a new value.
print ChildClass.class_variable  # What is the value of class_variable?
print D.get_class_var()  # What is the value of class_variable using the function 'get_class_var'
D.instance_var_child = 100  # Set the instance variable
print D.instance_var_child  # What is the updated instance variable?


print C.get_class_var()  # What is the value of class_variable using the function 'get_class_var'
print C.instance_var_child  # What is the instance variable for C? Still 0?
