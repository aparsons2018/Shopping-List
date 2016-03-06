#Austin Parsons
#2/24/16
import os
fileName = input("enter the file name: ")
if os.path.isfile(fileName):
	f = open(fileName, 'r+')
	f.truncate()
	f.seek(0)
	shoppingList = f.read()
	shoppingList = f.splitlines()
else:
	print("That file does not exist. A file called shoppingList.txt was created. ")
	f = open("shoppingList.txt", "w")
	shoppingList = []
grocery = "start shopping"
while grocery != "":
	if len(shoppingList) == 0:
		print("Your List is empty. Press enter to quit. Or add an item.")
		grocery = input("Add an item: ")
		shoppingList.append(grocery)
	else:
		print("your shopping List contains: ")
		numberItem = 0
		for item in shoppingList:
			numberItem += 1
			print(numberItem + " " + item + " ")
			grocery = input("Add an item: ")
			shoppingList.append(grocery)
f.close()
exit()