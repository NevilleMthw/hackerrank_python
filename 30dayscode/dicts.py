import sys
from io import StringIO

sys.stdin = StringIO("""3
sam 99912222
tom 11122222
harry 12299933
sam
edward
harry""")

# Input to read the number of cases
cases = int(input())
if __name__ == "__main__":
    phonebook = {}
    # First for loop to add to the dictionary based on the number of cases
    for _ in range(cases):
        # Take input of name and number of one line of string
        # so the input.split() takes the input as a list
        name, value = input().split()
        # Append from the list input to the dict
        phonebook[name] = value
    
    # Second while loop to take in the query inputs while true
    while True:
        try:
            query = input()
            # Check condition
            if query in phonebook:
                print(f"{query}={phonebook[query]}")
            else:
                print("Not found")
        except EOFError:
            break
