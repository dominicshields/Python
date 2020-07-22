def countlet(text,dict):
    for c in text.lower():
        if c in dict:
            dict[c] += 1
        else:
            dict[c] = 1

dict = {}
#countlet("Speaking to the Guardian ahead of International Women’s Day, Valeur criticised large listed companies for not achieving diversity targets. She said: “Do we really think that’s difficult? It’s a lie. It’s not difficult.",dict)
countlet(input("Please enter a string"),dict)
keylist = dict.keys()
keylist.sort()
for key in keylist:
    print (key," = ", dict[key])
