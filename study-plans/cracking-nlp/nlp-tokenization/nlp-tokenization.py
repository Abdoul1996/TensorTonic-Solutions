def tokenize(text: str) -> list:
    """
    Returns a list of token strings.
    """

    token = []
    current = ""

    for char in text:
        # Scan each characters and check if current char is valid 
        if ('A' <= char <='Z' or 
            'a' <= char <= 'z' or 
            '0' <= char <= '9' or 
            char == '_'):

            current += char 
        # handle invalid characters
        else:
            if not char.isspace():
                if current:
                    token.append(current)
                current = ""
                token.append(char)
            else:
                if current:
                    token.append(current)
                    current = ""
                continue
    if current:
      token.append(current)

    return token