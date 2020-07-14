
string1 = 'hello'
print(string1)
print(string1[1])
#string1[1] = 'E' # Strings are immutable. This causes an error.
string2 = string1[0] + 'E' + string1[2] + string1[3] + string1[4]
print(string2)

print(string1.upper())
print(string2.lower())

string3 = string1.upper()
subStrings = string1.split()
print(subStrings)

string4 = 'This is line 1.\nThis is a new line after line 1.'
print(string4)