class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def calculate_average(self):
        return sum(self.marks) / len(self.marks)


def calculate_class_averages(students):
    averages = {}
    top_student = None
    highest_average = 0

    for name, marks in students.items():
        student = Student(name, marks)
        avg = student.calculate_average()
        averages[name] = round(avg, 2)

        if avg > highest_average:
            highest_average = avg
            top_student = name

    return averages, top_student


students = {
    "John": [85, 78, 92],
    "Alice": [88, 79, 95],
    "Bob": [70, 75, 80]
}

averages, top_performer = calculate_class_averages(students)
print("Average Marks:", averages)
print("Top Performer:", top_performer)
