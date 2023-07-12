def check_numbers(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()    
    lines = [line.strip().split() for line in lines]

    numbers = [line[-1] for line in lines]
    if numbers[0] == numbers[1]:
        return True
    else:
        return False    

filename = 'note.txt'
are_numbers_same = check_numbers(filename)
if are_numbers_same:
    print("Two id numbers are the same.")
else:
    print("Two id numbers are different.")
