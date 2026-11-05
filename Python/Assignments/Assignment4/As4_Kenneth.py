# Problem 1 (2 points)
# Begin with: sentence = "The nickname of students at BYU is Cougars."
# Write the python code to place in a str variable named t the value:
# The nickname of students at BYUH is Seasiders.
# To do this, you must use the replace method to change BYU to BYUH and Cougar to Seasider.

print("Problem 1")

sentence = "The nickname of students at BYU is Cougars."
t = sentence.replace("BYU", "BYUH") and sentence.replace("Cougar", "Seasider")
print(t)

print("")
# Begin with: sentence = "The nickname of students at BYU is Cougars."
# Write the python code to place in a variable named c the count of the number of "s" characters found in sentence.
print("Problem 2")

print(t)
c = sentence.count("s")
print(c)

print("")
# Begin with: name = "put your name here"
# Write the python code using the upper method to place in a variable named upName the name found in name.
print("Problem 3")
name = "put your name here"
upName = name.upper()
print(upName)

print("")
# Begin with: sentence = "The brown dog."
# Write the python code using a variation of the strip method to place in a variable named
# stripped the value of sentence with only the trailing spaces removed. To get the correct
# space counts in sentence, copy the line from this document into your python code.
print("Problem 4")
sentence = " The brown dog. "
stripped = sentence.rstrip()
print(stripped)

print("")
# Begin with: sentence = "The purple cow."
# Write the python code using the find method to place in a variable named pos, the index
# position of "purple".
print("Problem 5")
sentence = "The purple cow."
pos = sentence.find("purple")
print(pos)

print("")
# Begin with:
# sentence = "The purple cow."
# Write the python code using string slicing to place in a variable named color, the word
# "purple". Note: You must use slicing of sentence to complete this problem.
print("Problem 6")
sentence = "The purple cow"
color = sentence[4:10]
print(color)

print("")
# Begin with: sentence = "The purple cow."
# Write the python code using string slicing to place in a variable named remainder,
# everything in sentence beginning from "purple" to the end of the variable sentence
print("Problem 7")
sentence = "The purple cow."
remainder = sentence[4:]
print(remainder)

print("")
# Begin with: word = "wisdom"
# Write the python code using string slicing to place in a variable named backwards, the
# characters in the variable word reversed.
print("Problem 8")
word = "wisdom"
backwards = word[::-1]
print(backwards)

print("")
# You will need to download the file BoM.txt from canvas. Store it on your computer drive 
# (for example, place in a folder named "C:\CS101"). Using the python interpreter 
# (do not use pyPDB.exe), begin by executing these two lines:
# with open('c:\\CS101\\BoM.txt', 'r', encoding='utf-8') as file:
# bom = file.read()
# This places the entire text of the Book of Mormom in the str variable bom. Note: You will
# need to change the file location in the "open" statement.
print("Problem 9")
# Write the python code to place in a variable named samCount, a count of the number of
# times the word Sam is found in bom.
with open('c:\\CS101\\BoM.txt', 'r', encoding='utf-8') as file:
    bom = file.read()
    samCount = bom.count("Sam")
    print(samCount)
    bom = file.close()

print("")
print("Problem 10")
# The Book of Alma starts at index position 538,993. The book of Helaman starts at position
# 1,004,127. Write the python code to place in a variable named almaCount, a count of the
# number of times the word Alma is found in the Book of Alma. Note: There is a line at the
# beginning of each chapter that says: "Alma Chapter 1", etc. Use python to determine how
# many chapters there are in the Book of Alma. Do not include the chapter heading lines in
# the almaCount.
with open('c:\\CS101\\BoM.txt', 'r', encoding='utf-8') as file:
    bom = file.read()
    almaCount = bom.count("Alma ")
    almaChapterCount = bom.count("Alma Chapter ")
    almaFinalCount = almaCount - almaChapterCount
    print(almaFinalCount)
    bom = file.close()

print("")
# Find the index position of the second time the name "Mosiah" is found in the Book of
# Mormon (bom). Hint: Find the first position, then do a find again starting at the position
# just after where the first was found
print("Problem 11")
with open('c:\\CS101\\BoM.txt', 'r', encoding='utf-8') as file:
    bom = file.read()
    pos = bom.find("Mosiah")
    pos2 = bom.find("Mosiah",pos + 1)
    print(pos2)
    bom = file.close()

# Write the python code to place in a variable named c the count of the number of "s" characters found in sentence.
