#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Given dictionaries, d1 and d2, create a new dictionary with the following property: for each entry (a, b) in d1, if a is not a key of d2 (i.e., not a in d2) then add (a,b) to the new dictionary for each entry (a, b) in d2, if a is not a key of d1 (i.e., not a in d1) then add (a,b) to the new dictionary
 For example, if d1 is {2:3, 8:19, 6:4, 5:12} and d2 is {2:5, 4:3, 3:9}, then the new dictionary should be {8:19, 6:4, 5:12, 4:3, 3:9}
 Associate the new dictionary with the variable d3
"""

def new_dict(dict1, dict2):
    newdict = {}
    newdict.update(dict1)
    newdict.update(dict2)
    d = newdict.copy()
    for i in d.iterkeys():
        if dict1.has_key(i) and dict2.has_key(i):
            newdict.pop(i)
    return newdict

def main():
    d1 = {2:3, 8:19, 6:4, 5:12}
    d2 = {2:5, 4:3, 3:9}
    print new_dict(d1, d2)

if __name__ == '__main__':
    main()
