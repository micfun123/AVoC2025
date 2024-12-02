input_data = open("in.txt", "r")

data = input_data.read().split('\n')

total_safe = 0

def check_row(row):
    
    direction = None
    print(row) 
    for j in range(1, len(row)):
        diff = int(row[j]) - int(row[j - 1])

        
        if diff == 0 or abs(diff) > 3:
            return False, j

        if direction is None:
            direction = "up" if diff > 0 else "down"
        else:
            if (direction == "up" and diff < 0) or (direction == "down" and diff > 0):
                return False, j

    return True, None


def has_discrepancy(row):
    for i in range(len(row)):
        modified_row = row[:i] + row[i+1:]
        safe, _ = check_row(modified_row)
        if safe:
            return True
    return False


for i in data:
    row = i.split(" ")  
    row = list(map(int, row)) 
    
    safe, _ = check_row(row)
    if not safe:
        safe = has_discrepancy(row)



    print(safe) 
    if safe:
        total_safe += 1

print(total_safe)
