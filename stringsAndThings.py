# strings
#  data that falls within" " marks

# Concatenation
# Put 2 or more strings together

firstname = "Fred"
lastname = "Flintstone"

fullname = firstname + " " + lastname

print(fullname)

# Repetition
# repetition operator: *

print("Hip "*2+ "Hooray!")

def rowyourboat():
    print("Row, "*3 + 'your boat')
    print("Gently down the stream")
    print("Merrily, "*4)
    print("Life is but a dream")

rowyourboat()

# Indexing

name = "Roy G Biv"
firstChar = name[0]
print(firstChar)
middleIndex = len(name) // 2
print(middleIndex)
print(name[middleIndex])


print(name[-1])

for i in range(len(name)):
    print(name[i])

# slicing and dicing
# slicing operator: :
# slicing lets us make substrings

print(name[0:3])
print(name[:5])
print(name[6:9])
print(name[6:])

for i in range(1, len(name)+1):
    print(name[0:i])
