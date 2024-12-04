from helpers import read_file

import re

with open("input.txt", "r") as f:
    data = f.read()

def do_dont_transformer(s: str) -> str:
    '''
    Takes some string s, and all mul following don't keywords
    are removed, all mul characters following do are kept
    '''
    new_data = ""

    while True:
        dont_index = s.find("don't()")
        if dont_index == -1:
            new_data += s
            break
        new_data += s[:dont_index]
        s = s[dont_index:]
        do_index = s.find("do()")
        if dont_index == -1:
            break
        # everything in this substring doesn't execute.
        s = s[do_index:]
    return new_data




data = data.replace("\n", "")

mul_re = re.compile(r"mul\((\d+),(\d+)\)")

total = 0
matches = mul_re.findall(data)
for match in [(int(a), int(b)) for (a,b) in matches]:
    total += match[0] * match[1]

print("part 1", total)

data = do_dont_transformer(data)
total = 0
matches = mul_re.findall(data)
for match in [(int(a), int(b)) for (a,b) in matches]:
    total += match[0] * match[1]
print("part 2", total)
