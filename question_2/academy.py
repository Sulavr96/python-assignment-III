import csv
import sys
import time


class Academy:
    def __init__(self, courses, students):
        self.courses = courses
        self.students = students

    def export_courses(self):
        with open('courses.csv', 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["Course Name", "Code"])

            for k, v in self.courses.items():
                writer.writerow([k, v])

    def export_students(self):
        with open('students.csv', 'w') as file:
            writer = csv.writer(file)
            writer.writerow(['Student Name', 'Roll num', 'Amount Paid', 'Remaining Payment'])
            writer.writerow(self.students)

    @staticmethod
    def csv_reader(file_name):
        file_array = []
        with open(file_name, 'r', newline='') as file:
            reader = csv.reader(file)
            for row in reader:
                file_array.append(row)

        return file_array

    def list_courses(self, show_course):
        if show_course == 'Y' or show_course == 'y':
            available_courses = self.csv_reader('courses.csv')
            print("The available courses are: ")

            for course in available_courses:
                print("{0:<25} {1:<10}".format(course[0], course[1]))

            time.sleep(1)
            print()
        else:
            sys.exit("Thank you for your interest")

    def admit_student(self, confirmation, roll):
        if confirmation == 'y' or confirmation == 'Y':
            name = input("Please enter your name: ")
            payment = 10000
            remaining_payment = 10000

            students = self.csv_reader('students.csv')
            last_roll = int(students[-1][1])
            current_roll = last_roll + 1
            with open('students.csv', 'a') as file:
                writer = csv.writer(file)
                writer.writerow([name, current_roll, payment, remaining_payment])
                print("Congratulations! you have been admitted")
        else:
            sys.exit("Thank you for your interest")

    def list_students(self):
        students = self.csv_reader('students.csv')
        for student in students:
            print("{0:<15} {1:^15} {2:<15} {3:<15}".format(student[0], student[1], student[2], student[3]))
        print()

    def update_student(self, amount):
        with open('students.csv', newline='') as file:
            read_data = [row for row in csv.DictReader(file)]
            remaining_payment = int(read_data[-1]['Remaining Payment'])
            new_remaining_payment = remaining_payment - amount
            amount_paid = int(read_data[-1]['Amount Paid'])
            new_amount_paid = amount_paid + amount
            headers = read_data[0].keys()

            read_data[-1]['Amount Paid'] = str(new_amount_paid)
            read_data[-1]['Remaining Payment'] = str(new_remaining_payment)

        with open('students.csv', "w", newline="") as file:
            writer = csv.DictWriter(file, fieldnames=headers)
            writer.writeheader()
            writer.writerows(read_data)

        print("Payment received successfully!")
        time.sleep(1)
        self.list_students()

    def del_and_refund(self):
        students = self.csv_reader('students.csv')
        lines = list()
        member = students[-1][0]

        with open('students.csv', 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                lines.append(row)
                for field in row:
                    if field == member:
                        lines.remove(row)

        with open('students.csv', 'w') as file:
            writer = csv.writer(file)
            writer.writerows(lines)

        print("Please wait for your refund amount..")
        time.sleep(1)
        print("Please collect your refunded amount: 20000")
        time.sleep(1)
        self.list_students()
        print("Wish you a great future ahead!!")
        time.sleep(1)


course_dict = {'Programming': 'IT101', 'DBMS': 'IT102', 'Data Structure': 'IT105', 'Artificial Intelligence': 'IT104'}
student_array = ['Ram Thapa', 1, 10000, 10000]
academy1 = Academy(course_dict, student_array)

academy1.export_courses()
academy1.export_students()

accepted_values = ['y', 'Y', 'n', 'N']
while True:
    try:
        course_details = input("Do you want to list the available courses?(Y/N): ")
        if course_details in accepted_values:
            break
        print("Please enter a valid input")
    except Exception as e:
        print(e)

time.sleep(1)
academy1.list_courses(course_details)

time.sleep(1)
print("Your total fee for the course is 20000 which is to be paid in two installments of 10000 each")
print()
while True:
    try:
        payment_confirmation = input("Do you want to proceed for your first payment?(Y/N): ")
        if course_details in accepted_values:
            break
        print("Please enter a valid input")
    except Exception as e:
        print(e)

time.sleep(1)
academy1.admit_student(payment_confirmation, roll=2)
time.sleep(1)
academy1.list_students()

time.sleep(1)
print("Now its time for your second installment (Remaining 10000)")
print()
time.sleep(1)
while True:
    try:
        second_payment_confirmation = int(input("Please enter the remaining amount to be paid: "))
        if second_payment_confirmation == 10000:
            break
        print("Please enter the exact amount")
    except Exception as e:
        print(e)
print()
time.sleep(1)
academy1.update_student(10000)

time.sleep(2)
print("Congratulations!!! You have completed the course")
academy1.del_and_refund()
