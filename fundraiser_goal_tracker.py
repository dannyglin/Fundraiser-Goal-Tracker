def track_fundraiser(goal_amount, current_amount):
    amount_left = goal_amount - current_amount
    percentage_achieved = (current_amount / goal_amount) * 100

    print(f"Current amount raised: ${current_amount}")
    print(f"Percentage achieved: {percentage_achieved:.1f}%")
    print(f"Amount left to reach the goal: ${amount_left}")

def main():
    print("Welcome to the Fundraiser Tracker!")
    try:
        goal_amount = float(input("Please input your fundraising goal amount: $"))
        current_amount = float(input("Please input the current amount raised: $"))

        if goal_amount < 0 or current_amount < 0:
            print("Please enter positive amounts.")
        elif current_amount > goal_amount:
            print("The current amount raised exceeds the fundraising goal!")
        else:
            track_fundraiser(goal_amount, current_amount)
    except ValueError:
        print("Invalid input. Please enter a valid amount.")

if __name__ == "__main__":
    main()
