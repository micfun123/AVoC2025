input_data = open("test.txt", "r")
data = input_data.read().split('\n')

total_safe = 0

def check_row(row):
    direction_of_change = []
    for j in range(1, len(row)):
        out = int(row[j]) - int(row[j-1])
        if out < 0:
            direction_of_change.append("down")
        elif out > 0:
            direction_of_change.append("up")
        
        
        if abs(int(row[j]) - int(row[j-1])) > 3 or (int(row[j]) - int(row[j-1])) == 0:
            return False, j 
        
    
    for k in range(len(direction_of_change) - 1):
        if direction_of_change[k] != direction_of_change[k+1]:
            return False, k + 1  
    
    return True, None  


for i in data:
    row = i.split(" ")  
    row = list(map(int, row)) 
    
    
    safe, fail_index = check_row(row)
    
    if not safe:
        modified_row = row[:fail_index] + row[fail_index+1:]
        safe, _ = check_row(modified_row)
    
    print(safe) 
    if safe:
        total_safe += 1

print(total_safe)
