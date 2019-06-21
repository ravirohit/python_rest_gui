class MyFirst:
    name = 'rohit'
    def __init__(self):
        print('this is init method')
        self.name = "this is initialized in the init method"

    def basicOper(self):
        print(f'hiiiiii .... {self.name}')
      
#@add_method(MyFirst)
def display():
    print('this is dynamic method added to the the class MyFirst')
obj = MyFirst()
obj.basicOper()

