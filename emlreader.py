from ast import IsNot
from operator import truediv
import os
import json


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
invoice = ""

def splitproducts(products3):
    for p in products3:
        if products3.index(p) % 4 == 0:
            thisdict = {}
            thisdict["invoice number"] = invoice
            thisdict["quantity"] = p
        if products3.index(p) % 4 == 1:
            thisdict["price"] = p
        if products3.index(p) % 4 == 2:
            thisdict["description"] = p
        if products3.index(p) % 4 == 3:
            thisdict["name"] = p
            thislist.append(thisdict)
         
      
 
   
        
       
       

     
 
        
        

def getproduct(text, startnum):
    products2 = []
    removenextline = False
    for l in text[startnum + 1:]:
        products2.append(l)
        if removenextline == True:
            products2.remove(l)
            print("removing line")
            removenextline = False
        if len(l) == 76:
            removenextline = True
        if l == "FARROW WHOLESALER\n":
            products2.remove(l)
        
        if "Subtotal" in l:
            products2.remove(l)
            break
    
    splitproducts(products2)


        
    


def getproducts(text):
    productstart = 0

    for l in text:
          
        if "Terms" in l:

            productstart = text.index(l) + 1
            break
        
    getproduct(text, productstart)
            
        
    





def grabtext(foo, num):
    plaintext = []
    for l in foo[num:]:
        

        plaintext.append(l)

        if end in l:

         
            break
    getproducts(plaintext)
        

filenum = 0
for filename in os.listdir(directory):
    filenum += 1
    f = os.path.join(directory, filename)
    if os.path.isfile(f):
        with open(f, "r") as fh:
            print(filenum)
            invoice = filename
            lines = fh.read().splitlines()
            for l in lines:
                if start in l:
                    linenum = lines.index(l)
                    grabtext(lines, linenum)
                    break
json_object = json.dumps(thislist, indent = 2, default = str)
print(json_object)


