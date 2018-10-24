import os

testFile = open("text.txt", "wb") # write binary

print(testFile.mode)
print(testFile.name)

testFile.write(bytes("Hello", "UTF-8"))
testFile.close()



testFile = open("text.txt", "r+")
print(testFile.read())
testFile.close()
os.remove("text.txt")