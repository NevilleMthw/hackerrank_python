import sys
from io import StringIO

sys.stdin = StringIO("""12
insert 0 5
insert 1 10
insert 0 6
print
remove 6
append 9
append 1
sort
print
pop
reverse
print
""")

if __name__ == '__main__':
    N = int(input())
    
    new_list = []
    
    # Use the value of N to iterate over the commands
    for x in range(N):
        # Split the input strings into a list of strings (by default)
        # Convert the indices of the list into int from strings
        split_string = input().split()
        if split_string[0] == 'insert':
            new_list.insert(int(split_string[1]), int(split_string[2]))
        elif split_string[0] == 'print':
            print(new_list)
        elif split_string[0] == 'remove':
            new_list.remove(int(split_string[1]))
        elif split_string[0] == 'append':
            new_list.append(int(split_string[1]))
        elif split_string[0] == 'sort':
            new_list.sort()
        elif split_string[0] == 'pop':
            new_list.pop()
        elif split_string[0] == 'reverse':
            new_list.reverse()
