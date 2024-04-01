def main():
  winning_price = 0.0
  bid = 0.0
  bid_choice = 0
  item_name = ""
  bidder_name = ""

  print("Welcome to the auction!")
  item_name = input("What is the name of the item to be listed? ")

  winning_price = float(input(f"What is the starting bid for {item_name}?\n"))

  print(f"The winning bid for {item_name} is ${winning_price:.2f}")

  bidder_name = input("What is your name? ")

  bid_choice = int(input(f"Hello, {bidder_name}, would you like to bid? (1 for yes, 0 for no)\n"))

  while bid_choice == 1:
      bid = float(input("How much would you like to bid?\n"))

      if winning_price <= bid:
          print(f"Congratulations, {bidder_name}! You won the auction for {item_name}! Please pay within 24 hours.")
          break
      else:
          print(f"Your bid for {item_name} is lower than the winning bid, please bid again.")

      bid_choice = int(input("Would you like to bid again? (1 for yes, 0 for no)\n"))

  print(f"Thank you {bidder_name} for participating in the auction.")

if __name__ == "__main__":
  main()