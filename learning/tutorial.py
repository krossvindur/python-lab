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
print("COMMAND ME, MASTER:")
command = input("> ")
exits = ["back", "forth", "forward", "backwards"]

match command.split():
    # *_ can be used, if binding is not wanted
    case ["drop", *objects]:
        print("\nYou drop:")
        for obj in objects:
            print(obj)
        print("And then you fall. Forever.")
    case ["run", "fast"]:
        print("\nYou run fast. And then you fall. Forever.")
    case ["run", "slowly"]:
        print("\nYou run slowly. You keep running slowly. " 
              "And then you fall. Forever.")
    case ["go", ("north" | "south" | "east" | "west") as direction]:
        print(f"\nYou go {direction}. And then you fall. Forever.")
    case ["go", direction] if direction in exits:
        print(f"\nYou try to go {direction}. And then you fall. "
              "Forever.")
    case ["help"]:
        print('\nYou cry for help. And then you fall. Forever.')
    case _:
        print("\nYou just fall. Forever.")
print("")

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

