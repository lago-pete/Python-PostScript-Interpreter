#Peter Lagonegro

from HW5_skeleton import *

opstack = []  
dictstack = []  

def opPop():
    if not opstack:
        print("stack is empty")
        return False
    else:
        print("successfully popped")
        return opstack.pop()
    

def opPush(value):
    opstack.append(value)
        
    
def dictPop():
    if not dictstack:
        print("dictionary empty bozo")
        return 0
    else:
        return dictstack.pop()
    

def dictPush(d):
    dictstack.append(d)
    

def define(name, value):
    if name is None or value is None:
        return False
    if not isinstance(name, str):
        return False
    temp = {name:value}
    dictPush(temp)
    
    
def lookup(name):
    if not isinstance(name, str):
        print("No name was entered")
        return False
    else:
        if name[0] != '/':
            name = '/' + name
        for dic in reversed(dictstack):
            if name in dic:
                return dic[name]
        print("Incorrect Name Entered")
        return False

    
def add():
    if len(opstack) < 2:
        print("Not enough Arguements")
        return False
    arg1 = opstack.pop()
    arg2 = opstack.pop()
    
    if isinstance(arg1, int):
       if isinstance(arg2, int):
           opstack.append(arg1+arg2)
           print("Successfully added")
           return
    if isinstance(arg1, float):
       if isinstance(arg2, float):
           opstack.append(arg1+arg2)
           print("Successfully added")
           return
    else:
        print("Incorrect type")
         
    opPush(arg2)
    opPush(arg1)
            
        
def sub():
    if len(opstack) < 2:
        print("Not enough Arguements")
        return False
    arg2 = opstack.pop()
    arg1 = opstack.pop()
    
    if isinstance(arg1, int):
       if isinstance(arg2, int):
           opstack.append(arg1-arg2)
           print("Successfully Subtracted")
           return
    if isinstance(arg1, float):
       if isinstance(arg2, float):
           opstack.append(arg1-arg2)
           print("Successfully Subtracted")
           return
    else:
        print("Incorrect type")
        
    opPush(arg2)
    opPush(arg1)
  

def mul():
    if len(opstack) < 2:
        print("Not enough Arguements")
        return False
    arg1 = opstack.pop()
    arg2 = opstack.pop()
    
    if isinstance(arg1, int):
       if isinstance(arg2, int):
           opstack.append(arg1*arg2)
           print("Successfully Multiplied")
           return
    if isinstance(arg1, float):
       if isinstance(arg2, float):
           opstack.append(arg1*arg2)
           print("Successfully Multiplied")
           return
    else:
        print("Incorrect type")
        
    opPush(arg2)
    opPush(arg1)
    

def div():
    
    if len(opstack) < 2:
        print("Not enough Arguements")
        return False
    arg2 = opstack.pop()
    arg1 = opstack.pop()
    
    if isinstance(arg1, int):
       if isinstance(arg2, int):
           opstack.append(arg1/arg2)
           print("Successfully Divided")
           return
    if isinstance(arg1, float):
       if isinstance(arg2, float):
           opstack.append(arg1/arg2)
           print("Successfully Divided")
           return
    else:
        print("Incorrect type")
        
    opPush(arg2)
    opPush(arg1)


def mod():
    
    if len(opstack) < 2:
        print("Not enough Arguements")
        return False
    arg2 = opstack.pop()
    arg1 = opstack.pop()
    
    if isinstance(arg1, int):
       if isinstance(arg2, int):
           opstack.append(arg1 % arg2)
           print("Successfully Modded")
           return
    if isinstance(arg1, float):
       if isinstance(arg2, float):
           opstack.append(arg1 % arg2)
           print("Successfully Modded")
           return
    else:
        print("Incorrect type")
        
        
    opPush(arg2)
    opPush(arg1)
    
    
def eq():
    if len(opstack) < 2:
        print("Not enough Arguements")
        return False
    arg1 = opstack.pop()
    arg2 = opstack.pop()
    
    if arg1 == arg2:
        print("They are Equal")
        opPush(True)
    else:
        opPush(False)
        return False
        

def lt():
    if len(opstack) < 2:
        print("Not enough Arguements")
        return False
    arg1 = opstack.pop()
    arg2 = opstack.pop()
    
    if arg1 > arg2:
        print("is Less then")
        opPush(True)
        
        return True
    else:
        opPush(False)
        return False
    
    
def gt():
    if len(opstack) < 2:
        print("Not enough Arguements")
        return False
    arg1 = opstack.pop()
    arg2 = opstack.pop()
    
    if arg1 < arg2:
        print("is Greater then")
        opPush(True)
        
    else:
        opPush(False)
        return False
  

def length():
    temp = opPop()
    if isinstance(temp, str):
        temp = len(temp)
        print("Length = ", temp - 2)
        opPush(temp - 2)
        return 
    else:
        print("Was not a String")
        return False
    
        
def get():
    temp = opPop()
    temp2 = opPop()
    if isinstance(temp2, str):
        temp2 = temp2.replace("(", "").replace(")", "")
        value = temp2[temp]
        value = ord(value)
        opPush(value)
        return True
    else:
        print("Was not a String")
        return False
    
    
def getinterval():
    num_char = opPop()
    start_index = opPop()
    
    temp = opPop()
    
    if isinstance(temp, str):
        temp = temp.replace("(", "").replace(")", "")
        str_split = temp[start_index: (start_index+num_char)]
        str_split = "(" +  str_split + ")"
        opPush(str_split)
        print("successful getInterval")
        return 
    else:
        print("Was not a String")
        opPush(temp)
        return False
    
    
def put():
    if len(opstack) >= 3:
        replace = opPop()
        index = opPop()
        og = opPop()  
        temp = og.replace("(", "").replace(")", "")
        
        if isinstance(temp, str) and isinstance(index, int) and 0 <= index < len(temp) and 0 <= replace <= 255:
            newChar = chr(replace)
            updated = temp[:index] + newChar + temp[index+1:]
            updated = "(" + updated + ")"
           
            for i in range(len(opstack)):
                if opstack[i] == temp:
                    opstack[i] = updated
           
            for d in dictstack:
                for key, value in d.items():
                    if value == og:
                        d[key] = updated
            opPush(updated)  
        else:
            print("Error: Invalid input")
            return False
    else:
        print("Error: Not enough items in the opstack")
        return False


def dup():
    if not opstack:
        print("Error: opstack is empty")
        return False
    temp1 = opPop()
    temp2 = temp1
    opPush(temp2)
    opPush(temp1)
    
    
def copy():
    count = opPop()
    copied = opstack[-count:]
    opstack.extend(copied)
        

def pop():
    return opPop()


def clear():
    opstack.clear()
    

def exch():
    if not opstack:
        print("Error: opstack is empty")
        return False
    temp1 = opPop()
    temp2 = opPop()
    opPush(temp1)
    opPush(temp2)


def roll():
    num_temp = opPop()
    move = opPop()
    
    
    temp_move = opstack.index(num_temp) + move
    opstack.remove(num_temp)
    
    if temp_move > len(opstack):
        opstack.append(num_temp)
    else:
        opstack.insert(temp_move, num_temp)
    
        
def stack():
    if not opstack:
        print("stack is empty")
        return False
    else:
        for temp in reversed(opstack):
            print(temp)
    
    
def psDict():
    if not opstack:
        return False
    else:
        temp = opstack.pop()
        temp_dic = {}
        opstack.append(temp_dic)
        
        
def begin():
    temp = opstack.pop()
    if isinstance(temp, dict):
        dictPush(temp)
    else:
        return False
    
    
def end():
    temp = dictstack.pop()
    if isinstance(temp, dict):
        return True
    

def psDef():
    temp_value = opstack.pop()
    temp_name = opstack.pop()
    
    if isinstance(temp_name, str):
        define(temp_name, temp_value)





# Copy this to your HW5.py file>
def interpreter(s): # s is a string
    interpretSPS(parse(tokenize(s)))
    
#Test Section -------------------------
    
def testPut():
    opPush("(This is a test _)")
    dup()
    opPush("/s")
    exch()
    psDef()
    dup()
    opPush(15)
    opPush(48)
    put()
    if lookup("s") != "(This is a test 0)" or opPop() != "(This is a test 0)":
        return False
    return True
    
    
 

#This is where i will test the functions
#print(testPut())

print(interpreter(input1))