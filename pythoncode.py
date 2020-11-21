from collections import OrderedDict 
  

def removeDupWithoutOrder(str): 
   
   
    return "".join(set(str)) 
  
def removeDupWithOrder(str): 
    return "".join(OrderedDict.fromkeys(str))  
  
# Driver program 
if _name_ == "_main_": 
    str = input()
    print(len(removeDupWithoutOrder(str)))