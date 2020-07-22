piratedict = {"are":"be",
"boy":"matey",
"excuse":"arr",
"hello":"avast",
"hotel":"fleabag inn",
"is":"be",
"lawyer":"foul blaggart",
"madam":"proud beauty",
"man":"matey",
"my":"me",
"professor":"foul blaggart",
"restaurant":"galley",
"restroom":"head",
"sir":"matey",
"student":"swabbie",
"students":"swabbies",
"the":"th’",
"your":"yer"}

sentence = input("Please enter a sentence")
words = sentence.split(" ")
translated = ""
for x in words:
    if x in piratedict:    
        translated += " " + piratedict[x]
    else:
         translated += " " + x

print(translated)