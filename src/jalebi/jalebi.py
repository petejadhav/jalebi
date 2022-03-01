# MIT License
# Author - Prithviraj Jadhav (petejadhav.github.io)

# Logic -
# peterJohn123 -> peter John 123
# peter-john-123 -> peter john 123

# Char Groups -> A-Z; a-z; 0-9
charGroups = [(65,90),(97,122),(48,57)]
def getCharGroup(ch):
    code = ord(ch)
    for idx,grp in enumerate(charGroups):
        if code >= grp[0] and code <= grp[1]:
            return idx
    return -1#code

# Takes boundary/edge character for split
def jalebiSplit(raw_str):
    output = []
    substring = ""
    last_group = -2
    for i in raw_str:
        curr_group = getCharGroup(i)
        if curr_group != last_group:
            # change
            if len(substring) == 1 and last_group == 0 and curr_group == 1:
                last_group=curr_group
                substring += i
                continue
            last_group=curr_group
            output.append(substring)
            substring = ""
        substring += i
    output.append(substring)
    return output[1:]


# Takes boundary/edge character for split but does not add it to list
def jalebi(raw_str):
    output = []
    substring = ""
    last_group = -1
    for i in raw_str:
        curr_group = getCharGroup(i)
        if curr_group != last_group:
            # change
            if last_group == -1:
                substring = substring[:-1]
            if len(substring) == 1 and last_group == 0 and curr_group == 1:
                last_group=curr_group
                substring += i
                continue
            if len(substring) > 0: output.append(substring)
            last_group=curr_group
            substring = ""
        substring += i
    output.append(substring)
    return output
