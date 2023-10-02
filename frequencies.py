"""Frequencies function."""
"""ENTER YOUR SOLUTION HERE!"""

def frequencies(items):
    frequencies = {}
    for item in items:
        if isinstance(items,str):
            key = item 
        else:
            key = str(item)
        
        if key in frequencies:
            frequencies[key] += 1 
        else:
            frequencies[key] = 1

    return frequencies

#Test cases 
print(frequencies(['a','a','b','b','c']))
print(frequencies([100,'Hello','100','100',100]))