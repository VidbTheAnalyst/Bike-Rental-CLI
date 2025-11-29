# Simple Bike Rental System 
import math
from datetime import datetime

RATE_PER_HOUR = 100  

class Bikeshop:
    def __init__(self, stock):
        self.stock = stock
        self.current_rental = None   

    def displaybike(self):
        print("Total Bikes:", self.stock)

    def rentforbike(self, name, qty):
        if self.current_rental is not None:
            print("A bike is already rented!! Please return it first.")
            return

        if qty <= 0:
            print("Enter a positive number: ")
            return
        if qty > self.stock:
            print("Not enough bikes in stock")
            return

        self.stock -= qty
        self.current_rental = {
            'name': name,
            'qty': qty,
            'start': datetime.now()
        }

        print(f"Rented {qty} bike(s) to {name}.")
        print("Start time:", self.current_rental['start'].strftime("%Y-%m-%d %H:%M:%S"))

    def returnbike(self):
        if self.current_rental is None:
            print("No active rental to return.")
            return

        rent = self.current_rental
        end = datetime.now()
        duration_seconds = (end - rent['start']).total_seconds()

        duration_hours = math.ceil(duration_seconds / 3600) or 1  # minimum 1 hour 
        amount = duration_hours * RATE_PER_HOUR * rent['qty']

        # return bikes
        self.stock += rent['qty']
        self.current_rental = None

        print("\n--- RENT SUMMARY ---")
        print("Customer:", rent['name'])
        print("Quantity:", rent['qty'])
        print("Start:", rent['start'].strftime("%Y-%m-%d %H:%M:%S"))
        print("End:  ", end.strftime("%Y-%m-%d %H:%M:%S"))
        print("Hours charged:", duration_hours)
        print("Total Amount: ₹", amount)
        print("--------------------\n")

    def status(self):
        if self.current_rental is None:
            print("No active rental.")
        else:
            r = self.current_rental
            print(f"{r['qty']} bike(s) rented to {r['name']} since {r['start'].strftime('%Y-%m-%d %H:%M:%S')}")


def main():
    shop = Bikeshop(100)

    while True:
        try:
            uc = int(input('''
1. Display the stock
2. Rent a bike
3. Return bike
4. Show current rental status
5. Exit
Choose: '''))
        except ValueError:
            print("Enter a valid number.")
            continue

        if uc == 1:
            shop.displaybike()

        elif uc == 2:
            name = input("Customer name: ").strip() or "Guest"
            try:
                qty = int(input("Enter quantity: "))
            except ValueError:
                print("Enter a valid number.")
                continue
            shop.rentforbike(name, qty)

        elif uc == 3:
            shop.returnbike()

        elif uc == 4:
            shop.status()

        elif uc == 5:
            print("Goodbye.")
            break

        else:
            print("Invalid choice, try again.")

if __name__ == "__main__":
    main()
