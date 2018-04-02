'''
# Strings
demoStr = "this is an example sentence for Python to manipulate."

print("")
print("Original String: ")
print(demoStr)
print("")

# capitalize
print("")
print("Capitalize: ")
print(demoStr.capitalize())
print("")

# upper
print("")
print("Upper: ")
print(demoStr.upper())
print("")

# lower
print("")
print("Lower: ")
print(demoStr.lower())
print("")

# count 
print("")
print("Count of 't': ")
print(demoStr.count("t"))
print("")

# find 
print("")
print("Find first occurence of 'a': ")
print(demoStr.find("a"))
print("")

# index 
print("")
print("Find first occurence of 'a' with index: ")
print(demoStr.index("a"))
print("")


# split 
print("")
print("Split string by spaces: ")
demoArr = demoStr.split(" ")
print(demoArr)
print("")

# join 
print("")
print("Re-join resulting array back to original string: ")
print(" ".join(demoArr))
print("")

# replace 
print("")
print("Insert the word 'Audrey' into the sentence: 'Hello [name]!: ")
print("Hello {}!".format("Audrey"))
print("")
'''


demoList =['chocolate', 7, 'Greg', 'Coding', 'ninja', 'Zanker', 5, 10]
demoint =[7, 5, 3, 2, 9, 40, 30]

#len
print("")
print("Find the length of the given list")
print(len(demoList))
print("")


#max
print("")
print("Find the max in the given list")
print(max(demoint))
print("")

#min
print("")
print("Find the min in the given list")
print(min(demoint))
print("")

#index
print("")
print("Find the lowest in the given list")
print(demoList.index("Coding"))
print("")

#append
print("")
print("add new object to our list")
demoList.append("Aman")
print(demoList)
print("")

#pop
print("")
print("POP object from list")
print(demoList.pop(3))
print(demoList)
print("")

#remove
print("")
print("remove object from list")
print(demoint.remove(2))
print(demoint)
print("")



#insert
print("")
print("add new object to our list")
demoList.pop(3)
print(demoList)
print("")







