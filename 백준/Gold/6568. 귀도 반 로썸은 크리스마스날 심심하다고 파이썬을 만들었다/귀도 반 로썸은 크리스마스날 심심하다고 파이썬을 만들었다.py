import sys
input = sys.stdin.readline
STA, LDA, BEQ, NOP, DEC, INC, JMP, HLT = [i for i in range(8)]
while True:
    pc, adder = 0, 0
    memory = [0] * 32
    for i in range(32):
        try:
            memory[i] = int(input().rstrip(), 2)
        except:
            sys.exit(0)
    while True:
        address = memory[pc]
        command, value = address // 32, address % 32
        pc = (pc + 1) % 32
        if command == STA: memory[value] = adder
        if command == LDA: adder = memory[value]
        if command == BEQ and adder == 0: pc = value
        if command == NOP: continue
        if command == DEC: adder = (adder + 255) % 256
        if command == INC: adder = (adder + 1) % 256
        if command == JMP: pc = value
        if command == HLT: break
    print(f"{bin(adder)[2:]:0>8}")
