

import os, sys, inspect
from . import
classlist = []
for name, obj in inspect.getmembers(chain):
    if inspect.isclass(obj):
        classlist.append((name.lower(), obj))



print(classlist)