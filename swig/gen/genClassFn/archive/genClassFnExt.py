#
#   generate class function extensions for swig
#

graphTypes = ['TUNGraph', 'TNGraph', 'TNEANet']

def removeFirstParam(funcDecl):
    startParamIdx = funcDecl.find('(')
    endParamIdx = funcDecl.find(')')
    commaIdx = funcDecl.find(',')
    if commaIdx != -1:
        # If function has two or more parameters
        newFuncDecl = funcDecl[:(startParamIdx + 1)] + funcDecl[commaIdx+1:].lstrip()
    else:
        # If function has only one parameter
        newFuncDecl = funcDecl[:(startParamIdx + 1)] + funcDecl[endParamIdx:]
    return newFuncDecl

def stripTypes(decl):
    returnStr = ""
    currentArg = ""
    for char in decl:
        if char in (" ", "\t"):
            currentArg = ""
        elif char in (",",")"):
            equalsIdx = currentArg.find("=")
            if equalsIdx != -1:
                currentArg = currentArg[:equalsIdx]
            returnStr += currentArg
            returnStr += (char + " ")
        else:
            currentArg += char
    return returnStr.strip()

def genFuncCall(funcDecl, funcName, graphType):
    startParamIdx = funcDecl.find('(')
    endParamIdx = funcDecl.find(')')
    commaIdx = funcDecl.find(',')
    
    funcCall = funcName
    if commaIdx != -1:
        # If function has two or more parameters
        funcCall += "(P" + graphType[1:] + "($self), " + stripTypes(funcDecl[commaIdx + 1:])
    else:
        # If function has only one parameter
        funcCall += "(P" + graphType[1:] + "($self))"
    return funcCall     

def getFuncName(funcDecl):
    startParamIdx = funcDecl.find('(')
    s = funcDecl[:startParamIdx].strip()
    last_space = max(s.rfind(' '), s.rfind('\t'))
    name = s[last_space + 1:]
    while not name[0].isalpha():
        name = name[1:]
    return name

for graphType in graphTypes:
    print("%extend " + graphType + "{")

    with open('classFnDef.txt', 'r') as f:
        for line in f:
            funcName = line[:line.find(' ')]
            funcHeader = line[(line.find(' ') + 1):].strip()

            startParamIdx = funcHeader.find('(')
            endParamIdx = funcHeader.find(')')
            startTemplateIdx = funcHeader.find('<')
            endTemplateIdx = funcHeader.find('>')

            funcDecl = funcHeader[(endTemplateIdx + 1):(endParamIdx + 1)].strip()
            name = getFuncName(funcDecl)
            newFuncDecl = removeFirstParam(funcDecl).strip()
            funcCall = genFuncCall(funcDecl, funcName, graphType).strip()

            if name == funcName:
                print ("    " + newFuncDecl + "{")
                print ("        " + "return TSnap::" + funcCall + ";")
                print ("    }")
                
        print ("};")
        print()
