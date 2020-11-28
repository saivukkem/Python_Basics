# coding=utf-8
# Write code that uses the string stored in sent and creates an acronym
# which is assigned to the variable acro. The first two letters of each word should be used,
# each letter in the acronym should be a capital letter,
# and each element of the acronym should be separated by a “. ” (dot and space).
# Words that should not be included in the acronym are stored in the list stopwords.
# For example, if sent was assigned the string “height and ewok wonder”
# then the resulting acronym should be “HE. EW. WO”.

stopwords = ['to', 'a', 'for', 'by', 'an', 'am', 'the', 'so', 'it', 'and', 'The']
sent = "The water earth and air are vital"
acro = ""
two_letters = []
sent_split = sent.split(" ")
print(sent_split)
for word in sent_split:
    if word not in stopwords:
        two_letters.append(word[0].upper() + word[1].upper())

for chars in two_letters:
    if chars != two_letters[-1]:
        acro = acro + chars + ". "
    else:
        acro = acro + chars
print(acro)
