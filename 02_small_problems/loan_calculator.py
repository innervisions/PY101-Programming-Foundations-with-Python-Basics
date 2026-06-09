def prompt(message):
    print(f"==> {message}")


def invalid_number(number_str):
    try:
        number = float(number_str)
        if number <= 0:
            raise ValueError(f"Value must be > 0: {number_str}")
    except ValueError:
        return True

    return False


while True:
    prompt("Welcome to the Loan Calculator!")
    prompt("Please enter the loan amount in dollars:")
    loan_amount = input()
    while invalid_number(loan_amount):
        prompt("That is not a valid amount.")
        prompt("Please enter the loan amount in dollars:")
        loan_amount = input()

    prompt("Please enter the APR in %:")
    apr = input()
    while invalid_number(apr):
        prompt("That is not a valid APR.")
        prompt("Please enter the APR in %:")
        apr = input()

    prompt("Please enter the loan duration in months:")
    duration = input()
    while invalid_number(duration):
        prompt("That is not a valid duration.")
        prompt("Please enter the loan duration in months:")
        duration = input()

    loan_amount = float(loan_amount)
    apr = float(apr)
    duration = float(duration)
    monthly_interest_rate = apr / 12 * 0.01
    monthly_payment = loan_amount * (
        monthly_interest_rate / (1 - (1 + monthly_interest_rate) ** (-duration))
    )
    prompt(f"Your monthly payment is ${monthly_payment:.2f}.")

    prompt("Another calculation?")
    answer = input().lower()
    while True:
        if answer.startswith("n") or answer.startswith("y"):
            break
        prompt('Please enter "y" or "n".')
        answer = input().lower()

    if answer[0] == "n":
        break
