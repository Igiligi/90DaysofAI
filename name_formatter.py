# Day 2 of my 90Day AI/ML Journey
# Script: name_formatter.py
# What it does: Takes a full name and displays various formats + character count + word count

# --- MY CODE TODAY (DAY 2) ---

# Get user information (full name) using input function
full_name = input("Please enter your full name: ").strip()   # Asks for full name and quickly cleans space(s)

# Display VARIOUS FORMATS
print("\n" + "*"*34)   # Gives a line space and creates a line of 34 equal signs (*)
print("YOUR FULL NAME IN VARIOUS FORMATS")
print("*"*34)

# Various format outputs
print(f"Lowercase: {full_name.lower()}")   # prints the user full name in lowercase
print(f"Uppercase: {full_name.upper()}")   # prints the user full name in uppercase
print(f"Titlecase: {full_name.title()}")   # prints the user full name with each word capitalized

# Original full name inputed by the user (to show what .strip() did)
print(f"Original full name entered: '{full_name}' (spaces removed from ends)")

# CHARACTER COUNT (with and without spaces)
print("\n" + "*"*16)
print("CHARACTER COUNT")
print("*"*16)

# various count outputs
character_with_spaces = len(full_name)   # Character count with spaces
character_without_spaces = len(full_name.replace(" ", ""))   # Character count without spaces
print(f"Total Characters (including spaces): {character_with_spaces}")   # prints the number of characters (including spaces) in the user full name
print(f"Total Characters (excluding spaces): {character_without_spaces}")   # prints the number of characters (excluding spaces) in the user full name

# WORD COUNT
print("\n" + "*"*11)
print("WORD COUNT")
print("*"*11)

# Count words
word_count = len(full_name.split())   # Converts the string to lists, and counts how many items are in that list
print(f"Number of words: {word_count}")

# Appreciate user for using the Name-Formatter
print("\n" + "✨"*19)
print("Thank you for using the Name-Formatter 😊")
print("✨"*19)


# --- WHAT I LEARNED TODAY (DAY 2) ---
"""
=== STRING METHODS ===
1. .lower() - Converts ALL characters to lowercase
   Example: "IGILIGI".lower() → "igiligi"

2. .upper() - Converts ALL characters to uppercase
   Example: "igiligi".upper() → "IGILIGI"

3. .title() - Capitalizes first letter of EVERY word
   Example: "chibueze igiligi".title() → "Chibueze Igiligi"

4. .split() - Cuts a string into a LIST of words (removes extra spaces)
   Example: "chibueze   igiligi".split() → ['chibueze', 'igiligi']

5. .replace(" ", "") - Removes all spaces (for counting without spaces)
   Example: "chibueze igiligi".replace(" ", "") → "chibuezeigiligi"

=== BUILT-IN FUNCTIONS ===
6. len() - Counts items in a list OR characters in a string
   Example: len(['chibueze', 'igiligi']) → 2
   Example: len("chibueze") → 8

=== KEY INSIGHTS ===
- String methods don't change the original string (strings are IMMUTABLE)
- .split() is powerful for cleaning messy user input
- You can chain methods like .strip().title() (do in order: clean THEN format)
- f-strings make printing variables MUCH cleaner than concatenation (+)

=== NEW OPERATOR ===
- String multiplication: "*"*34 creates a line of 34 equal signs
- Works with any character/emoji: "✨"*19 creates 19 sparkles emoji

How I got the Emoji for the art seperator on windows
1. Press Windows Key + . (period) or Windows Key + ; (semicolon)
2. Emoji picker appears
3. Search for "sparkle" or "star"
4. Click the ✨ emoji

To copy a line of code in PyCharm
1) Place your cursor on the line.
2) Press ctrl + D (windows/Linux)

# print(help(str)) - returns explanation of all string methods in python
# print(help(str.count)) - returns only the explanation of the specified string method '.count'
"""