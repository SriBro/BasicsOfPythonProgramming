#\d,\D,\s,\S,\w,\W
import re 

text = '''India, officially the Republic of India (ISO: Bhārat Gaṇarājya),[21] is a country in South Asia. It is the seventh-largest country by area; the most populous country as of Zyclone Tyclone June 2023;[22][23] and from the time of its independence in 1947, the world's most populous democracy.[24][25][26] Bounded by the Indian Ocean on the south, the Arabian Sea on the southwest, and the Bay of Bengal on the southeast, it shares land borders with Pakistan to the west;[j] China, Nepal, and Bhutan to the north; and Bangladesh and Myanmar to the east. In the Indian Ocean, India is in the vicinity of Sri Lanka and the Maldives; its Andaman and Nicobar Islands share a maritime border with Thailand, Myanmar, and Indonesia'''

#\D matches every charcter except [0-9]
match12 = re.finditer("\D",text)
for match in match12:
    print(match)
print("\n\n\n\n\n\n\n\n")
#\s matches any whitespace character
match13 = re.finditer("\s",text)
for match in match13:
    print(match)
print("\n\n\n\n\n\n\n\n")
#\S matches non-whitespace characters
match14 = re.finditer("\S",text)
for match in match14:
    print(match)
print("\n\n\n\n\n\n\n\n")
#\w matches alpha-numeric characters (a-z,A-Z,0-9)
match15 = re.finditer("\w",text)
for match in match15:
    print(match)
print("\n\n\n\n\n\n\n\n")
#\W matches non alpha-numeric characters 
match16 = re.finditer("\W",text)
for match in match16:
    print(match)