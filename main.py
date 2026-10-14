
import numpy as np

print("===== MATRIX OPERATIONS TOOL =====")

# Input first matrix
r1 = int(input("Enter rows of first matrix: "))
c1 = int(input("Enter columns of first matrix: "))

print("Enter first matrix row by row:")
A = []
for i in range(r1):
    A.append(list(map(float, input().split())))
A = np.array(A)

# Input second matrix
r2 = int(input("Enter rows of second matrix: "))
c2 = int(input("Enter columns of second matrix: "))

print("Enter second matrix row by row:")
B = []
for i in range(r2):
    B.append(list(map(float, input().split())))
B = np.array(B)

while True:
    print("\n--- MENU ---")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Transpose")
    print("5. Determinant")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        if A.shape == B.shape:
            print("Result:\n", A + B)
        else:
            print("Matrices must have the same dimensions.")

    elif choice == "2":
        if A.shape == B.shape:
            print("Result:\n", A - B)
        else:
            print("Matrices must have the same dimensions.")

    elif choice == "3":
        if A.shape[1] == B.shape[0]:
            print("Result:\n", np.dot(A, B))
        else:
            print("Columns of A must equal rows of B.")

    elif choice == "4":
        print("Transpose of first matrix:\n", A.T)
        print("Transpose of second matrix:\n", B.T)

    elif choice == "5":
        if A.shape[0] == A.shape[1]:
            print("Determinant of first matrix:",
                  round(np.linalg.det(A), 2))
        else:
            print("First matrix must be square.")

        if B.shape[0] == B.shape[1]:
            print("Determinant of second matrix:",
                  round(np.linalg.det(B), 2))
        else:
            print("Second matrix must be square.")

    elif choice == "6":
        print("Thank you for using Matrix Operations Tool!")
        break

    else:
        print("Invalid choice. Please try again.")