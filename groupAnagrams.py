def groupAnagrams(strs):
    temp_dict = {}
    for word in strs:
        key = tuple(sorted(word))
        # Here we create dictionary key from each word, out of a given list
        # Why we turn word first to tuple, then add it as a key to dictionary? - Dictionary key has to be immutable.

        temp_dict[key] = temp_dict.get(key, []) + [word]
        # Here we create value from empty list for dictionary key, and append words to it
        # As dictionary key has to be unique, whenever we call dictionary key, script will get proper key for us
        # in order to append word to the key's value ("temp_dict.get(key, []) + [word]")

    return temp_dict.values()


a = ["eat", "tea", "tan", "ate", "nat", "bat"]

print(groupAnagrams(a))
