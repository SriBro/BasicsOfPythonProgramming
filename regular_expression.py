import re
#search(), finditer(), findall(), split(), sub()
#regular expression is used to find a particular match in a string

pattern="n"
pattern1 = r"[A-Z]+yclone"
text =  '''India, officially the Republic of India (ISO: Bhārat Gaṇarājya),[21] is a country in South Asia. It is the seventh-largest country by area; the most populous country as of Zyclone Tyclone June 2023;[22][23] and from the time of its independence in 1947, the world's most populous democracy.[24][25][26] Bounded by the Indian Ocean on the south, the Arabian Sea on the southwest, and the Bay of Bengal on the southeast, it shares land borders with Pakistan to the west;[j] China, Nepal, and Bhutan to the north; and Bangladesh and Myanmar to the east. In the Indian Ocean, India is in the vicinity of Sri Lanka and the Maldives; its Andaman and Nicobar Islands share a maritime border with Thailand, Myanmar, and Indonesia
'''

#search() is used to find whether a pattern exists or not for first occurence
match = re.search(pattern,text)
print(match)

#finditer
match1 = re.finditer(pattern1,text)
for amatch in match1:
    print(amatch)

#$ is for checking whether the specified string the ending or not
match2 = re.search("Indonesia$",text)
if match2:
    print("We have a match")
else:
    print("We dont have a match")

#$ is for checking whether the specified string the starting or not
match3 = re.search("^India",text)
if match3:
    print("Match successfull")
else:
    print("Match not successfull")

#findall() returns the a list containing all matches
match4 = re.findall("i",text)
for match in match4:
    print(match)

#split() the string at every whitespace character
match5 = re.split("\s",text)
print(match5)

#splits() the text into 3 parts 
match6 = re.split("\s",text,2)
print(match6)

#sub() replaces a given word with a specified word
match7 = re.sub("India","America",text)
print(match7)

#sub() used to replace the first three occurrences of i with x
match8 = re.sub("i","x",text,3)
print(match8)

#finditer() matches every character having a letter from  a to d
match9 = re.finditer("[a-d]",text)
for match in match9:
    print(match)

#\d matches [0-9]
match10 = re.finditer("\d",text)
for match in match10:
    print(match)

import re
#regular expression is used to find a particular match in a string

pattern="n"
pattern1 = r"[A-Z]+yclone"
text =  '''India, officially the Republic of India (ISO: Bhārat Gaṇarājya),[21] is a country in South Asia. It is the seventh-largest country by area; the most populous country as of Zyclone Tyclone June 2023;[22][23] and from the time of its independence in 1947, the world's most populous democracy.[24][25][26] Bounded by the Indian Ocean on the south, the Arabian Sea on the southwest, and the Bay of Bengal on the southeast, it shares land borders with Pakistan to the west;[j] China, Nepal, and Bhutan to the north; and Bangladesh and Myanmar to the east. In the Indian Ocean, India is in the vicinity of Sri Lanka and the Maldives; its Andaman and Nicobar Islands share a maritime border with Thailand, Myanmar, and Indonesia
'''

#search() is used to find whether a pattern exists or not for first occurence
match = re.search(pattern,text)
print(match)

#finditer
match1 = re.finditer(pattern1,text)
for amatch in match1:
    print(amatch)

#$ is for checking whether the specified string the ending or not
match2 = re.search("Indonesia$",text)
if match2:
    print("We have a match")
else:
    print("We dont have a match")

#$ is for checking whether the specified string the starting or not
match3 = re.search("^India",text)
if match3:
    print("Match successfull")
else:
    print("Match not successfull")

#findall() returns the a list containing all matches
match4 = re.findall("i",text)
for match in match4:
    print(match)

#split() the string at every whitespace character
match5 = re.split("\s",text)
print(match5)

#splits() the text into 3 parts 
match6 = re.split("\s",text,2)
print(match6)

#sub() replaces a given word with a specified word
match7 = re.sub("India","America",text)
print(match7)

#sub() used to replace the first three occurrences of i with x
match8 = re.sub("i","x",text,3)
print(match8)

#finditer() matches every character having a letter from  a to d
match9 = re.finditer("[a-d]",text)
for match in match9:
    print(match)

