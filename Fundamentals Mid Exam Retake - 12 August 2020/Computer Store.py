total_no_tax = 0
type_customer = None
total_with_taxes = None
final_price = None

while True:
    part = input()

    if part == "special" or part == "regular":
        type_customer = part
        break

    part = float(part)

    if part < 0:
        print("Invalid price!")
    else:
        total_no_tax += part


if total_no_tax > 0:
    taxes = total_no_tax * 0.20

    if type_customer == "special":
        total_with_taxes = total_no_tax + taxes
        final_price = total_with_taxes - (total_with_taxes * 0.1)

    else:
        final_price = total_no_tax + taxes

    print(f"Congratulations you've just bought a new computer!\n"
            f"Price without taxes: {total_no_tax:.2f}$\n"
            f"Taxes: {taxes:.2f}$\n"
            f"-----------\n"
            f"Total price: {final_price:.2f}$")
else:
    print(f"Invalid order!")

