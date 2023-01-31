def isValid(s):
    result = True
    validCharacters = ['(',')', '[', ']', '{', '}']
    validCharactersDict = {
        '(':')', '[': ']', '{': '}'
    }
    listString = list(s)
    firstCharacter = listString[0]
    openedCharacters = []
    if firstCharacter not in validCharactersDict.keys():
        result = False
        return result
    
    
    for _ in listString:
        if _ in validCharactersDict.keys():
            openedCharacters.append(_)
        if _ not in validCharacters:
            result = False
            return result
        
        if _ in validCharactersDict.values():
            c = openedCharacters.pop(len(openedCharacters) - 1)
            if validCharactersDict[c] != _:
                print
                return False    
    return result




print(isValid("([][]{[]})"))