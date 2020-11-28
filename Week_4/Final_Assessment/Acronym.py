stopwords = ['to', 'a', 'for', 'by', 'an', 'am', 'the', 'so', 'it', 'and', "The"]
org = "The organization for health, safety, and education"
split_org = org.split(" ")
print(split_org)
acro = ""
for word in split_org:
    if word not in stopwords:
        acro = acro + word[0].upper()
print(acro)