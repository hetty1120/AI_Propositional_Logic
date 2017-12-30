
# coding: utf-8

# In[186]:

# import class of Stack
from pythonds.basic import Stack


# In[187]:

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


# In[188]:

class sentence:
    
    def __init__(self,booexp):
        self.tree = None
        self.symbols = []
        self.words = booexp
    
    # represent sentence in parse tree
    def build_parse_tree(self):
        boolist = self.words.split()
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
            elif (i == "&" or i == "|" or i == "=>" or i == "<=>" ):
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
                if i not in self.symbols:
                    self.symbols.append(i)

        self.tree = p_tree


# In[189]:

def preorder(tree):
    # to check the tree
    if tree:
        print(tree.get_root_val())
        preorder(tree.get_left_child())
        preorder(tree.get_right_child())


# In[190]:

def evaluation(parse_tree,model):

    left_c = parse_tree.get_left_child()
    right_c = parse_tree.get_right_child()

    # consider the speical case that using "!" in boolean statement (unary operation)
    if parse_tree.get_root_val() == "!":
        return not evaluation(right_c,model)
    elif left_c and right_c:
        fn = parse_tree.get_root_val()
        if fn == "&":
            return evaluation(left_c,model) and evaluation(right_c,model)
        
        elif fn == "|":
            return evaluation(left_c,model) or evaluation(right_c,model)    
        
        # we can change "=>" and "<=>" to and/or which program can operate
        elif fn == "=>":
            return (not evaluation(left_c,model)) or evaluation(right_c,model)          
        
        elif fn == "<=>":
            return (((not evaluation(left_c,model)) or evaluation(right_c,model)) and 
                    ((not evaluation(right_c,model)) or evaluation(left_c,model)))
    
    else:
        return model[parse_tree.get_root_val()]


# In[191]:

def pl_true(sentence,model):
    
    # to check whether the model makes the sentence true
    for i in sentence:
        if evaluation(i.tree,model)==False:
            return False
    
    return True


# In[192]:

def tt_entails(KB,alpha):
    symbols_list = []
    
    # get all proposition symbols in order to assign values to them
    for i in KB:
        for j in i.symbols:
            if j not in symbols_list:
                symbols_list.append(j)
                
    return tt_check_all(KB,alpha,symbols_list,{})


# In[193]:

def tt_check_all(KB,alpha,symbols_list,model):
    if not symbols_list:
        if pl_true(KB,model):
            #print(model)
            return pl_true(alpha,model)
        else:
            # if KB is not true, it entails any sentence
            return True
    
    else:
        p = symbols_list[0]
        rest = symbols_list[1:]
        # assign True/False to every symbol in order to generate all possible models
        return tt_check_all(KB,alpha,rest,dict(model,**{p:True})) and tt_check_all(KB,alpha,rest,dict(model,**{p:False}))


# In[194]:

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
    s = sentence(get_s)
    s.build_parse_tree()
    alpha = [s]
    result1 = tt_entails(KB,alpha)
    s_negative = "( ! " + get_s + " )"
    s = sentence(s_negative)
    s.build_parse_tree()
    alpha = [s]
    result2 = tt_entails(KB,alpha)
    # check both alpha and !alpha
    if result1 != result2:
        print(result1)
    else:
        print("Can not tell") 
    get_s = input()


# In[ ]:



