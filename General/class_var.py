class MotherClass(object):
    def __init__(self):
        print 'mother class just got called'
        self.instVarA = 49

class MyClass(MotherClass, object):
    def __init__(self):
        super(MyClass, self).__init__()
        print 'MyClass class just got called', self.instVarA
        self.instVarB = 0
         
    classVar = 4
    
    def setClassVar(self, value):
        MyClass.classVar = value
        
    def getClassVar(self):
        return MyClass.classVar
        
C = MyClass()
print C.classVar
C.setClassVar(10)
print MyClass.classVar

D = MyClass()
print MyClass.classVar
D.setClassVar(1234)
print MyClass.classVar
print D.getClassVar()
D.instVarB = 100
print D.instVarB
print 'changes'

E = MyClass()
print MyClass.classVar
E.setClassVar(4321)
print MyClass.classVar
print E.getClassVar()

print C.getClassVar()
print C.instVarB