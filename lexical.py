import re

def lexical_analyzer(s):
    patterns = [
        (r"\b(if|else|elif|while|for|in|break|continue|return|def|class|import|from|as|try|except|finally|raise|with|assert|lambda|global|nonlocal|True|False|None)\b", "KEYWORD"),
        (r"\b[a-zA-Z_]\w*\b", "IDENTIFIER"),
        (r"[+\-*/%**//=<>!]=?", "OPERATOR"),
        (r"\d+\.\d*", "FLOAT_LITERAL"),
        (r"\d+", "INTEGER_LITERAL"),
        (r"\"([^\\\"]|\\\\|\\\"|\\n|\\r|\\t)*?\"", "STRING_LITERAL"),
        (r"'([^\\']|\\\\|\\'|\\n|\\r|\\t)*?'", "STRING_LITERAL"),
        (r"[(),:;\[\]\{\}]", "PUNCTUATOR"),
        (r"\s+|#.*", None),  # Ignore whitespace and comments
    ]
    return [(t, m.group(0)) for m in [re.match(p[0], s[i:]) for i in range(len(s)) for p in patterns if re.match(p[0], s[i:])] if (t := m.re.pattern, m.group(0))[0]]

# Example usage:
statements = [
    "count = 10 + 5",
    "print(\"Hello, World!\")",
    "if x > 0: print(x)",
    "my_variable = 3.14 * radius ** 2",
    "def my_function(arg1, arg2): return arg1 + arg2"
]

for statement in statements:
    tokens = lexical_analyzer(statement)
    print(f"Tokens for '{statement}': {tokens}")
