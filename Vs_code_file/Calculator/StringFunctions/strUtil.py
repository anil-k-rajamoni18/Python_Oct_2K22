def filterFirstName(data):
    if data:
        for ch in data:
            return ch.split()[0]
    else:
        return "empty data"


def convertUpper(st):
    return st.upper()


def printAscii(character):
    return ord(character)

#["Kumar Rajamoni","Python User"]