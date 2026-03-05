# Day 4 of my 90Day AI/ML Journey
# Shopping List App: Add, remove, view, and sort items
from random import choice

def show_menu():
    """Displays the Menu"""
    print("\n" + "*" * 35)
    print("🛒 YOUR SHOPPING LIST APP".center(35)) # Keeps the output at the center of 35 spaces or characters
    print("*" * 35)
    print("1. 📝 Add shopping item")
    print("2. ❌ Remove shopping item")
    print("3. 👁 View shopping list/items")
    print("4. 🛒 Sort shopping list/items")
    print("5. Exist")

def add_item(shopping_list):
    """Adds item to the list"""
    print(" ---ADD ITEM---")
    item = input("Enter item name: ").strip().lower()

    if not item:
        print("Item cannot be empty.")
        return shopping_list

    if item in shopping_list:
        print(f"'{item}' is already in your list.")
        choice = input("Add again? (y/n): ").strip().lower()
        if choice == 'y':
            shopping_list.append(item)
            print(f"✅ Added '{item}' (duplicate)")
        else:
            print("❌ Not added.")
    else:
        shopping_list.append(item)
        print(f"✅ '{item}' is successfully added  to your list.")
    return shopping_list

def remove_item():
    """To remove item from the list"""
    print("--- REMOVE ITEM---")

    pass
def view_item():
    pass
def sort_item():
    pass

# The main program
def main():
    """loop function"""
    shopping_list = []

    while True:
        show_menu()
        choice = input("\n Enter your choice (1-5): ").strip()

        if choice == "1":
            add_item(shopping_list)

        elif choice == "2":
            remove_item()

        elif choice == "3":
            view_item()

        elif choice == "4":
            sort_item()

        elif choice == "5":
            print("\nThank you for using the SHOPPING LIST APP 🤗. Happy shopping!")
            if shopping_list:
                print(f"📝 Your final list ({len(shopping_list)} items):")
                for item in sorted(shopping_list):
                    print(f"   • {item}")
            break

        else:
            print("\n❌ Invalid choice. Please enter 1, 2, 3, 4, or 5.")

        # Pause after actions (except exit)
        if choice in ["1", "2", "3", "4"]:
            input("\n⏎ Press Enter to continue...")



# Run the program
if __name__ == "__main__":
    main()

# ============================================
#       WHAT I LEARNED TODAY (DAY 4)
# ============================================
#
# 1. LISTS:
#    - Lists are ordered, mutable collections: shopping_list = []
#    - Can store any data type (strings, numbers, etc.)
#    - Index starts at 0
#
# 2. LIST METHODS:
#    - .append(item) – adds item to end
#    - .remove(item) – removes first occurrence
#    - .clear() – removes all items
#    - .count(item) – counts occurrences
#    - .sort() – sorts in-place (modifies original)
#
# 3. SORTED() FUNCTION:
#    - sorted(list) returns NEW sorted list (original unchanged)
#    - Great for viewing without modifying
#
# 4. ENUMERATE():
#    - for i, item in enumerate(list, 1):
#    - Gives both index and value
#    - Start parameter (1) makes numbering start at 1
#
# 5. SETS FOR UNIQUE ITEMS:
#    - set(list) converts list to set (removes duplicates)
#    - len(set(list)) counts unique items
#
# 6. INPUT CLEANING:
#    - .strip() removes extra spaces
#    - .lower() makes comparison case-insensitive
#
# 7. VALIDATION PATTERNS:
#    - Check if list is empty before removing
#    - Check if item exists before removing
#    - Confirm before destructive actions (clear)
#
# 8. USER EXPERIENCE:
#    - Show current list before asking what to remove
#    - Show statistics (total items, duplicates)
#    - Friendly messages with emojis
#    - Final summary on exit