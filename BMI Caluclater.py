def bmi_calculator():
    name = input("Enter your name: ")
    print(f"\nHello {name}! Welcome to the BMI Calculator \n")

    while True:
        weight = float(input("Enter your weight in kg: "))
        height = float(input("Enter your height in meters: "))

        bmi_value = weight / (height ** 2)
        print(f"\n{name}, your Body Mass Index (BMI) is: {round(bmi_value, 2)}")

        if bmi_value < 18.5:
            print("You are Underweight.")
            print(" Try to eat more nutritious and balanced meals.")
        elif bmi_value < 24.9:
            print("You have Normal weight.")
            print(" Great! Keep maintaining a healthy lifestyle.")
        elif bmi_value < 29.9:
            print("You are Overweight.")
            print(" Consider regular exercise and a healthy diet.")
        else:
            print("You are Obese.")
            print(" Please consult a doctor or dietitian for advice.")

        print("\nHealthy BMI range is 18.5 – 24.9 ")

        again = input("\nDo you want to calculate again? (yes/no): ").lower()
        if again != "yes":
            print(f"\nThank you, {name}! Stay healthy and take care! ")
            break

# Run the program
bmi_calculator()
