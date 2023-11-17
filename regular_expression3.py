# . * +
import re  

text = '''India, officially the Republic of India (ISO: Bhārat Gaṇarājya),[21] is a country in South Asia. It is the seventh-largest country by area; the most populous country as of Zyclone Tyclone June 2023;[22][23] and from the time of its independence in 1947, the world's most populous democracy.[24][25][26] Bounded by the Indian Ocean on the south, the Arabian Sea on the southwest, and the Bay of Bengal on the southeast, it shares land borders with Pakistan to the west;[j] China, Nepal, and Bhutan to the north; and Bangladesh and Myanmar to the east. In the Indian Ocean, India is in the vicinity of Sri Lanka and the Maldives; its Andaman and Nicobar Islands share a maritime border with Thailand, Myanmar, and Indonesia M'''

# . matches any word that has any two arbitary letters and that ends with s
match16 = re.finditer("..s",text)
for match in match16:
    print(match)

# * matches all words with zero or more occurrences of the preeceding character
#Here we match all words that start with M
match17 = re.findall(r"M\w*",text)
for match in match17:
    print(match)

# + matches all words with zero or more occurrences of the preeceding character
#Here we match all words that start with M
match18 = re.findall(r"M\w+",text)
for match in match18:
    print(match)


