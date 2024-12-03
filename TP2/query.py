import re

def valid_query(query):
    valid = [
        "Terme",
        "Terme AND Terme",
        "Terme OR Terme",
        "Terme AND Terme OR Terme",
        "NOT Terme",
        "NOT Terme AND Terme",
        "NOT Terme OR NOT Terme",
        "Terme AND NOT Terme",
        "NOT Terme AND Terme OR NOT Terme"
    ]

    not_valid = [
        "AND",
        "OR",
        "Terme Terme",
        "Terme OR",
        "AND OR Terme",
        "Terme AND OR Terme",
        "Terme AND Terme AND",
        "NOT",
        "NOT NOT Terme",
        "NOT AND Terme",
        "Terme AND NOT",
        "Terme AND Terme NOT"
    ]



    query = query.lower()
    query = query.strip()
    if '(' in query or ')' in query:
        return False
    
    regexbool = r'(\bNOT\b|\bAND\b|\bOR\b|\b\w+)'
    
    tokens = re.findall(regexbool, query)

    print(tokens)

    i = 0

    while i in range(len(tokens)):
        token = tokens[i]
        if len(tokens) == 1:
            if tokens[0].lower() in ['not', 'and', 'or']:
                return False
            else: 
                return True
        else:
            if tokens[0].lower() in ['and', 'or']:
                return False
            if tokens[0] == tokens[1]:
                return False
            if (tokens[0].lower() not in ['not', 'and', 'or'] and tokens[1].lower() not in ['not', 'and', 'or']) :
                return False
            if (tokens[len(tokens)-1].lower() in ['not','and', 'or']):
                return False

            if token.lower() in ['and', 'or']:
                if tokens[i+1].lower() in ['and', 'or', ]:
                    return False
            
            if token.lower() in ['and', 'or']:
                if tokens[i+1].lower() in ['not'] and i+1 == len(tokens):
                    return False
                
            
            if token.lower() == 'not':
                for word in reversed(tokens[:i]):
                    if word in ['and', 'or']:
                        break
                    if word == 'not' and word[i]:
                        return False
    
        i += 1

    return True    


queries_to_check = [
    "terme",
    "NOT",
    "terme terme",
    "NOT TERME NOT TERME",
    "NOT TERME OR NOT TERME AND NOT TERME",
    "NOT NOT TERME",
    "TERME AND NOT",
    "",
    "",
    "",
    "",
    "",
]

print(valid_query(query=queries_to_check[4]))
