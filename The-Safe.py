class Safe:
    def __init__(self, password):

        self.password = password

        self.contents = {}

    def add_item(self, item, quantity):
        if item in self.contents:
            self.contents[item] += quantity
        else:
            self.contents[item] = quantity
        print(f"{quantity} {item}(s) added to the safe.")

    def withdraw_item(self, item, quantity):

        if item in self.contents and self.contents[item] >= quantity:

            self.contents[item] -= quantity

            print(f"{quantity} {item}(s) withdrawn from the safe.")

        else:

            print("Insufficient quantity in the safe.")

    def display_contents(self):

        print("Safe Contents:")

        for item, quantity in self.contents.items():

            print(f"{item}: {quantity}")

def main():
    print("Welcome to The Safe.")

    password = input("Set the password for the safe: ")

    safe = Safe(password)

    while True:
        print("Safe Secured.")

        attempt = input("Enter the password to access the safe (type 'exit' to quit): ")

        if attempt == 'exit':

            break

        elif attempt == safe.password:

            while True:
                print("\n1. Add item to safe\n2. Withdraw item from safe\n3. Display safe contents\n4. Exit")

                choice = input("Enter your choice: ")

                if choice == '1':

                    item = input("Enter the item to add: ")

                    quantity = int(input("Enter the amount to add: "))

                    safe.add_item(item, quantity)

                elif choice == '2':

                    item = input("Enter the item to withdraw: ")

                    quantity = int(input("Enter the amount to withdraw: "))

                    safe.withdraw_item(item, quantity)

                elif choice == '3':

                    safe.display_contents()

                elif choice == '4':

                    break
                else:
                    print("Invalid choice. Please try again.")
        else:
            print("Incorrect password. Please try again.")

if __name__ == "__main__":
    main()
