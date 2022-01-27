def hello_world():
    print('Hello, world!')

def serenafunction(who):
    print(who + ' is awesome. ')

def add5(value):
    return(value + 5)

def add5_after_multiplying(value1, value2):
    return((value1 * value2) + 5)

def print_ts(mylist):
 for x in mylist:
        if (x[0] == 't'):
            print(x)

list1 = ['circle', 'heart', 'triangle', 'square']
list2 = ['one', 'two', 'three', 'four']
print_ts(list1)
print_ts(['tooth', 'tape', 'poop'])
final_num2 = add5_after_multiplying(10,10)
final_number = add5(17)
print(final_number)
print(final_num2)
hello_world()
serenafunction('sophie')

with open('/usr/share/dict/words', 'r') as f:
    for x in range(15):
        print(f.readline().strip('10-point').strip('\n'))

words = []
with open ('/usr/share/dict/words', 'r') as f:
    words = f.read().splitlines()

for x in range(5):
    print(words[x])

my_shapes = ['circle', 'heart', 'triangle', 'square']

with open('my_shapes.txt', 'a') as f:
    for shape in my_shapes:
        f.write(f'{shape}\n')

import random
for i in range(5):
    print(random.random())

import names
for i in range(10):
    print(names.get_full_name())
