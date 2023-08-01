from openpyxl import Workbook

def get_student_data():
    roll_number = input("Enter Roll Number: ")
    name = input("Enter Name: ")
    return roll_number, name

def save_to_excel(student_data):
    wb = Workbook()
    sheet = wb.active
    sheet.title = "Student Data"
    sheet.append(["Roll Number", "Name"])
    for roll_number, name in student_data:
        sheet.append([roll_number, name])
    wb.save("student_data.xlsx")

if __name__ == "__main__":
    print("Enter details for five students:")
    student_data = []
    for _ in range(5):
        print(f"Student {len(student_data) + 1}:")
        roll_number, name = get_student_data()
        student_data.append((roll_number, name))

    print("Data successfully stored in Excel.")
    save_to_excel(student_data)
