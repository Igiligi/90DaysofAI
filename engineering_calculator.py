# Day 3 of my 90Day AI/ML Journey
# Built Engineering Calculator: Area of circle, Volume of cylinder, Meters to feet conversion

import math # Imports Python's math library, which gives me access to mathematical constants and functions like math.pi (π).
# Without this, I'd have to type 3.14159 manually. Math.pi is more accurate.

def display_welcome_message():   # Defines a function named display_welcome_message
    """Display welcome message and menu options"""
    print("\n" + "*"*35)
    print("ENGINEERING CALCULATOR".center(35))   # .center(35) centers the text within 35 characters
    print("*"*35)
    print("1. Calculate area of a circle")
    print("2. Calculate volume of a cylinder")
    print("3. Convert meters to feet")
    print("4. Exit")
    print("-"*35)

 # This is input validation function – one of the most important concepts!
def get_positive_number(prompt):  # Function that takes a prompt (the question to ask the user)
    """Get a positive number from user with validation"""
    while True:   # Creates an infinite loop – will keep asking until valid input
        try:   # Attempts to do something that might cause an error
            value = float(input(prompt))   # Shows the prompt, gets user input, converts to float (decimal number)
            if value <= 0:   # Checks if number is zero or negative
                print("❌ Please enter a positive number.")
                continue   # Goes back to the start of the loop (asks again)
            return value   # Exits the function and sends the valid value back
        except ValueError:   # If float() fails (user typed letters), run this code
            print("❌ Invalid input. Please enter a number.")   # Error message, then loop repeats
# Input validation function prevents your program from crashing and ensures you always get valid data.

def circle_area():
    """Calculate area of a circle: πr²"""
    print("\n--- CIRCLE AREA CALCULATOR ---")
    radius = get_positive_number("Enter radius (in meters): ")   # Calls our validation function – reusing code!

    area_of_circle = math.pi * radius ** 2

    print(f"\n📐 Radius: {radius} m")
    print(f"📏 Area: {area_of_circle:.2f} m²")   # Format specifier (area_of_circle:.2f) – shows area of circle with 2 decimal places
    print(f"(using π = {math.pi:.5f})")

    return area   # Returns the value (could be used later)

def cylinder_volume():
    """Calculate volume of a cylinder: πr²h"""
    print("\n--- CYLINDER VOLUME CALCULATOR ---")
    radius = get_positive_number("Enter radius (in meters): ")
    height = get_positive_number("Enter height (in meters): ")

    volume = math.pi * radius ** 2 * height

    print(f"\n📐 Radius: {radius} m")
    print(f"📏 Height: {height} m")
    print(f"🧊 Volume: {volume:.2f} m³")

    return volume
# Same pattern as before, but with two inputs and a different formula.

def meters_to_feet():
    """Convert meters to feet (1 m = 3.28084 ft)"""
    print("\n--- METERS TO FEET CONVERTER ---")
    meters = get_positive_number("Enter length in meters: ")

    feet = meters * 3.28084

    print(f"\n{meters} meters = {feet:.2f} feet")
    print(f"(conversion factor: 1 m = 3.28084 ft)")

    return feet

# main() – The Brain
def main():
    """Main program loop"""
    while True:   # Infinite loop – keeps showing menu until user exits
        display_welcome_message()

        choice = input("\nEnter your choice (1-4): ").strip()   # Gets input and removes extra spaces

        if choice == "1":   # Checks which option user chose
            circle_area()   # Calls the circle area function

        elif choice == "2":
            cylinder_volume()   # Calls the cylinder volume function

        elif choice == "3":
            meters_to_feet()   # Calls the meters to feet function

        elif choice == "4":
            print("\nThank you for using Engineering Calculator. Goodbye!👋")
            break   # Exits the loop completely (ends program)

        else:   # Catches any other input (not 1-4)
            print("\n❌ Invalid choice. Please enter 1, 2, 3, or 4.")

        # Ask if user wants to continue
        if choice in ["1", "2", "3"]:  # Checks if choice is in that list
            input("\n⏎ Press Enter to continue...")

if __name__ == "__main__":   # Python idiom – checks if this file is being run directly (not imported)
    print("🚀 Starting Engineering Calculator...")
    main()   # Calls the main function to start the program
# This allows you to import functions from this file into other programs without automatically running the menu.

# *********************************
# 📚 WHAT I LEARNED TODAY (DAY 3)
# *********************************
#
# 1. FUNCTIONS:
#    - How to define functions using 'def'
#    - Functions help organize code into reusable blocks
#    - Docstrings ("""...""") document what functions do
#
# 2. INPUT VALIDATION:
#    - Using while loops to keep asking until input is valid
#    - try/except to catch errors when converting to float
#    - Checking for positive numbers (value <= 0)
#    - The 'continue' keyword to restart a loop
#
# 3. MATH OPERATIONS:
#    - Using the math library (import math)
#    - math.pi for accurate π value
#    - Exponent operator (**) for squaring numbers
#    - Multiplication for volume and conversion
#
# 4. STRING FORMATTING:
#    - f-strings with variables: f"Radius: {radius}"
#    - Format specifiers: {area:.2f} (2 decimal places)
#    - String multiplication: "*"*35 creates divider lines
#    - .center(35) to center text
#
# 5. PROGRAM FLOW:
#    - Main program loop with while True
#    - if/elif/else for menu choices
#    - break to exit loop
#    - Checking if choice is in a list: if choice in ["1","2","3"]
#    - Using input() to pause the program
#
# 6. PROFESSIONAL PATTERNS:
#    - if __name__ == "__main__": guard
#    - Returning values from functions
#    - Reusing validation function across multiple calculations
#    - Clear function names that describe their purpose
#
# 7. USER EXPERIENCE:
#    - Emojis for visual appeal (📐, 📏, 🧊, 🚀, 📚)
#    - Clear section headers
#    - Pausing so user can read results
#    - Friendly error messages