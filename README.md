# python-inventory-reconciliation
First project of python, used to parse xlxs files, and eml files to make sure financial books match real life
Goal: 
  Understand exactly what products are being bought and sold, and when, in order to maximize the profits by reducing the amount of products kept in inventory when unable to physically see what is in stock.
  
Steps required for project:
  First: Parse files of different types, xlxs and eml, to get the billed items in a common format in order to maniupulate data later.
  Second: Look at inventory movements and see where products are going, or if they are sitting on the shelf being unsold.
  Third: Make user interface to read important statistics in order to better understand how the products are moving.
  
xlsxreader.py: 
  This being my first ever python project and having no experience in Python or other interpreted languages, this code does not use functions, but does use a library openpyxl.
  It functions as a way to make dictionaries of each item that has been billed, then creates a JSON file to see results in a way that can be exported to different files or manipulated by other scripts later.
  
emlreader.py:
  This is more complicated than csv files as the eml files contain different formats within them. I decided to start using functions to make the readability of the code easier to help with debuging as well as changes needing to be made later. I am attemping to find the key words within every file that start the list of products that are needed to be stored in a JSON in order to move to the next step.
  This still does not function as intended but will be updated when debugging has been completed.
