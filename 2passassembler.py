symtab, optab = {}, {"LDA": "00", "STA": "0C", "LDCH": "50", "STCH": "54"}
locctr, intermed = 0, []

# Pass 1: Generate symbol table and intermediate file
with open("macro_output.asm") as f:
    for line in f:
        parts = line.strip().split()
        if len(parts) == 3:
            label, op, arg = parts
            symtab[label] = locctr
        elif len(parts) == 2:
            op, arg = parts
        else:
            continue
        intermed.append((locctr, line.strip()))
        locctr += 3

# Pass 2: Generate object code
with open("object_code.txt", "w") as out:
    for addr, line in intermed:
        parts = line.split()
        if len(parts) == 3: _, op, arg = parts
        elif len(parts) == 2: op, arg = parts
        else: continue
        code = optab.get(op, "??")
        arg_addr = symtab.get(arg, 0)
        out.write(f"{addr:04X} {code}{arg_addr:04X}\n")
