# numbers
1           # integers
2.3         # floating point
3i          # imaginary
0b10101     # binary
0o237       # octal
0xFF        # hexadecimal


# strings
'hello'     # single line string
"hello"     # single line string
'''hello''' # multi-line string
"""hello""" # multi-line string
r'hello'    # raw string (can use backslashes)
r"hello"    # raw string (can use backslashes)


# lists: store a list of data.
[]          # Empty list     
[1]         # List with 1 value
[1,2,3]     # List with 3 value
list()      # Empty list
list([])    # Empty list (from another empty list)
list([1])   # Empty list (from another list)
len([])     # length of an empty list (0)


# tuples: store data in a list that can't change.
()          # Empty tuple
(1,)        # Tuple with 1 value (trailing comma required)
(1,2,3,)    # Tuple with 3 values (trailing comma optional)
tuple()     # Empty tuple  
tuple([])   # Empty tuple (from an empty list)
tuple([1])  # Tuple with 1 value (from a list)
len(())     # length of an empty tuple (0)


# dicts: store data using a unique key for each piece of data.
{}          # Empty dictionary
{'a':1}     # dictionary with 1 key/value
{'a':1,     # dictionary with 2 key/values
 'b':2}
dict()      # Empty dictionary
dict(       # dictionary with 2 key/values
  a=1,
  b=2)
len({})     # length of an empty dictionary (0)


# sets: store a unique set of data.
set()       # Empty set
set([1,2])  # Set of 2 values (from a list)
set([1,1])  # Set of 1 values (from a list)
len(set())  # length of an empty set (0)


# frozensets: store a unique set of data that can't change.
frozenset()       # Empty set
frozenset([1,2])  # Set of 2 values (from a list)
frozenset([1,1])  # Set of 1 values (from a list)
len(frozenset())  # length of an empty set (0)
