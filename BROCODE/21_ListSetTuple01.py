"""
collection = single "variable" useed to store multiple values.
list = [] ordered and changeable. Duplicates OK
set = {} unordered and immutable, but Add/Remove OK . No duplicates
tuble = () ordered and unchangeable. Duplicates OK. FASTER
"""

#                    SET ; we can not use indexing over here

fruits = {"apple", "orange", "banana", "coconut"}

print(dir(fruits)) #"""['__and__', '__class__', '__class_getitem__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getstate__', '__gt__', '__hash__', '__iand__', '__init__', '__init_subclass__', '__ior__', '__isub__', '__iter__', '__ixor__', '__le__', '__len__', '__lt__', '__ne__', '__new__', '__or__', '__rand__', '__reduce__', '__reduce_ex__', '__repr__', '__ror__', '__rsub__', '__rxor__', '__setattr__', '__sizeof__', '__str__', '__sub__', '__subclasshook__', '__xor__', 'add', 'clear', 'copy', 'difference', 'difference_update', 'discard', 'intersection', 'intersection_update', 'isdisjoint', 'issubset', 'issuperset', 'pop', 'remove', 'symmetric_difference', 'symmetric_difference_update', 'union', 'update']"""
print(help(fruits))
"""
Help on set object:                                                                                                                                             

class set(object)
 |  set(iterable=(), /)
 |
 |  Build an unordered collection of unique elements.
 |
 |  Methods defined here:
 |
 |  __and__(self, value, /)
 |      Return self&value.
 |
 |  __contains__(self, object, /)
 |      x.__contains__(y) <==> y in x.
 |
 |  __eq__(self, value, /)
 |      Return self==value.
 |
 |  __ge__(self, value, /)
 |      Return self>=value.
 |
 |  __gt__(self, value, /)
 |      Return self>value.
 |                                                                                                                                                              
 |  __iand__(self, value, /)                                                                                                                                    
 |      Return self&=value.                                                                                                                                     
 |                                                                                                                                                              
 |  __init__(self, /, *args, **kwargs)                                                                                                                          
 |      Initialize self.  See help(type(self)) for accurate signature.                                                                                          
 |                                                                                                                                                              
 |  __ior__(self, value, /)                                                                                                                                     
 |      Return self|=value.                                                                                                                                     
 |                                                                                                                                                              
 |  __isub__(self, value, /)                                                                                                                                    
 |      Return self-=value.                                                                                                                                     
 |                                                                                                                                                              
 |  __iter__(self, /)                                                                                                                                           
 |      Implement iter(self).                                                                                                                                   
 |                                                                                                                                                              
 |  __ixor__(self, value, /)                                                                                                                                    
 |      Return self^=value.                                                                                                                                     
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
 |  __ne__(self, value, /)                                                                                                                                      
 |      Return self!=value.                                                                                                                                     
 |                                                                                                                                                              
 |  __or__(self, value, /)                                                                                                                                      
 |      Return self|value.                                                                                                                                      
 |                                                                                                                                                              
 |  __rand__(self, value, /)                                                                                                                                    
 |      Return value&self.                                                                                                                                      
 |                                                                                                                                                              
 |  __reduce__(self, /)                                                                                                                                         
 |      Return state information for pickling.                                                                                                                  
 |                                                                                                                                                              
 |  __repr__(self, /)                                                                                                                                           
 |      Return repr(self).                                                                                                                                      
 |                                                                                                                                                              
 |  __ror__(self, value, /)                                                                                                                                     
 |      Return value|self.                                                                                                                                      
 |                                                                                                                                                              
 |  __rsub__(self, value, /)                                                                                                                                    
 |      Return value-self.                                                                                                                                      
 |                                                                                                                                                              
 |  __rxor__(self, value, /)                                                                                                                                    
 |      Return value^self.                                                                                                                                      
 |                                                                                                                                                              
 |  __sizeof__(self, /)                                                                                                                                         
 |      S.__sizeof__() -> size of S in memory, in bytes.                                                                                                        
 |                                                                                                                                                              
 |  __sub__(self, value, /)                                                                                                                                     
 |      Return self-value.                                                                                                                                      
 |                                                                                                                                                              
 |  __xor__(self, value, /)                                                                                                                                     
 |      Return self^value.                                                                                                                                      
 |                                                                                                                                                              
 |  add(self, object, /)                                                                                                                                        
 |      Add an element to a set.                                                                                                                                
 |                                                                                                                                                              
 |      This has no effect if the element is already present.                                                                                                   
 |                                                                                                                                                              
 |  clear(self, /)                                                                                                                                              
 |      Remove all elements from this set.                                                                                                                      
 |                                                                                                                                                              
 |  copy(self, /)                                                                                                                                               
 |      Return a shallow copy of a set.                                                                                                                         
 |                                                                                                                                                              
 |  difference(self, /, *others)                                                                                                                                
 |      Return a new set with elements in the set that are not in the others.                                                                                   
 |                                                                                                                                                              
 |  difference_update(self, /, *others)                                                                                                                         
 |      Update the set, removing elements found in others.                                                                                                      
 |                                                                                                                                                              
 |  discard(self, object, /)                                                                                                                                    
 |      Remove an element from a set if it is a member.                                                                                                         
 |                                                                                                                                                              
 |      Unlike set.remove(), the discard() method does not raise                                                                                                
 |      an exception when an element is missing from the set.                                                                                                   
 |                                                                                                                                                              
 |  intersection(self, /, *others)                                                                                                                              
 |      Return a new set with elements common to the set and all others.                                                                                        
 |                                                                                                                                                              
 |  intersection_update(self, /, *others)                                                                                                                       
 |      Update the set, keeping only elements found in it and all others.                                                                                       
 |                                                                                                                                                              
 |  isdisjoint(self, other, /)                                                                                                                                  
 |      Return True if two sets have a null intersection.                                                                                                       
 |                                                                                                                                                              
 |  issubset(self, other, /)                                                                                                                                    
 |      Report whether another set contains this set.                                                                                                           
 |                                                                                                                                                              
 |  issuperset(self, other, /)                                                                                                                                  
 |      Report whether this set contains another set.                                                                                                           
 |                                                                                                                                                              
 |  pop(self, /)                                                                                                                                                
 |      Remove and return an arbitrary set element.                                                                                                             
 |                                                                                                                                                              
 |      Raises KeyError if the set is empty.                                                                                                                    
 |                                                                                                                                                              
 |  remove(self, object, /)                                                                                                                                     
 |      Remove an element from a set; it must be a member.                                                                                                      
 |                                                                                                                                                              
 |      If the element is not a member, raise a KeyError.                                                                                                       
 |                                                                                                                                                              
 |  symmetric_difference(self, other, /)                                                                                                                        
 |      Return a new set with elements in either the set or other but not both.                                                                                 
 |                                                                                                                                                              
 |  symmetric_difference_update(self, other, /)                                                                                                                 
 |      Update the set, keeping only elements found in either set, but not in both.                                                                             
 |                                                                                                                                                              
 |  union(self, /, *others)                                                                                                                                     
 |      Return a new set with elements from the set and all others.                                                                                             
 |                                                                                                                                                              
 |  update(self, /, *others)                                                                                                                                    
 |      Update the set, adding elements from all others.                                                                                                        
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
print(len(fruits))
print("pineapple" in fruits)
# we cannot change a element but we can add or remove though
fruits.add("pineapple") # adds a element
fruits.remove("apple") # removes a element
fruits.pop() # removes a element randomly
fruits.clear() # clear all