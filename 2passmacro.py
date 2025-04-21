# Pass 1: Build Macro Name Table (MNT) and Macro Definition Table (MDT)
mnt, mdt, in_macro = {}, [], False
with open("D:/Users/Siddhant/Desktop/TICTACTOE/Third Year/6th SEMESTER/trainer/experiments/input_file.asm") as f:
    lines, i = f.readlines(), 0
    while i < len(lines):
        if lines[i].strip() == "MACRO":
            in_macro, name = True, lines[i+1].split()[0]
            mnt[name], start = len(mdt), i+1
            while lines[i].strip() != "MEND":
                mdt.append(lines[i].strip())
                i += 1
            mdt.append("MEND")
            i += 1
        else:
            i += 1

# Pass 2: Expand macros
with open("input_file.asm") as f, open("macro_output.asm", "w") as out:
    lines, skip = f.readlines(), False
    for i in range(len(lines)):
        if lines[i].strip() == "MACRO":
            skip = True
        elif lines[i].strip() == "MEND":
            skip = False
        elif not skip:
            tokens = lines[i].split()
            if tokens and tokens[0] in mnt:
                for line in mdt[mnt[tokens[0]]+1:]:
                    if line == "MEND": break
                    out.write(line + "\n")
            else:
                out.write(lines[i])
