patients = []

def add_patient(name):
    patients.append(name)
    print("Patient added successfully")

def show_queue():
    if not patients:
        print("Patient is empty")
    else:
        for patient in patients:
            print(patient)


def next_patient():
    if not patients:
        print("Patient is empty")
    else:
        patient = patients.pop()
        print("Successful")
        print("Patient is now " + patient)

def search_patient(name):
    if name in patients:
        print("Patient found")
    else:
        print("Patient not found")

def count_patients():
    count = 0
    for patient in patients:
        count += 1
    print(f"count of patients is {count}")

def main():
    while True:
        print("==== Clinic queue manager =====")
        print("1. Add patient")
        print("2. Show patient")
        print("3. Next patient")
        print("4. Search patient")
        print("5. Count patients")
        print("6. Exit")

        try:
            choice = int(input("Enter your choice: "))
        except ValueError:
            print("please enter a valid number")
            continue
        if choice == 1:
            name = input("Enter patient name: ")
            add_patient(name)
        elif choice == 2:
            show_queue()
        elif choice == 3:
            next_patient()
        elif choice == 4:
            name = input("Enter patient name: ")
            search_patient(name)
        elif choice == 5:
            count_patients()
        elif choice == 6:
            print("Thank you for using this program")
            break
        else:
            print("Invalid choice")

main()
