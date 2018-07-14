import copy

[n for n in dir(copy) if not n.startswith('_')]

copy.__all__

help(copy.copy)

print copy.copy.__doc__
