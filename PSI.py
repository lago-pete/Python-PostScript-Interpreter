#Peter Lagonegro



import re


opstack = []  
dictstack = []  




commands = ['opPop','opPush','dictPop','dictPush','define', 'lookup', 'add', 'sub', 'mul', 'div','mod','eq', 'lt', 'gt', 'length', 'get', 'getinterval', 'put', 'dup', 'exch', 'pop', 'copy', 'clear', 'stack','roll', 'dict', 'begin', 'end', 'def', 'if', 'ifelse', 'for']



def tokenize(s):
    return re.findall("/?[a-zA-Z()][a-zA-Z0-9_()]*|[-]?[0-9]+|[}{]+|%.*|[^ \t\n]", s)


# complete this function
# The it argument is an iterator.
# The sequence of return characters should represent a list of properly nested
# tokens, where the tokens between '{' and '}' is included as a sublist. If the
# parenteses in the input iterator is not properly nested, returns False.
def groupMatching2(it):
    res = []
    for c in it:
        if c == '}':
            return res
        elif c=='{':
            # Note how we use a recursive call to group the tokens inside the
            # inner matching parenthesis.
            # Once the recursive call returns the code array for the inner
            # paranthesis, it will be appended to the list we are constructing
            # as a whole.
            res.append(groupMatching2(it))
        elif c.isdigit():
            c = int(c)
            res.append(c)
        elif isinstance(c, str):
            if c == 'True':
                c = True
                res.append(c)
            elif c == 'False':
                c = False
                res.append(c)
            else:
                c = str(c)
                res.append(c)
        else:
            res.append(c)
    return False


# Complete this function
# Function to parse a list of tokens and arrange the tokens between { and } braces
# as code-arrays.
# Properly nested parentheses are arranged into a list of properly nested lists.
def parse(L):
    res = []
    it = iter(L)
    for c in it:
        if c=='}':  #non matching closing paranthesis; return false since there is
                    # a syntax error in the Postscript code.
            return False
        elif c=='{':
            res.append(groupMatching2(it))
            
        elif c.isdigit():
            c = int(c)
            res.append(c)
        elif isinstance(c, str):
            if c == 'True':
                c = True
                res.append(c)
            elif c == 'False':
                c = False
                res.append(c)
            else:
                c = str(c)
                res.append(c)
        else:
            res.append(c)
    return res


# Write the necessary code here; again write
# auxiliary functions if you need them. This will probably be the largest
# function of the whole project, but it will have a very regular and obvious
# structure if you've followed the plan of the assignment.
#


def interpretSPS(code):
    count = 0
    for token in code:
        count += 1
        if isinstance(token,str) and token.startswith('/') and isinstance(code[count],list):
            opPush(token)
            opPush(code.pop(count))
            continue
        if isinstance(token, list):  
            opPush(token)
        elif isinstance(token, str):
            if isinstance(token,str) and token.startswith('/'):
                opPush(token)
                continue
            if lookup(token):
                continue
            elif token in commands:
                commanding(token)
                continue
            else:
                opPush(token)
        else:
            opPush(token)
          
    


def commanding(token):
    if token in commands:
        if token == 'opPop':
            opPop()
            return 
        elif token == 'opPush':
            opPush()
            return
        elif token == 'dictPop':
            dictPop()
            return
        elif token == 'dictPush':
            dictPush()
            return
        elif token == 'define':
            define()
            return
        elif token == 'lookup':
            lookup()
            return
        elif token == 'add':
            add()
            return
        elif token == 'sub':
            sub()
            return
        elif token == 'mul':
            mul()
            return
        elif token == 'div':
            div()
            return
        elif token == 'mod':
            mod()
            return
        elif token == 'eq':
            eq()
            return
        elif token == 'lt':
            lt()
            return
        elif token == 'gt':
            gt()
            return
        elif token == 'length':
            length()
            return
        elif token == 'get':
            get()
            return
        elif token == 'getinterval':
            getinterval()
            return
        elif token == 'put':
            put()
            return
        elif token == 'dup':
            dup()
            return
        elif token == 'exch':
            exch()
            return
        elif token == 'pop':
            pop()
            return
        elif token == 'copy':
            copy()
            return
        elif token == 'clear':
            clear()
            return
        elif token == 'stack':
            stack()
            return
        elif token == 'roll':
            roll()
            return
        elif token == 'dict':
            psDict()
            return
        elif token == 'begin':
            begin()
            return
        elif token == 'end':
            end()
            return
        elif token == 'def':
            psDef()
            return
        elif token == 'if':
            psIf()
            return
        elif token == 'ifelse':
            psIfelse()
            return
        elif token == 'for':
            psFor()
            return



#-------------------------Helper Functions------------------------------------      
            
            
def psIf():
    block = opPop()
    condition = opPop()
    if condition:
        interpretSPS(block)

def psIfelse():
    false_block = opPop() 
    
    true_block = opPop()
    
    condition = opPop()
    
    if condition:
        interpretSPS(true_block)
    else:
        interpretSPS(false_block)

def psFor():
    block = opPop()  
    end = int(opPop())  
    
    increment = int(opPop())      
    start = int(opPop())  
    

    for i in range(start, end-1 , increment):
        opPush(i)
        interpretSPS(block)





#testing
input1 = """
        /square {
               dup mul
        } def
        (square)
        4 square
        dup 16 eq
        {(pass)} {(fail)} ifelse
        stack
        """

input2 ="""
    (facto) dup length /n exch def
    /fact {
        0 dict begin
           /n exch def
           n 2 lt
           { 1}
           {n 1 sub fact n mul }
           ifelse
        end
    } def
    n fact stack
    """

input3 = """
        /fact{
        0 dict
                begin
                        /n exch def
                        1
                        n -1 1 {mul} for
                end
        } def
        6
        fact
        stack
    """

input4 = """
        /lt6 { 6 lt } def
        1 2 3 4 5 6 4 -3 roll
        dup dup lt6 {mul mul mul} if
        stack
        clear
    """

input5 = """
        (CptS355_HW5) 4 3 getinterval
        (355) eq
        {(You_are_in_CptS355)} if
         stack
        """

input6 = """
        /pow2 {/n exch def
               (pow2_of_n_is) dup 8 n 48 add put
                1 n -1 1 {pop 2 mul} for
              } def
        (Calculating_pow2_of_9) dup 20 get 48 sub pow2
        stack
        """
   















#------------------------------------------------------------------------------


def opPop():
    if not opstack:
        return False
    else:
        return opstack.pop()
    

def opPush(value):
    opstack.append(value)
        
    
def dictPop():
    if not dictstack:
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
        return False
    else:
        if name[0] != '/':
            name = '/' + name
        for dic in reversed(dictstack):
            if name in dic:
                if isinstance(dic[name], list):
                    temp = dic[name].copy()
                    interpretSPS(temp)
                    return True 
                else:
                    temp = [dic[name]]
                    interpretSPS(temp)
                    return True
                   
        
        return False

    
def add():
    if len(opstack) < 2:
        
        return False
    arg1 = opstack.pop()
    arg2 = opstack.pop()
    
    if isinstance(arg1, int):
       if isinstance(arg2, int):
           opstack.append(arg1+arg2)
          
           return
    if isinstance(arg1, float):
       if isinstance(arg2, float):
           opstack.append(arg1+arg2)
           
           return
    
       
         
    opPush(arg2)
    opPush(arg1)
            
        
def sub():
    if len(opstack) < 2:
        return False
    arg2 = opstack.pop()
    arg1 = opstack.pop()
    
    if isinstance(arg1, int):
       if isinstance(arg2, int):
           opstack.append(arg1-arg2)
           return
    if isinstance(arg1, float):
       if isinstance(arg2, float):
           opstack.append(arg1-arg2)
           return
    
        
    opPush(arg2)
    opPush(arg1)
  

def mul():
    if len(opstack) < 2:
        return False
    arg1 = opstack.pop()
    arg2 = opstack.pop()
    
    if isinstance(arg1, int):
       if isinstance(arg2, int):
           opstack.append(arg1*arg2)
           return
    if isinstance(arg1, float):
       if isinstance(arg2, float):
           opstack.append(arg1*arg2)
           return
    
        
    opPush(arg2)
    opPush(arg1)
    

def div():
    
    if len(opstack) < 2:
        return False
    arg2 = opstack.pop()
    arg1 = opstack.pop()
    
    if isinstance(arg1, int):
       if isinstance(arg2, int):
           opstack.append(arg1/arg2)
           return
    if isinstance(arg1, float):
       if isinstance(arg2, float):
           opstack.append(arg1/arg2)
           return
    
        
    opPush(arg2)
    opPush(arg1)


def mod():
    
    if len(opstack) < 2:
        return False
    arg2 = opstack.pop()
    arg1 = opstack.pop()
    
    if isinstance(arg1, int):
       if isinstance(arg2, int):
           opstack.append(arg1 % arg2)
           return
    if isinstance(arg1, float):
       if isinstance(arg2, float):
           opstack.append(arg1 % arg2)
           return
          
        
    opPush(arg2)
    opPush(arg1)
    
    
def eq():
    if len(opstack) < 2:
        
        return False
    arg1 = opstack.pop()
    arg2 = opstack.pop()
    
    if arg1 == arg2:
        
        opPush(True)
    else:
        opPush(False)
        return False
        

def lt():
    if len(opstack) < 2:
       
        return False
    arg1 = opstack.pop()
    arg2 = opstack.pop()
    
    if arg1 > arg2:
        opPush(True)
        
        return True
    else:
        opPush(False)
        return False
    
    
def gt():
    if len(opstack) < 2:
        return False
    arg1 = opstack.pop()
    arg2 = opstack.pop()
    
    if arg1 < arg2:
        opPush(True)
        
    else:
        opPush(False)
        return False
  

def length():
    temp = opPop()
    if isinstance(temp, str):
        temp = len(temp)
        opPush(temp - 2)
        return 
    else:
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
        
        return 
    else:
        
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
                if opstack[i] == og:
                    del opstack[i]
           
            for d in dictstack:
                for key, value in d.items():
                    if value == og:
                        d[key] = updated
            opPush(updated)  
        else:
            print
            return False
    else:
        print
        return False


def dup():
    if not opstack:
        
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
    dictstack.clear()
    

def exch():
    if not opstack:
        
        return False
    temp1 = opPop()
    temp2 = opPop()
    opPush(temp1)
    opPush(temp2)


def roll():
    x = int(opPop())  
    y = int(opPop())  

    if y > len(opstack):
        return False
    x = x % y if x > 0 else -(-x % y)
    temp = opstack[-y:]

    if x > 0: 
        temp = temp[-x:] + temp[:-x]
    else:  
        x = -x 
        temp = temp[x:] + temp[:x]
    opstack[-y:] = temp


    
        
def stack():
    if not opstack:
        
        return False
    else:
        for temp in reversed(opstack):
            print(temp)
    
    
def psDict():
    if len(opstack) > 0:
        opPop()
        opPush({})
    else:
        return False
    
    
def begin():
    if len(opstack) > 0:
        temp = opPop()
        
        
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





#--------------------------Runner----------------------------------------------
def interpreter(s): # s is a string
    interpretSPS(parse(tokenize(s)))
    clear()
    




#---------------------------------Testing---------------------------------------
#print(tokenize(input2))
#print(parse(tokenize(input2)))



#interpreter(input1)
#clear()
#interpreter(input2)
#clear()
#interpreter(input3)
#clear()
#interpreter(input4)
#clear()
#interpreter(input5)
#clear()
#interpreter(input6)


