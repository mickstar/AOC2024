from helpers import read_lines,abs


lines = read_lines("input.txt")

def is_safe(data: list[int]) -> tuple[bool, int]:
    '''
    Returns a tuple of a boolean indicating if the data is safe and an index of the offending data
    '''
    if len(data) <= 1:
        return (True, 0)

    direction = (data[1] - data[0]) < 0

    for i in range(len(data)-1):
        diff = (data[i+1] - data[i])
        if direction != (diff < 0):
            # direction mismatch
            return (False, i)
        diff = abs(diff)
        if diff < 1 or diff > 3:
            return (False, i)

    return (True, 0)

data = []
for line in lines:
    data.append([int(x) for x in line.split(" ")])

safe_count = 0
for row in data:
    safety,error = is_safe(row)
    if safety:
        safe_count += 1
print("part 1: total", safe_count)

safe_count = 0
for row in data:
    safety, error_index = is_safe(row)
    if safety:
        safe_count += 1
        continue
    # now we need to remove the offending score and see if we can use it
    modified_row = list(row)
    modified_row.pop(error_index)
    if is_safe(modified_row)[0]:
        safe_count +=1
        continue

    modified_row = list(row)
    modified_row.pop(error_index + 1)
    if is_safe(modified_row)[0]:
        safe_count += 1
        continue

    if error_index == 0:
        continue
    modified_row = list(row)
    modified_row.pop(error_index - 1)
    if is_safe(modified_row)[0]:
        safe_count += 1
        continue

# 655 too low
print("part 2: total", safe_count)
