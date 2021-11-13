def lengthOfLongestSubstring(s):
    charSet = set()
    maximum = 0
    duplicate = 0

    for value in range(len(s)):
        # Check if next character in "charSet"
        # If yes, then remove all the characters from "charSet", until (including) the element we are looking for
        # Here is "duplicate" value increases, everytime we remove an element from "charSet",
        # until we reach the duplicated element (which we look for)
        while s[value] in charSet:
            charSet.remove(s[duplicate])
            duplicate += 1

        # If character doesn't exist in "charSet", we are adding it to "charSet"
        charSet.add(s[value])

        # Here we check, if length of the "charSet" is bigger than "maximum's" value
        # If yes, then change "maximum's" value to "len(charSet)"
        if len(charSet) > maximum:
            maximum = len(charSet)

    return maximum


lengthOfLongestSubstring("abcabcbb")
