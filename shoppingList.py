#Austin Parsons
#2/24/16
import os
fileName = input("enter the file name: ")
if os.path.isfile(fileName):
	f = open(fileName, 'r+')
		#truncate when you are done with the list.
	shoppingList = f.read().splitlines()
else:
	print("That file does not exist. A file called shoppingList.txt was created. ")
	f = open("shoppingList.txt", "w")
	shoppingList = []

grocery = None 
while grocery != "":
	if len(shoppingList) == 0:
		print("Your List is empty. Press enter to quit. Or add an item.")
	else:
		print("your shopping List contains: ")
		numberItem = 0
		for grocery in shoppingList:
			numberItem += 1
			print("{}. {}".format(numberItem, grocery)) 
	grocery = input("Add an item: ")
	if grocery != "":
		shoppingList.append(grocery)
f.seek(0)
f.truncate()	
for grocery in shoppingList:
	f.write(grocery + '\n')
f.close()
exit()
