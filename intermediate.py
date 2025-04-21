import re

def tac(c):
    t = 0
    def new_temp():
        nonlocal t; v = f"t{t}"; t += 1; return v
    def expr(e):
        if re.match(r"^[a-zA-Z]$|^\d+$", e): return e
        parts = re.split(r'(\+|\-|\*|\/)', e, 1)
        if len(parts) != 3: return None
        o1, op, o2 = parts
        x, y = expr(o1.strip()), expr(o2.strip())
        tmp = new_temp(); print(f"{tmp} = {x} {op} {y}"); return tmp
    v, e = c.split("="); v = v.strip(); e = e.strip(); res = expr(e)
    if res: print(f"{v} = {res}")

def main():
    cases = ["x = a + b"]
    for c_statement in cases:
        print(f"\nC: {c_statement}")
        tac(c_statement)

if __name__ == "__main__":
    main()
