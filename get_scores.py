def convertLine(line):
    ''' try to convert "LASTNAME FIRSTNAME 1GxTDx X,X" to a float'''
    try:
        return float(line.split(" ")[-1].replace(',', '.'))
    except:
        return False


def getScoresFromFile(path):
    ''' return a array of all the scores (float) '''

    nArray = []

    with open(path, 'r') as f:
        lines = f.read().split("\n")

        for line in lines:
            c = convertLine(line)
            if c:
                nArray.append(c)

    return nArray
