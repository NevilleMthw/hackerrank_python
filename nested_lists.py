import sys
from io import StringIO

sys.stdin = StringIO("""5
Harry
37.21
Berry
37.21
Tina
37.2
Akriti
41
Harsh
39""")

if __name__ == "__main__":
    # Create lists to store students and only scores
    students = []
    scores_new = []

    for _ in range(int(input())):
        name = input()
        score = float(input())
        # Append to the students list into a nested list format
        students.append([name, score])

    # Exit the loop to sort all students by name alphbetically
    students.sort()
    # Append all the scores only to the new list
    for x in students:
        scores_new.append(x[:][1])

    # Remove duplicates by putting into set
    scores_new = set(scores_new)
    # Sort values using sorted() which is ascending by default
    scores_new = sorted(scores_new)

    # Compare if the values match in the students list
    for values in students:
        if scores_new[1] == values[:][1]:
            print(values[0])
