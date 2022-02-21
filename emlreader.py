from ast import IsNot
from operator import truediv
import os
import json

thislist = []
thisdict = {}
directory = './emlfiles'
start = 'Content-type: text/plain;'
end = 'html;'
linenum = 0
thisdict = {}
thislist = []
products = []
plaintext = []
splitp = []
productslist = [] 

def splitproducts(products3):
    productslist = []
    for p in products3:
        
        if products3.index(p) % 4 == 0:
            thisdict["quantity"] = p
        if products3.index(p) % 4 == 1:
            thisdict["price"] = p
        if products3.index(p) % 4 == 2:
            thisdict["description"] = p
        if products3.index(p) % 4 == 3:
            thisdict["name"] = p
            productslist.append(thisdict)
            thislist.append(productslist[0])
        productslist = []    
    print("length of productslist")
    print(len(productslist))
    
            
        
        


        
    
        
        

def getproduct(text, startnum):
    products2 = []
    for l in text[startnum + 1:]:

        products2.append(l)
        if "Subtotal" in l:
            print("removing")
            products2.remove(l)
            break
    print("length of products2")
    print(len(products2))
    splitproducts(products2)


        
    


def getproducts(text):
    productstart = 0

    for l in text:
          
        if "Due on" in l:

            productstart = text.index(l)
            break
        
    getproduct(text, productstart)
            
        
    





def grabtext(foo, num):
    plaintext = []
    for l in foo[num:]:
        

        plaintext.append(l)

        if end in l:

         
            break
    print("Length of plaintext")
    print(len(plaintext))
    getproducts(plaintext)
        

filenum = 0
for filename in os.listdir(directory):
    filenum += 1
    f = os.path.join(directory, filename)
    if os.path.isfile(f):
        with open(f, "r") as fh:
            print(filenum)
            print(filename)
            lines = fh.readlines()
            for l in lines:
                if start in l:
                    linenum = lines.index(l)

                grabtext(lines, linenum)
                break
json_object = json.dumps(thislist, indent = 2, default = str)
print(json_object)
            
#                print(l.rstrip())


