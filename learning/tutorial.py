"""Tutorial"""

# NOTE: CHAPTER 1: BASIC MATH
# how about some very basic math?
# division always returns a floating point number
print("\n3 / 4 =", 3 / 4, end='\n\n') # 0.75

# floor division, on the other hand, returns an integer
print("3 / 4 =", 3 // 4, end='\n\n') # 0

# for the remainder, use %
print("3 % 4 =", 3 % 4, end='\n\n')

# and ** for power
print("3^4 =", 3**4, end='\n\n')

# but, achtung: since ** has higher precedence,
print("-2^2 !=", -2**2, end='\n\n')

# so, mind the ().
print("-2^2 =", (-2)**2, end='\n\n')

# math operations with mixed type operands convert all int to float
print("1 + 2 =", 1 + 2.0, end='\n\n')
print("2 x 3 =", 2.0 * 3, end='\n\n')

# NOTE: CHAPTER 2: STRINGS
# now, we have already been using strings
print('This is a string.')
print('Hey! I am no \'string\', mate.')
print("Are you\nSURE\nyou're not a\n'string',\n\tmate?", end='\n\n')

# check this out, it is raw!
print("c:\path\to\some\file\name")
print(r"c:path\to\some\file\name", end='\n\n')

# printing in multiple lines
# (the backslash avoids automatic inclusion of a line break)
print("""\
Usage: thingy [OPTIONS]
\t-h\tDisplay thingy
\t-H\tDisplay huge thingy
""", end='\n\n')

# repeating and concatenating strings
print("I've got the", 3 * 'blu' + 'es!')

# but also (and it only works with literals)
print("Me"
      " too...", end='\n\n')

# there is no char type; a char is simply...
thestring = 'b'

# a str of size 1:
print(f"type of thestring [{thestring}]: ", type(thestring), end='\n\n')

# indices!
thestring = 'I am Stan, the Man!'
print(thestring[5])
print(thestring[0])

# -1 is the 0 backwards, and -n is the (n - 1) backwards
print(thestring[-1])
print(thestring[-19], end='\n\n')

# unsafe: it throws an IndexError if index out of range
# don't do it!
# print(thestring[27])
# print(thestring[-50], end='\n\n')

# slicing! it always includes the start and excludes the end:
thestring = 'I am Ulma, the Woman!'
print(thestring[2:7])

# and it is always safe
print(thestring[2:4587])

# you can ommit the start, and it starts from 0
print(thestring[:7])

# or leave the end out, and it goes till the end
print(thestring[7:])

# you can also do this
print(thestring[:], end='\n\n')

# strings are immutable
# don't do it! Will throw a TypeError
# thestring[3] = 'x'

# check this out
thestring = '0123456789'
print(thestring)
thenewstring = thestring[2:6] + '46810'
print(thenewstring, end='\n\n')

# strings have len
print(len(thestring), end='\n\n')

# NOTE: CHAPTER 3: LISTS
# now lists!
# this creates an empty list
mylist = []

# lists can contain items of different types (and nested lists)
mylist = [1, 'two', [3, 'three', 'troi', 'drei']]
print(mylist)

# it can also be done like this
mylist = []
mylist.append(1)
mylist.append('two')
mylist.append([3, 'three', 'troi', 'drei'])
print(mylist)

# indexes and slices work just like with strings, mate
print(mylist[2])
print(mylist[-2:])

# it means that using index out of range is unsafe in indexing
# don't do it! will throw an IndexError: intex out of range
# mylist[27]

# and that using index out of range when slicing is safe
print(mylist[27:4981], end='\n\n')

# but beware, mate
# slicing returns a shallow copy
# that means: if an element is an object
# the shallow copy contains a reference to it
# and not it itself (capisce?)
otherlist = mylist[-2:]
print(otherlist)
otherlist[1][2] = 'TROI'
print(otherlist)
print(mylist)

# we have seen above that lists are mutable, unlike strings
# but they can be concatenated
otherlist = mylist + ['247.3 - 242.3']
print(otherlist, end='\n\n')

# since lists are mutable, this is cool - check it out
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
print(letters)
letters[2:5] = ['C', 'D', 'E']
print(letters)
letters[2:5] = []
print(letters)
letters[:] = []
print(letters, end='\n\n')

# len works for lists too (actually, for any sequence or collectible)
print(otherlist)
print(len(otherlist), end='\n\n')

# NOTE: CHAPTER 4: FLOW CONTROL
# now to more advanced language constructs
# see if you can figure this one out
a, b = 0, 1
while b < 20:
    a, b = b, a+b
    print(a)

print("Beware! "
      "Expressions and functions are evaluated "
      "before assignment.\n"
      "(and the right hand side expressions and functions "
      "are evaluated from left to right)", end='\n\n')

# in a test, anything with a non-zero lenght is true, 
# empty sequences are false
alist = [1, 2, 3]
while alist:
    print(alist.pop())

print("\nYou should check PEP 8 regularly, mate.", end='\n\n')

# there is also the 'ifamous' if
if alist:
    print(alist)
elif alist is None:
    print("None.")
else:
    print("Nada.", end='\n\n')

# in python, for iterates over items of any sequence
# (note: in can be used in other places, not just for)
words = ['cat', 'window', 'defenestrate']
for w in words:
    print(w, len(w))

# when using collections, you cannot change it in a for loop
users = {'Hans': 'active', 'Eleonor': 'inactive', 'Barbora': 'active'}
print(users)

# don't do it!
# will throw RuntimeError: dictionary changed size during iteration
# for user, status in users.items():
#     if status == 'inactive':
#         del users[user]

# iterate over a copy instead
for user, status in users.copy().items():
    if status == 'inactive':
        del users[user]

print(users)

users = {'Hans': 'active', 'Eleonor': 'inactive', 'Barbora': 'active'}

# or create a new collection
active_users = {}
print(active_users)
for user, status in users.items():
    if status == 'active':
        active_users[user] = status

print(active_users, end='\n\n')

# but...to us all there comes the time when we just need
# the fix of iterating over a sequence of numbers...
# then we can use the ol' while style
i = 0
while i <= 10:
    print(i, end=' ')
    i += 1
print("")

# or...we could use the infamous range()
for i in range(11):
    print(i, end=' ')
print("")

# or like an avantgardist:
for i in range(12, 2, -3):
    print(i, end='   ')
# remember: in range(start, stop[, step]), start defaults to 0
# and, mathematically speaking, the interval is closed on start
# and open on stop
print("\n")

# at this point, if you feel the crave for iterating over
# the indices of a sequence, you can do this for now
phrase = ['Mary', 'had', 'a', 'little', 'lamb']
for i in range(len(phrase)):
    print(i, phrase[i])
print("")

# important remark: range() is not a list created whole
# it spits the next element whenever needed
# thus saving space
# range is a kind of iterable
# and iterables make good targets for constructs and functions
# that expects something over wich they can iterate
# until then can no more
# for is one of these constructs
# there is also this
print(sum(range(5)))
print("")

# check this out
def print_some_numbers(some_numbers):
    for number in numbers:
        if number%2 == 0:
            continue
        elif number%3 == 0:
            print(number, end=' ')
        elif number%7 == 0:
            print("...cough!")
            break
        else:
            print("?", end=' ')
        print("and", end=' ')
    else:
        print("EOL (i. e. end of list)")

numbers = [2, 3, 5, 6, 7, 9, 13]
print_some_numbers(numbers)
numbers = [2, 3, 5, 6, 8, 9, 13]
print_some_numbers(numbers)
print("")
# so:
# continue skips the rest of the for loop execution
# and goes to the next one
# break breaks out of the for loop, ending it
# else clause of the for loop only executes when the for loop
# reaches gracefully the end of the list
# (in a while, an else clause only gets executed when
# the test condition becomes false)
# capisce?

# if there is nothing to be done or you just want a dummy,
# thats the magic word you write
if numbers:
    pass

def dummy():
    pass

class dumdummy:
    pass

# and then there is the match
code = 404

match code:
    case 400:
        print("Bad request, baby.")
    case 401 | 403:
        print("Not allowed, baby.")
    case 404:
        print("Not found, baby.")
    case 418:
        print("I'm a teapot, baby!")
    # ah! the wildcard!
    case _:
        print("Somthin's wrong withis internet, baby...")
print("")

# note that it matches not only values, but patterns and values
# it peels the data and can be used to bind variables
# (something similar to unpacking, like x, y = my_tuple)
# print("COMMAND ME, MASTER:")
# command = input("> ")
# exits = ["back", "forth", "forward", "backwards"]

# match command.split():
#     # *_ can be used, if binding is not wanted
#     case ["drop", *objects]:
#         print("\nYou drop:")
#         for obj in objects:
#             print(obj)
#         print("And then you fall. Forever.")
#     case ["run", "fast"]:
#         print("\nYou run fast. And then you fall. Forever.")
#     case ["run", "slowly"]:
#         print("\nYou run slowly. You keep running slowly. " 
#               "And then you fall. Forever.")
#     case ["go", ("north" | "south" | "east" | "west") as direction]:
#         print(f"\nYou go {direction}. And then you fall. Forever.")
#     case ["go", direction] if direction in exits:
#         print(f"\nYou try to go {direction}. And then you fall. "
#               "Forever.")
#     case ["help"]:
#         print('\nYou cry for help. And then you fall. Forever.')
#     case _:
#         print("\nYou just fall. Forever.")
# print("")

# the following is also useful, it is about match points
class Point:
    __match_args__ = ('x', 'y')
    def __init__(self, x, y):
        self.x = x
        self.y = y

def match_points(the_points):
    match the_points:
        case []:
            print("Sorry, no points for you.")
        case [Point(0, 0)]:
            print("The Great Origin!")
        case [Point(x, 0)]:
            print(f"Just abscissas for you: {x},0")
        case [Point(0, y)]:
            print(f"Just ordinates for you: 0,{y}")
        # the guard! values are captured before guards are evaluated
        case [Point(x, y)] if abs(x) == abs(y):
            print(f"Some diagonal! {x}:{y}")
        case [Point(0, y1), Point(0, y2), Point(0, y3)]:
            print(f"You have 3 ordinate break points: 0,{y1} 0,{y2} 0,{y3}")
        case[Point(x, y)]:
            print(f"Ugh, so ordinary...match point for you: {x},{y}")
        case _:
            print("This is new!...")

match_points([])
match_points([Point(0,-3)])
match_points([Point(0,0), Point(1,2)])
match_points([Point(0,0), Point(0,2), Point(0,-1)])
match_points([Point(0,0), Point(1,2), Point(-1,-1)])
match_points([Point(0,0)])
match_points([Point(-1,1)])
match_points([Point(1,2)])
print("")

# NOTE: CHAPTER 5: FUNCTIONS
# and just like that you have seen how to define functions!
def my_function(args):
    """Always use a docstring (I think they are in PEP 257)"""
    return "I did nothing."

# functions without a return statement
# always return None
def my_function_returns(args):
    """Remember the docstring"""
    pass

print(my_function_returns(1), end='\n\n')

# as does a lonely return
def my_function_returns():
    """Always remember the docstring.
    """
    if True:
        return
    
print(my_function_returns(), end='\n\n')

# python uses call by object value, i. e., if a mutable object
# is passed, the caller will see any changes the callee makes to it
alist = [1]
print(alist)

def afunction(arg):
    arg.extend([2, 3, 4])
    return 0

afunction(alist)
print(alist, end='\n\n')

# the function is an object
print(alist)
f = afunction
f(alist)
print(alist, end='\n\n')

# a function can be defined with a variable number of arguments
# 1: by using default values
def one(arg1, arg2 = 'I\'m an arg'):
    print(arg1, arg2)

one(1)
print()

# default values are evaluated at function definition in the
# defining scope
i = 5

def f(arg = i):
    print(arg)

i = 6
f()
print()

# default values are evaluated only once, so be aware
def f(arg1, arg2 = []):
    arg2.append(arg1)
    return arg2

print(f(1))
print(f(2))
print(f(3))
print()

# if this is not the intended behaviour, then
def f(arg1, arg2 = None):
    if arg2 is None:
        arg2 = []
    arg2.append(arg1)
    return arg2

print(f(1))
print(f(2))
print(f(3))
print()

# things got a little messy in the tutorial, so I'm trying to
# clean it up for better understanding...
# a function definition, in general, looks like this
# def name(pos1, pos2, /, key_or_pos1, key_or_pos2, *, kwarg1, kwarg2)
# where pos is positional and kw is keyword
# / and * are optional
# above, / indicates that pos1 and pos2 are positional only
# and * indicates that kwarg1 and kwarg2 are keyword only
# whatever comes in between them may be used either
# as positional or keyword
# but if / and * are not present, arguments can be passed
# by position or by keyword
# order is not important for keyword arguments
# if you do something like f(name, **kwargs) and there is a 'name' key
# in kwargs, you get a 'multiple values error'
# (since name parameter can be either positional or keyword)
# but if you change it to f(name, /, **kwargs) then it is ok

# figure this one out
def f(a, b, /, c, *d, e, f, **g):
    print(a, b, c, d, e, f, g)

f('a', 'b', 'c', 'd', 'd', 'd', e='e', f='f', **{'h':'h', 'i':'i'})
print()

# if arguments are in a list / tuple or dict, they need to be unpacked
# by using * (list/tuple) or ** (dict)
args = [3, 6]
print(list(range(*args)))

def area(width, height):
    print(width*height)

args = {'width': 5, 'height': 7}
area(**args)
print()

# lambda expressions are single expression anonymous functions,
# to be use wherever function objects are needed.

def make_incrementor(n):
    """Remember: remember the docstring (summary)
    
    Just remember it, always, really (description)
    (note that the previous line and this one
    are indented by 4 spaces)
    """
    return lambda x: x + n

inc = make_incrementor(3)
print(inc(3))
print(inc(4))

pairs = [(1, 'one'), (2, 'two'), (3, 'three'), (4, 'four')]
print(pairs)
pairs.sort(key=lambda pair:pair[1])
print(pairs)
print()

# you can also annotate
def food(ham: str, eggs: str = 'eggs') -> str:
    print("Annotations:", food.__annotations__)
    print("Arguments:", ham, eggs)
    return ham + " and " + eggs

print(food('spam'))
print()

# NOTE: CHAPTER 6: DATA STRUCTURES

# you can turn lists into stacks by using append(n) and pop()
# but for queues, it is better to use "from collections import deque"

# list comprehensions: a simple way to create lists without side effects
# comprehensions are good to filter and extend lists
# form:
# [expression for clause (other for or if clauses)]
# the expression will be evaluated in the context of the
# for or if clauses
squares = [x**2 for x in range(10)]
# which is equivalent to
# squares = list(map(lambda x: x**2, range(10)))
print(squares)

diffs = [(x, y) for x in [2, 1, 3] for y in [3, 1, 4] if x != y]
print(diffs)

vec = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flat = [num for elem in vec for num in elem]
print(vec)
print(flat)

matrix = [
    ['a', 'b', 'c', 'd'],
    ['e', 'f', 'g', 'h'],
    ['i', 'j', 'l', 'm']
]

trans = [[row[i] for row in matrix] for i in range(4)]
print(matrix)
print(trans)
print()

# del: another way to remove items from lists
alist = [0, 1, 2, 2, 3, 3, 4, 4, 4, 5]
print(alist)
del alist[2]
print(alist)
del alist[4:7]
print(alist)
del alist[:]
print(alist)
print()

# now, tuples:
t = (34, 43, 'hi')
print(t)

# like lists, tuples can be nested and can contain mutable objects
# the parenthesis are not needed here, but they are good for clarity
u = (t, (33, 44, 45, 54, 'hello'))
print(u)

s = (u, ['a', 'b', 'c'])
print(s)
s[1][1] = 'B'
print(s)
print()

# and like strings, tuples are immutable
# don't do it! will throw TypeError:
# object does not support item assignment
# u[0] = 11, 22, 33

# creating an empty tuple
empty = ()
print(empty)

# creating a single value tuple
single = ('just the one',)
print(single)
print()

# this is packing
pack = ('one', 2, '3')
print(pack)

# this is unpacking
# (and it works for any sequence on the right-hand side)
a, b, c = pack
print(a, b, c)
print()

# sets
# an empty set (careful: using {} creates an empty dict)
basket = set()
print(basket)
basket = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
# no duplicates, 'cause its a set
print(basket)

# membership testing
print('orange in basket?', 'orange' in basket)
print('what about papaya?', 'papaya' in basket)
print()

# creating sets of unique letters from words
# (remember: sets are unordered)
a = set('abracadabra')
b = set('alacazam')
print(a)
print(b)
print()
print(a - b)
print(a | b)
print(a & b)
print(a ^ b)
# a ^ b can also be
print((a|b) - (a&b))
print((a|b) - (a&b) == a^b)
print()

# like lists, set comprehensions are also possible
a = {x for x in 'abracadabra' if x not in 'abc'}
print(a)
print()

# dictionaries, or dicts, are indexed by keys
# a key can be any immutable type: strings and numbers
# can be used, tuples can be used (if composed of strings, numbers
# and tuples); lists cannot be used
# dicts: a set of key:value pairs where the keys are unique

# an empty dictionary
empty = {}
print(empty)

tel = {'jack': 4098, 'sape': 4139}
tel['guida'] = 4127
print(tel)
print(tel['guida'])
del tel['jack']
print(tel)
tel['ivy'] = 4439
print(tel)
print(list(tel))
print(sorted(tel))
print('Is ivy in tel?', 'ivy' in tel)
print('What about brendon?', 'brendon' in tel)
print('I hear sape is not in tel...:', 'sape' not in tel)
print()

# if you have a list of key-value pairs, use dict to create a dict
mylist = [('uno', 1), ('dos', 2), ('tres', 3), ('catorze', 14)]
print(mylist)
count = dict(mylist)
print(count)
print(count['catorze'])
print()

# but when keys are strings, it may be easier just to...
mylist = dict(uno=1, dos=2, tres=3, catorze=14)
print(mylist)
print()

# dicts also support comprehensions
squares = {x: x**2 for x in (3, 6, 9)}
print(squares)
print()

# looping
# when looping through dicts, key:value pairs can be obtained
# by using items()
knights = {
    'galahad': 'the doubtful',
    'robin': 'the fearful',
    'ionas': 'the zombie'
}

for name, title in knights.items():
    print(name, title)
print()

# when looping through a sequence, here's a way to obtain
# the index and the corresponding value
actions = ['ping', 'pong', 'pang!']
for idx, action in enumerate(actions):
    print(idx, action)
print()

# looping over 2 or more sequences at a time
questions = [
    'name',
    'quest',
    'favorite color'
]
answers = [
    'lancelot',
    'the holy grail',
    'bluish purplish reddish black',
]

for q, a in zip(questions, answers):
    print('What is your {0}? It is {1}.'.format(q, a))
print()

# how about in reverse?
for q, a in zip(reversed(questions), reversed(answers)):
    print('What is your {}? It is {}.'.format(q, a))
print()

# conditions
# in, not in: membership test
# is, is not: wether 2 objects are the same object
# <, >, <=, >=, ==, != 
# all of the above have the same priority
# and, or, not: not > and > or 
# so not a and b or c is the same as ((not a) and b) or c
# and, or are short-circuit operators
# when used on values other than Booleans, this is what happens
s1, s2, s3 = '', 'Trondheim', 'Hammer Dance'
result = s1 or s2 or s3
print(result)
print()

# it is possible to have assignments in expressions like in C,
# but we have to use :=
# while (name := input("State your name: ")):
#     if (name.lower() != 'q'):
#         print('Hello, {}!'.format(name))
#     else:
#         break

# comparing sequences:
# lexicographical ordering is used, in which the first item
# of sequence a is compared to the first item of sequence b
# and so on; if one comparison differ, then the sequences are not equal
# if 2 items being compared are themselves sequences of the same type
# the lexicographical ordering is again used, recursively
# the comparison goes until either sequence is exhausted
# the first to be exhausted is the smaller one

# NOTE: CHAPTER 7: MODULES
# through "import module_name", the contents of the respective module
# are added to the current namespace through the module name
# ("module_name", in this case, or any alias when using
# "import module_name as my_module")

# if you want to bring the module contents directly into the
# current namespace, you can use from module_name import name,
# or from module_name import name as my_name or
# from module_name import * (which will import all names except
# those beginning with _, but this is frowned upon except when
# in interactive mode, for it usually causes poorly readable code.

# when a module is imported, its code is executed. if you run the
# module as a script (e.g. python prime.py 101), its __name__ is
# set to "__main__". so if you use the following code in your module,
# it only gets executed as a script, not when importing it as a mudule,
# making it usable as both a script and an importable module:
# if __name__ == "__main__":
#     import sys
#     prime(int(sys.argv[1]))
# of course, if the called function takes no argument, then importing
# sys won't be necessary.

# module search path
# import a_module
# searches for a_module in sys.builtin_module_names
# if not found, searches for a_module.py in sys.path
# for more info, see PEP 3147

# to see a list of builtin functions and variables, 
# import builtins module

# from package import item
# item can be package, module, function, class, variable
# import item.subitem.subsubitem
# item and subitem must be packages and subsubitem must be
# a package or a module

# from package import item is the preferred choice, unless
# when there is the need to use "item" with the same name
# from different packages

# for intra-package references, "." and ".." can be used
# except in the main module

# NOTE: CHAPTER 8: In & Out
# see https://docs.python.org/3/library/string.html#formatstrings

first_name = 'Uklund'
last_name = 'Tuurvilsen'
print(f"My name is {first_name + ' ' + last_name}.")
print(f"My name is {first_name} {last_name}.")
print("My name is {} {}.".format(first_name, last_name))
print("My name is {} {}.".format(last_name, first_name))
print("My name is {0} {1}.".format(first_name, last_name))
print("My name is {1} {0}.".format(last_name, first_name))
print("My name is {first} {last}.".format(first=first_name, last=last_name))
print("My name is {0} {last}.".format(first_name, last=last_name))
print()

for x in range (1, 11):
    print('{0:2d} {1:3d} {2:4d}'.format(x, x*x, x*x*x))
print()

# for old string formatting, check
# https://docs.python.org/3/library/stdtypes.html#old-string-formatting

# for file handling, UTF-8 is the standard encoding
# and, remember: DBES - decode bytes, encode strings
# also, be aware of the encoding of some terminals:
# they don't work with UTF-8 (like Windows...)
# so, whenever possible, for maximum safety,
# use ASCII characters, mainly if the code is global

# it is better to use with clause with files, since
# it assures their closure; if with is not used,
# then file.close() must be invoked
with open("my_file.txt", encoding='utf-8') as file:
    read_data = file.read()
    print(read_data)
print(file.closed)
print()

# it's cool to iterate over the lines of an open file
with open("my_file.txt", mode='r', encoding='utf-8') as file:
    for line in file:
        print(line, end='')
print()

# if lines as a list is the way to go...
with open("my_file.txt", encoding='utf-8') as file:
    for line in file.readlines():
        print(line, end='')
print()

# end='' above means that each line already includes a \n from the file

# for writing, strings are ok; other objects need to be converted
# to a string or to a bytes obj
# (write returns the numbers of characters written)
with open("my_file.txt", mode='w', encoding='utf-8') as file:
    file.write('A string is fine.\n')
    file.write(str(('but this', 'must', 'b', 'converted', 4)))
    file.write('\n')
    file.write(str(['as', 'this', '.']))
    file.write('\n')

with open('my_file.txt', encoding='utf-8') as file:
    print('1st reading:')
    for line in file:
        print(line, end='')
    print('\n2nd reading:')
    file.seek(5, 0)
    for line in file:
        print(line, end='')
print()

with open('my_file.bin', mode='w+b') as file:
    file.write(b'0123456789abcdef')
    file.seek(5) # same as seek(5, 0)
    print(file.read(1))
    file.seek(-2, 1)
    print(file.read(2))
    file.seek(-3, 2)
    print(file.read(5))
print()

# using JSON
import json
data = (1, 'simple', 'piece of data')
print(json.dumps(data))
print()

with open('my_file.json', mode='w', encoding='utf-8') as file:
    json.dump(data, file)

with open('my_file.json', encoding='utf-8') as file:
    # as data was originally a tuple
    data = tuple(json.load(file))
    print(data)
    print()

# the simple serialization / deserialization above works well with
# tuples and lists and dicts, but it will require extra effort for
# arbitrary class instances

# NOTE: CHAPTER 9: ERRORS AND EXCEPTIONS

# while True:
#     try:
#         x = int(input('Please give me a number: '))
#         break
#     except ValueError:
#         print('Whoa! Not a number, pal. Try again.')

# while True:
#     try:
#         x = int(input('Please give me a number: '))
#         break
#     except ValueError:
#         print('Whoa! Not a number, pal. Try again.')
#     except:
#         print('Nice try! Try again.')

# can treat more than one exception
# except (RuntimeError, TypeError, NameError):

class A(Exception):
    pass

class B(A):
    pass

class C(B):
    pass

class D(C):
    pass

for cls in [A, B, C, D]:
    try:
        raise cls()
    except D:
        print('D')
    except C:
        print('C')
    # except B:
    #     print('B')
    except A:
        print('A')

print()

# if arguments to the exception are needed...
# (__str__ allows args to be printed directly,
# but may be overriden by subclasses)
try:
    raise Exception('spam', 'eggs')
except Exception as exception:
    print(type(exception))
    print(exception.args)
    print(exception)
    x, y = exception.args
    print('x = ', x)
    print('y = ', y)
print()

# BaseException is the mother of all, and its daughter Exception
# is the mother of all non-fatal exceptions; those which are not
# subclasses of Exception are unhandled

# it is a good practice to be as specific as possible with the type
# of exceptions that we intend to handle, and to allow any unexpected
# exceptions to propagate on

# the most common pattern for handling Exception is to print or log
# the exception and then re-raise it (allowing a caller to handle
# the exception as well)
import sys
try:
    # will raise OSError
    f = open('my_fil.txt', encoding='utf-8')
    # will raise ValueError
    # f = open('my_file.txt', encoding='utf-8')
    # will raise Exception
    # f = open('my_file.txt', encoding='utf-17')
    s = f.readline()
    i = int(s.strip())
except OSError as err:
    print('OS Error:', err)
except ValueError:
    print("Could not convert data to an integer.")
except Exception as err:
    print(f"Unexpected {err=}, {type(err)=}")
    raise
print()

# there is the else clause, for code that must be executed
# when the code in try runs successfully
for arg in sys.argv[1:]:
    try:
        f = open(arg, 'r', encoding='utf-8')
    except OSError:
        print('Cannot open', arg)
    else:
        print(arg, 'has', len(f.readlines()), 'lines.')
        f.close()
print()

# mind the exceptions raised by code run by functions invoked
# in your try clause...

# raise takes as argument either a subclass of BaseException or
# an exception instance; if a class is passed, its constructor
# will be implicitly called
try:
    raise ValueError
except ValueError:
    print('Some made up value error.\n')

# if you need to determine wether an exception was raised but do not
# intend to handle it, you can do this
# try:
#     raise NameError("I'm a name error!")
# except:
#     print("An exception was here...")
#     raise

# if an exception occurs during exception handling, it will be
# attached and printed in the current except clause
# try:
#     open('some_file.ext')
# except OSError:
#     raise RuntimeError('Oh boy!...')

# something useful for exception transformation
# def func():
#     raise ConnectionError

# try:
#     func()
# except ConnectionError as exc:
#     raise RuntimeError ('Cannot connect.') from exc

# but exception chaining can also be disabled
# try:
#     open('some_file')
# except OSError:
#     raise RuntimeError from None

# cleaning up:
# the finally clause always executes
# exceptions raised in try and not handled by any except
# will be re-raised after the finally block gets executed
# as will be the case when an exception occurs in an except
# but if finally contains break, continue or return,
# exceptions will not be re-reaised
# when try contains break, continue or return, finally will be
# excecuted just before it
# if both try and finally includes a return, the returned value
# will be that of the finally block

# whenever in the need to handle a group of exceptions
# (the type raised will be of ExceptionGroup)
# def f():
#     excs = [OSError('os problem 1'), SystemError('system problem 2')]
#     raise ExceptionGroup('some errors have occurred...', excs)

# f()

# this is how to treat some of the exceptions of a group
# def f():
#     raise ExceptionGroup(
#         "group 1",
#         [
#             OSError(1),
#             SystemError(2),
#             ExceptionGroup(
#                 "group 2",
#                 [
#                     OSError(3),
#                     RecursionError(4)
#                 ]
#             )
#         ]
#     )

# try:
#     f()
# except* OSError as e:
#     print("There were some OS errors...")
# except* SystemError as e:
#     print("There were some system errors...")

# of course, the exceptions in an exception group must be instances
# since in practice they are the ones already raised and caught
# by the program
# excs = []
# for test in tests:
#     try:
#         test.run()
#     except Exception as e:
#         excs.append(e)

# if excs:
#     raise ExceptionGroup("Test failures:", excs)

# whenever handling an exception, it is possible and useful to
# add notes to it, as needed
# def f():
#     raise OSError('Operation failed.')

# excs = []
# for i in range(3):
#     try:
#         f()
#     except Exception as e:
#         e.add_note(f'Happened in iteration {i+1}')
#         excs.append(e)

# raise ExceptionGroup('Oh no!', excs)

# NOTE: CHAPTER 10: CLASSES
