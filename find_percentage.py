import sys
from io import StringIO

sys.stdin = StringIO("""2
Harsh 25 26.5 28
Anurag 26 28 30
Harsh""")

if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    
    # Select the student's marks based on the input
    selected_marks = student_marks[query_name]
    
    average_marks = sum(selected_marks) / len(selected_marks)
    
    print(f"{average_marks:.2f}")
