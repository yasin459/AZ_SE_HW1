def check_numbers(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()    
    lines = [line.strip().split() for line in lines]
    
filename = 'note.txt'
are_numbers_same = check_numbers(filename)
if are_numbers_same:
    print("same.")
else:
    print("different.")
