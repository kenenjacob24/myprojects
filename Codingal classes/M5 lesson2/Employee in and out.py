class Employee:

    def __Init__(self):
        print('Employee created')

    def __del__(self):
        print("Destuction called")

def create_obj():
    print('Making Object...')
    obj = Employee()
    print('function end...')

print('Calling create)_obj() function...')
obj = create_obj()
print('Program End...')