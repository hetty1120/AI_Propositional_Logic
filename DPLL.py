
# coding: utf-8

# In[1]:

# import class of Stack
from pythonds.basic import Stack


# In[2]:

class BinaryTree:
    
    def __init__(self, root_val):
        self.key = root_val
        self.left_child = None
        self.right_child = None
        
    def insert_left(self, new_val):
        if self.left_child == None:
            self.left_child = BinaryTree(new_val)
        else:
            t = BinaryTree(new_val)
            t.left_child = self.left_child
            self.left_child = t
            
    def insert_right(self, new_val):
        if self.right_child == None:
            self.right_child = BinaryTree(new_val)
        else:
            t = BinaryTree(new_val)
            t.right_child = self.right_child
            self.right_child = t
            
    def get_right_child(self):
        return self.right_child
    
    def get_left_child(self):
        return self.left_child
    
    def set_root_val(self, obj):
        self.key = obj
        
    def get_root_val(self):
        return self.key


# In[3]:

class sentence:
    
    # clause will only have "!" or "|"
    
    def __init__(self,booexp):
        self.tree = None
        self.symbols = {}
        self.value = booexp
    
    
    def build_parse_tree(self):
        boolist = self.value.split()
        for i in range(len(boolist)):
            a_char = boolist[i]
            if a_char not in ['('," ",')','|','!']:
                if a_char not in self.symbols:
                    if boolist[i-1] != '!':
                        self.symbols[a_char] = 1     #means positive
                    elif boolist[i-1] == '!':
                        self.symbols[a_char] = 2     #means negative
                    
        p_stack = Stack()
        p_tree = BinaryTree("")
        p_stack.push(p_tree)
        current_tree = p_tree

        for i in boolist:
            if i == "(":
                current_tree.insert_left("")
                p_stack.push(current_tree)
                current_tree = current_tree.get_left_child()
            elif i == " ":
                pass
            elif (i == "|"):
                current_tree.set_root_val(i)
                current_tree.insert_right("")
                p_stack.push(current_tree)
                current_tree = current_tree.get_right_child()
            elif i == "!":
                current_tree = p_stack.pop()
                current_tree.set_root_val(i)
                current_tree.insert_right("")
                p_stack.push(current_tree)
                current_tree=current_tree.get_right_child()
            elif i == ")":
                current_tree = p_stack.pop()
            else:
                current_tree.set_root_val(i)
                parent = p_stack.pop()
                current_tree = parent

        self.tree = p_tree


# In[4]:

def preorder(tree):
    if tree:
        print(tree.get_root_val())
        preorder(tree.get_left_child())
        preorder(tree.get_right_child())


# In[5]:

def evaluation(parse_tree,model):
    
    # reconsutrcut code here

    left_c = parse_tree.get_left_child()
    right_c = parse_tree.get_right_child()

    # consider the speical case that using "not" in boolean statement
    if parse_tree.get_root_val() == "!":
        if evaluation(right_c,model) == None:
            return None
        else:
            return not evaluation(right_c,model)
    elif left_c and right_c:
        op = parse_tree.get_root_val()
        if op == "&":
            return evaluation(left_c,model) and evaluation(right_c,model)
        else:
            left_result = evaluation(left_c,model)
            right_result = evaluation(right_c,model)
            if ((left_result == None and right_result == False) or 
                (left_result == False and right_result == None)):
                    return None
            else:
                return left_result or right_result
    else:
        if parse_tree.get_root_val() not in model:
            return None
        else:
            #get_val = parse_tree.get_root_val()
            #print(get_val,model[parse_tree.get_root_val()])
            return model[parse_tree.get_root_val()]


# In[6]:

def pl_true(clause,model):
    
    return evaluation(clause.tree,model)


# In[7]:

def satisfactory(KB):
    
    # return true means the function find a satisfible condition, which means that k=>a is not right 
    # return False means the KB is unsatisfiable, which means that k=>a is right
    
    total_symbols = []
    for clause in KB:
        for key in clause.symbols:
            if key not in total_symbols:
                total_symbols.append(key)
    
    return dpll(KB,total_symbols,{})


# In[8]:

def dpll(KB,total_symbols,model):
    
    unknown_clause = []
    
    # evaluate model by checking the value of each clause, if there is a False, then just return False
    for c in KB:
        result = pl_true(c,model)
        if result == False:
            return False
        if result != True:
            unknown_clause.append(c)
    if len(unknown_clause) == 0:
        return True
    
    # to find pure symbol
    p,value = find_pure_symbol(total_symbols,unknown_clause)
    if p:
        # use extend to construct new list without changing original one
        new_total_symbols = []
        new_total_symbols.extend(total_symbols)
        new_total_symbols.remove(p)
        return dpll(KB,new_total_symbols,dict(model,**{p:value}))
    
    # to find a unit clause
    p,value = find_unit_clause(total_symbols,unknown_clause)
    if p:
        new_total_symbols = []
        new_total_symbols.extend(total_symbols)
        new_total_symbols.remove(p)
        return dpll(KB,new_total_symbols,dict(model,**{p:value}))
    
    # try normal search
    p = total_symbols.pop()
    return (dpll(KB,total_symbols,dict(model,**{p:True})) or 
                dpll(KB,total_symbols,dic(model,**{p:False})))
    


# In[9]:

def find_pure_symbol(total_symbols,clause):
    for p in total_symbols:
        find_true, find_false = False, False
        for c in clause:
            if p in c.symbols:
                if not find_true and c.symbols[p] == 1:
                    find_true = True
                if not find_false and c.symbols[p] == 2:
                    find_false = True
        if find_true != find_false:
            return p, find_true
        
    return None,None


# In[10]:

def find_unit_clause(total_symbols,clause):
    
    for c in clause:
        find_symbols = 0
        for symbol in c.symbols:
            if symbol in total_symbols:
                find_symbols += 1
                if c.symbols[symbol] == 1:
                    p = symbol
                    val = True
                else:
                    p = symbol
                    val = False
        if find_symbols == 1:
            return p,val
    return None,None


# In[11]:

# main function to get input and present the result
s_number = int(input("How many sentences in knowledge base do you want to type: "))
KB = []
for i in range(s_number):
    get_s = input()
    s = sentence(get_s)
    s.build_parse_tree()
    KB.append(s)
print("Please type a sentence to check: ")
get_s = input()
while get_s != "END":
    s_negative = "( ! " + get_s + " )"
    s = sentence(s_negative)
    s.build_parse_tree()
    KB.append(s)
    result1 = satisfactory(KB)
    KB.pop()
    
    s = sentence(get_s)
    s.build_parse_tree()
    KB.append(s)
    result2 = satisfactory(KB)
    KB.pop()
    
    # check both sentence and !sentence
    if result1 != result2:
        print(result2)
    else:
        print("Can not tell") 
    get_s = input()

