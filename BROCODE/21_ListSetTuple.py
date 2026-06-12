"""
collection = single "variable" useed to store multiple values.
list = [] ordered and changeable. Duplicates OK
set = {} unordered and immutable, but Add/Remove OK . No duplicates
tuble = () ordered and unchangeable. Duplicates OK. FASTER
"""
#                       LIST :-

fruits = ["apple" , "orange" , "banana" , "guvava"]

#to list the diff methods that are availabe in a collection use :-
print(dir(fruits))
"""
this is the terminal of the abve code in the termibnal:-
['__add__', '__class__', '__class_getitem__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getstate__', '__gt__', '__hash__', '__iadd__', '__imul__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__rmul__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']
"""
# for the description of all these methods use 
print(help(fruits))

"""
this code give the following output:-
class list(object)
 |  list(iterable=(), /)
 |
 |  Built-in mutable sequence.
 |
 |  If no argument is given, the constructor creates a new empty list.
 |  The argument must be an iterable if specified.
 |
 |  Methods defined here:
 |
 |  __add__(self, value, /)
 |      Return self+value.
 |
 |  __contains__(self, key, /)
 |      Return bool(key in self).
 |
 |  __delitem__(self, key, /)
 |      Delete self[key].
 |
 |  __eq__(self, value, /)
 |      Return self==value.
 |                                                                                                                                                                               
 |  __ge__(self, value, /)                                                                                                                                                       
 |      Return self>=value.                                                                                                                                                      
 |                                                                                                                                                                               
 |  __getitem__(self, index, /)                                                                                                                                                  
 |      Return self[index].                                                                                                                                                      
 |                                                                                                                                                                               
 |  __gt__(self, value, /)                                                                                                                                                       
 |      Return self>value.                                                                                                                                                       
 |                                                                                                                                                                               
 |  __iadd__(self, value, /)                                                                                                                                                     
 |      Implement self+=value.                                                                                                                                                   
 |                                                                                                                                                                               
 |  __imul__(self, value, /)                                                                                                                                                     
 |      Implement self*=value.                                                                                                                                                   
 |                                                                                                                                                                               
 |  __init__(self, /, *args, **kwargs)                                                                                                                                           
 |      Initialize self.  See help(type(self)) for accurate signature.                                                                                                           
 |                                                                                                                                                                               
 |  __iter__(self, /)                                                                                                                                                            
 |      Implement iter(self).                                                                                                                                                    
 |                                                                                                                                                                               
 |  __le__(self, value, /)                                                                                                                                                       
 |      Return self<=value.                                                                                                                                                      
 |                                                                                                                                                                               
 |  __len__(self, /)                                                                                                                                                             
 |      Return len(self).                                                                                                                                                        
 |                                                                                                                                                                               
 |  __lt__(self, value, /)                                                                                                                                                       
 |      Return self<value.                                                                                                                                                       
 |                                                                                                                                                                               
 |  __mul__(self, value, /)                                                                                                                                                      
 |      Return self*value.                                                                                                                                                       
 |                                                                                                                                                                               
 |  __ne__(self, value, /)                                                                                                                                                       
 |      Return self!=value.                                                                                                                                                      
 |                                                                                                                                                                               
 |  __repr__(self, /)                                                                                                                                                            
 |      Return repr(self).                                                                                                                                                       
 |                                                                                                                                                                               
 |  __reversed__(self, /)                                                                                                                                                        
 |      Return a reverse iterator over the list.                                                                                                                                 
 |                                                                                                                                                                               
 |  __rmul__(self, value, /)                                                                                                                                                     
 |      Return value*self.                                                                                                                                                       
 |                                                                                                                                                                               
 |  __setitem__(self, key, value, /)                                                                                                                                             
 |      Set self[key] to value.                                                                                                                                                  
 |                                                                                                                                                                               
 |  __sizeof__(self, /)                                                                                                                                                          
 |      Return the size of the list in memory, in bytes.                                                                                                                         
 |                                                                                                                                                                               
 |  append(self, object, /)                                                                                                                                                      
 |      Append object to the end of the list.                                                                                                                                    
 |                                                                                                                                                                               
 |  clear(self, /)                                                                                                                                                               
 |      Remove all items from list.                                                                                                                                              
 |                                                                                                                                                                               
 |  copy(self, /)                                                                                                                                                                
 |      Return a shallow copy of the list.                                                                                                                                       
 |                                                                                                                                                                               
 |  count(self, value, /)                                                                                                                                                        
 |      Return number of occurrences of value.                                                                                                                                   
 |                                                                                                                                                                               
 |  extend(self, iterable, /)                                                                                                                                                    
 |      Extend list by appending elements from the iterable.                                                                                                                     
 |                                                                                                                                                                               
 |  index(self, value, start=0, stop=9223372036854775807, /)                                                                                                                     
 |      Return first index of value.                                                                                                                                             
 |                                                                                                                                                                               
 |      Raises ValueError if the value is not present.                                                                                                                           
 |                                                                                                                                                                               
 |  insert(self, index, object, /)                                                                                                                                               
 |      Insert object before index.                                                                                                                                              
 |                                                                                                                                                                               
 |  pop(self, index=-1, /)                                                                                                                                                       
 |      Remove and return item at index (default last).                                                                                                                          
 |                                                                                                                                                                               
 |      Raises IndexError if list is empty or index is out of range.                                                                                                             
 |                                                                                                                                                                               
 |  remove(self, value, /)                                                                                                                                                       
 |      Remove first occurrence of value.                                                                                                                                        
 |                                                                                                                                                                               
 |      Raises ValueError if the value is not present.                                                                                                                           
 |                                                                                                                                                                               
 |  reverse(self, /)                                                                                                                                                             
 |      Reverse *IN PLACE*.                                                                                                                                                      
 |                                                                                                                                                                               
 |  sort(self, /, *, key=None, reverse=False)                                                                                                                                    
 |      Sort the list in ascending order and return None.                                                                                                                        
 |                                                                                                                                                                               
 |      The sort is in-place (i.e. the list itself is modified) and stable (i.e. the                                                                                             
 |      order of two equal elements is maintained).                                                                                                                              
 |                                                                                                                                                                               
 |      If a key function is given, apply it once to each list item and sort them,                                                                                               
 |      ascending or descending, according to their function values.                                                                                                             
 |                                                                                                                                                                               
 |      The reverse flag can be set to sort in descending order.                                                                                                                 
 |                                                                                                                                                                               
 |  ----------------------------------------------------------------------                                                                                                       
 |  Class methods defined here:                                                                                                                                                  
 |                                                                                                                                                                               
 |  __class_getitem__(object, /)                                                                                                                                                 
 |      See PEP 585                                                                                                                                                              
 |                                                                                                                                                                               
 |  ----------------------------------------------------------------------                                                                                                       
 |  Static methods defined here:                                                                                                                                                 
 |                                                                                                                                                                               
 |  __new__(*args, **kwargs)                                                                                                                                                     
 |      Create and return a new object.  See help(type) for accurate signature.                                                                                                  
 |                                                                                                                                                                               
 |  ----------------------------------------------------------------------                                                                                                       
 |  Data and other attributes defined here:                                                                                                                                      
 |                                                                                                                                                                               
 |  __hash__ = None
"""
print(fruits[0]) 
# {#basically u can use index operaters over here like step ::n, reverse : -1 ,etc.}



for fruit in fruits:
    print(fruit)
#general convention ke acc for loop mei x ki jagh singular use karte hai and jis range ya list ke elements ke sath deal kr rhe hai use plural.

print(len(fruits))
print("apple" in fruits)# boolean
fruit[0] = "pineapple" #we can replace a value using index.
fruits.append("pineapple") # add
fruits.insert(0, "pineapple")
fruits.sort() # alphabatical order
fruits.reverse()
fruits.clear()
print(fruits.index("apple"))
print(fruits.count("banana"))

