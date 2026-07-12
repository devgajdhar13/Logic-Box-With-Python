print("Welcome to the Pattern Generator and Number Analyzer.")

while True:
    print("\nSelect an option:")
    print("1. Generate a Pattern")
    print("2. Analyze a Range of Numbers")
    print("3. Exit")

    choice = int(input("Enter your choice number: "))

    if choice == 1:
        rows = int(input("Enter the number of rows: "))

        print("\nPattern:")
        for i in range(rows):
            for j in range(i + 1):
                print("*", end="")
            print()

    elif choice == 2:
        
        Start = int(input("\nEnter the start of the range: "))
        End = int(input("Enter the end of the range: "))

        total = 0

        for a in range(Start, End + 1):
            if a % 2 == 0:
                print("Number", a, "is Even")
            else:
                print("Number", a, "is Odd")

            total = total + a

        print("Sum of all numbers from", Start, "to", End, "is:", total)

    elif choice == 3:
        print("Exit")
        break

    else:
        print("Invalid")
