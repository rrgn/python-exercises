from collections import Counter

file = raw_input("Pls. enter text filename: ")


def read():
    target = open(file, 'r')
    contents = target.read()
    contents = contents.replace(',', ' ').replace('.', ' ').replace('!', ' ').replace('?', ' ').replace('\n', ' ')
    print contents
    list = contents.split(' ')
    # dict = Counter(list)
    # print dict
    dict = {}
    for word in list:
        # alternative 1
        # if word in dict:
        #     count = dict[word]
        #     count = count + 1
        #     dict[word] = count
        # else:
        #     dict[word] = 1

        # alternative 2
        count = dict.get(word, 0)
        count = count + 1
        dict[word] = count

        entries = dict.items()

    entries.sort(key=lambda entry: entry[1], reverse=True)
    entries = entries[0:2]
    print entries

    target.close()

read()
