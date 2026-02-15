import sys
from io import StringIO

sys.stdin = StringIO("""3
sam 99912222
tom 11122222
harry 12299933
sam
edward
harry""")

cases = int(input())
if __name__ == "__main__":
    phonebook = {}

    for _ in range(cases):
        name, value = input().split()
        phonebook[name] = value

    while True:
        try:
            query = input()
            if query in phonebook:
                print(f"{query}={phonebook[query]}")
            else:
                print("Not found")
        except EOFError:
            break
