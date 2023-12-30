from Student import Student

def main():
    courses = {
        ('Calculus II', 'MATH-2414', 'C', 4, 'Summer 2023', 'Austin Community College'),
        ('American Sign Language', 'SGNL-1401', 'B', 4, 'Summer 2023', 'Austin Community College'),
        ('American Sign Language', 'SGNL-1401', 'W', 4, 'Summer 2023', 'Austin Community College'),
    }

    s = Student(courses)

    print(s.gpa)
    print(s.completion_pct)

if __name__ == '__main__':
    main()
