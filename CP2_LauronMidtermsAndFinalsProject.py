# Kim Benedick Lauron
# Simple Reservation System (Console-Based)

reservations = []

def show_menu():
    print("\n==WELCOME TO NOBU RESERVATIONS==")
    print("1. Add Reservation")
    print("2. Find/View Reservation")
    print("3. Delete Reservation")
    print("4. Exit")

def add_reservation():
    name = input("Enter Reservation Name: ").strip()
    reservations.append(name)
    if name == "":
        print("Reservation Name is empty. Please try again.")
        return
    date = input("Enter Reservation Date (ex.DD-MM-YYYY: ").strip()
    if date == "":
        print("Reservation Date is empty. Please try again.")
        return

def view_reservations():
    if len(reservations) == 0:
        print("No Reservation Found.")
        return