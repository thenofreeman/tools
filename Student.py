class Student:
    def __init__(self, courses):
        self._letter_values = {
            'A' : 4, 'B' : 3, 'C' : 2, 'D' : 1, 'F' : 0, 'W' : 0, 'I' : 0, 'P' : 0,
            'a' : 4, 'b' : 3, 'c' : 2, 'd' : 1, 'f' : 0, 'w' : 0, 'i' : 0, 'p' : 0,
        }

        self._courses = set(courses)
        self._gpa = self.calculate_gpa()
        self._completion_pct = self.calculate_completion_pct()

    @property
    def info(self):
        info_str = '| '
        info_str += f'GPA: {self._gpa: .2f} | '
        info_str += f'Credit Completion %: {self._completion_pct: .1%} | '

        return info_str

    @property
    def gpa(self):
        return self._gpa

    @gpa.setter
    def gpa(self, value):
        self._gpa = value

    @property
    def completion_pct(self):
        return self._completion_pct

    @completion_pct.setter
    def completion_pct(self, value):
        self._completion_pct = value

    def should_use(self, letter):
        return (letter != 'W' and letter != 'I')

    def calculate_gpa(self):
        (points, hours) = zip(*[(self._letter_values[letter]*hours, hours) for (_, _, letter, hours, _, _) in self._courses if self.should_use(letter)])

        return sum(points)/sum(hours) if sum(hours) != 0 else 0

    def calculate_completion_pct(self):
        attempted = [hours for (_, _, _, hours, _, _) in self._courses]
        completed = [hours for (_, _, letter, hours, _, _) in self._courses if self.should_use(letter)]

        return sum(completed)/sum(attempted) if sum(attempted) != 0 else 0
