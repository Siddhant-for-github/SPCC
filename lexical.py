import re

def lexer(s):
    patterns = [
        (r"\b(if|else|elif|while|for|in|break|continue|return|def|class|import|from|as|try|except|finally|raise|with|assert|lambda|global|nonlocal|True|False|None)\b", "KEYWORD"),
        (r"\b[a-zA-Z_]\w*\b", "IDENTIFIER"),
        (r"[+\-*/%**//=<>!]=?", "OPERATOR"),
        (r"\d+\.\d*", "FLOAT"),
        (r"\d+", "INT"),
        (r"\"([^\\\"]|\\\\|\\\"|\\n|\\r|\\t)*?\"", "STR"),
        (r"'([^\\']|\\\\|\\'|\\n|\\r|\\t)*?'", "STR"),
        (r"[(),:;\[\]\{\}]", "PUNCT"),
        (r"\s+|#.*", None),
    ]
    tokens = []
    pos = 0
    while pos < len(s):
        for pat, typ in patterns:
            m = re.match(pat, s[pos:])
            if m:
                lexeme = m.group(0)
                if typ:
                    tokens.append((typ, lexeme))
                pos += len(lexeme)
                break
        else:
            raise ValueError(f"Invalid char at {pos}: '{s[pos]}'")
    return tokens

code1 = "count = 10 + 5"
print(f"'{code1}': {lexer(code1)}")
code2 = "print(\"Hello, World!\")"
print(f"'{code2}': {lexer(code2)}")
code3 = "if x > 0: print(x)"
print(f"'{code3}': {lexer(code3)}")
