
def main():
    courses = [
        ('Calculus II', 'MATH-2414', 'C', 4, 'Summer 2023'),
        ('American Sign Language', 'SGNL-1401', 'B', 4, 'Summer 2023'),
    ]

    print(calculate_gpa(courses))

def calculate_gpa(courses, only_completed=True):

    def should_use(letter):
        return only_completed or (letter != 'W' and letter != 'I')

    letter_values = {
        'A' : 4, 'B' : 3, 'C' : 2, 'D' : 1, 'F' : 0, 'W' : 0, 'I' : 0,
        'a' : 4, 'b' : 3, 'c' : 2, 'd' : 1, 'f' : 0, 'w' : 0, 'i' : 0,
    }

    (points, hours) = zip(*[(letter_values[letter]*hours, hours) for (_, _, letter, hours, _) in courses if should_use(letter)])


    gpa = sum(points)/sum(hours) if sum(hours) != 0 else -1 # no hours completed

    return gpa

if __name__ == '__main__':
    main()
