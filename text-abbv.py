import json

file = open('abbv.json', 'r')
abbreviations = json.loads(file.read())

print "What is the text?"
text = raw_input('> ')
words = text.split(' ')
for word in words:
    if word in abbreviations:
        print abbreviations.get(word, 'n/a')

    else:
        print "not found"

# print abbreviations
file.close()
