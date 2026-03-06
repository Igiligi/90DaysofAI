# Create student_grades.py that stores student names and grades in a dict, loops through to print each, and calculates average

def show_menu():
    """Shows the Menu"""
    print("\n" + "*" * 50)
    print("🧮 YOUR STUDENT AVERAGE CALCULATOR APP".center(50))  # Keeps the output at the center of 35 spaces or characters
    print("*" * 50)
    print("1. 📝 Enter Student Name and Grade")
    print("2. 🖋 Add New Grade(s) to a Student")
    print("3. 🧮 Calculate Average")
    print("4. 👁 Show student list")
    print("5. ❌ Exist")

def add_student_name_and_grade(student_name_grade):
    student_name = input(f"Enter student name: ").strip().upper()
    student_grade = input(f"Enter student grade: ").strip().upper()
    student_name_grade[f"{student_name}"] = f"{student_grade}"
    print(f"Name: {student_name}. Grade: {student_grade} added to the dictionary")

    return student_name_grade


def add_grade(student_name_grade):
    print(student_name_grade)

def calculate_average():
    pass

def show_student_list():
    pass

def main():
    """The main program"""
    student_name_grade = {}

    while True:
        show_menu()
        choice = input(f"\nEnter choice (1-5): ").strip().lower()

        if choice == "1":
            add_student_name_and_grade(student_name_grade)

        elif choice == "2":
            add_grade(student_name_grade)

        elif choice == "3":
            calculate_average()

        elif choice == "4":
            show_student_list()

        elif choice == "5":
            print(f"\nThank you for using the STUDENT AVERAGE CALCULATOR APP. Good luck!")
            break

        else:
            print(f"\nInvalid choice! Please enter a choice in (1, 2, 3, 4, or 5)")

        # Pause after actions (except exit)
        if choice in {"1", "2", "3", "4"}:
            input("\n⏎ Press Enter to continue...")


# Run program
if __name__ == "__main__":
    main()

# ============================================
# 📚 WHAT I LEARNED TODAY (DAY 5)
# ============================================
#
# 1. DICTIONARIES:
#    - Store key-value pairs: students = {"name": grade}
#    - Keys must be unique (like student names)
#    - Values can be any data type
#
# 2. DICTIONARY METHODS:
#    - .items() – returns (key, value) pairs for looping
#    - .keys() – returns all keys (names)
#    - .values() – returns all values (grades)
#    - .get(key) – safely gets value (returns None if not found)
#
# 3. ADDING/UPDATING:
#    - dict[key] = value (adds new or updates existing)
#    - del dict[key] removes an entry
#
# 4. LOOPING THROUGH DICTIONARIES:
#    - for name in students: (loops through keys)
#    - for name, grade in students.items(): (loops through both)
#
# 5. DICTIONARY OPERATIONS:
#    - len(dict) – number of entries
#    - if key in dict: – check if exists
#    - sum(dict.values()) – total of all values
#
# 6. ADVANCED DICTIONARY PATTERNS:
#    - max(dict, key=dict.get) – finds key with highest value
#    - sorted(dict.items(), key=lambda x: x[1]) – sorts by grade
#    - List comprehension with dict: [grade for grade in dict.values()]
#
# 7. REAL-WORLD APPLICATIONS:
#    - Grade tracking (this project)
#    - Student records
#    - Any lookup table (prices, codes, settings)
#
# 8. STATISTICAL CONCEPTS:
#    - Average = sum / count
#    - Range = max - min
#    - Percentile via ranking