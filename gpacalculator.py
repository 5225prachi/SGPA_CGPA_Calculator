def calculate_sgpa():
    num_subjects = int(input("Enter number of subjects: "))
    total_marks = 0
    total_credits = 0

    for i in range(num_subjects):
        marks = float(input(f"Enter marks obtained in subject {i+1}: "))
        credits = float(input(f"Enter credits for subject {i+1}: "))
        total_marks += (marks * credits)
        total_credits += credits
    
    sgpa = total_marks / total_credits
    return sgpa

def calculate_cgpa():
    num_semesters = int(input("Enter number of semesters: "))
    total_sgpa = 0

    for i in range(num_semesters):
        print(f"\nSemester {i+1}:")
        semester_sgpa = calculate_sgpa()
        total_sgpa += semester_sgpa
    
    cgpa = total_sgpa / num_semesters
    return cgpa

def main():
    print("SGPA and CGPA Calculator\n")
    choice = input("Do you want to calculate CGPA (C) or SGPA (S)? ").lower()

    if choice == 's':
        sgpa = calculate_sgpa()
        print(f"\nYour SGPA is: {sgpa:.2f}")
    elif choice == 'c':
        cgpa = calculate_cgpa()
        print(f"\nYour CGPA is: {cgpa:.2f}")
    else:
        print("Invalid choice! Please choose either 'C' for CGPA or 'S' for SGPA.")

if __name__ == "__main__":
    main()
