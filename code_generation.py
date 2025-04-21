import re

def asm(tac):
    a = ""
    regs = ['EAX', 'EBX', 'ECX', 'EDX']; rmap = {}; ri = 0
    def get_reg(v):
        nonlocal ri
        if v not in rmap:
            if ri < len(regs): rmap[v] = regs[ri]; ri += 1
            else: a += f"  PUSH {rmap.pop(list(rmap)[0])}\n"; rmap[v] = regs[ri-1]
        return rmap[v]
    for t in tac:
        d, s = t.split("="); d = d.strip(); s = s.strip()
        if re.match(r'^\w+$', s): a += f"  MOV {get_reg(d)}, {s}\n"
        else:
            p = re.split(r'\s*(\+|\-|\*|\/)\s*', s)
            if len(p) == 3:
                o1, op, o2 = p; r_d = get_reg(d); r_o1 = get_reg(o1.strip())
                a += f"  MOV {r_d}, {o1.strip()}\n"
                if op == '+': a += f"  ADD {r_d}, {o2.strip()}\n"
                elif op == '-': a += f"  SUB {r_d}, {o2.strip()}\n"
                elif op == '*': a += f"  IMUL {r_d}, {o2.strip()}\n"
                elif op == '/': a += f"  IDIV {r_d}, {o2.strip()}\n"
            else: a += f"  MOV {get_reg(d)}, {s}\n"
    return a

def main():
    test_cases = [
        ["x = a + b", "y = x * c", "z = y - d"],
    ]
    for i, tac_code in enumerate(test_cases):
        print(f"\nTAC Code {i+1}:\n" + "\n".join(tac_code))
        assembly_code = asm(tac_code)
        print(f"\nAssembly Code {i+1}:\n{assembly_code}")

if __name__ == "__main__":
    main()
