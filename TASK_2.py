def calculate_bmi(weight, height):
    """Calculate BMI and classify it into categories."""
    bmi = weight / (height ** 2)

    if bmi < 18.5:
        category = "Underweight"
    elif 18.5 <= bmi < 25:
        category = "Normal Weight"
    elif 25 <= bmi < 30:
        category = "Overweight"
    else:
        category = "Obese"

    return bmi, category

def get_user_input():
    """Prompt users for weight and height inputs."""
    try:
        weight = float(input("Enter your weight in kilograms: "))
        height = float(input("Enter your height in meters: "))
        return weight, height
    except ValueError:
        print("Invalid input. Please enter numeric values.")
        return get_user_input()

if __name__ == "__main__":
    print("BMI Calculator")

    weight, height = get_user_input()

    bmi, category = calculate_bmi(weight, height)

    print(f"Your BMI is: {bmi:.2f}")
    print(f"Category: {category}")
