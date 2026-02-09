import sys
from io import StringIO

sys.stdin = StringIO("""2
    Hacker
    Rank""")

cases = int(input())
if __name__ == "__main__":
    # Use a for loop to take into account the number of test cases which is from the cases input
    # So if it is two then it takes the loop two tries and gets the input for a new string in a new line
    for i in range(cases):
        first_string = str(input().strip())
        # Since it is in the cases loop there is two variables for holding odd/even values
        # The variables are default empty strings in the loop so it gets appended and not reset each time if not in the loop
        oneline = ""
        twoline = ""
        # The loop goes over the text input as a length since it is a string
        for x in range(len(first_string)):
            # If x divisibility by 2 it gives a remainder goes to the if condition
            # If x has no remainder then it adds to the variable in else condition
            # += is used to append to the existing string value
            if x % 2:
                oneline += first_string[x]
            else:
                twoline += first_string[x]

        print(twoline, oneline)
