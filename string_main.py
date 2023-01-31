def isValid(s):
    result = True
    validCharacters = ['(',')', '[', ']', '{', '}']
    validCharactersDict = {
        '(':')', '[': ']', '{': '}'
    }
    listString = list(s)
    firstCharacter = listString[0]
    openedCharacters = []
    
    
    # First let's check if the first character of the string is an opening character,
    if firstCharacter not in validCharactersDict.keys():
        result = False
        return result
    
    
    for _ in listString:
        
        # If character not a valid one close
        if _ not in validCharacters:
            result = False
            return result
        
        # If the character is an opening one, add it to the opened characters list
        if _ in validCharactersDict.keys():
            openedCharacters.append(_)
        
        if _ in validCharactersDict.values():
            c = openedCharacters.pop(len(openedCharacters) - 1)
            if validCharactersDict[c] != _:
                print
                return False    
    return result




print(isValid("([][]{[]})"))