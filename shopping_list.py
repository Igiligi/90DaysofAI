# Day 4 of my 90Day AI/ML Journey
# Shopping List App: Add, remove, view, and sort items
from multiprocessing.reduction import duplicate
from random import choice

from shopping_list2 import clear_list


def show_menu():
    """Displays the Menu"""
    print("\n" + "*" * 35)
    print("🛒 YOUR SHOPPING LIST APP".center(35)) # Keeps the output at the center of 35 spaces or characters
    print("*" * 35)
    print("1. 📝 Add shopping item")
    print("2. ❌ Remove shopping item")
    print("3. 👁 View shopping list/items")
    print("4. 🛒 Sort shopping list/items")
    print("5. ✂ Clear shopping list/items")
    print("6. Exist")

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

def remove_item(shopping_list):
    """To remove item from the list"""
    print("--- REMOVE ITEM---")


    if len(shopping_list) == 0:
        print(f"Their is no item in your list to remove")
        return shopping_list

    else:
        print(f"📝 Your Current list ({len(shopping_list)} items):")
        for item in sorted(shopping_list):  # Iteration: continues to print out the items in the list from first to last
            print(f"   • {item}")

        remove_item = input("\n Enter item to remove: ").strip().lower()
        if remove_item in shopping_list:
            shopping_list.remove(remove_item)
            print(f"'{remove_item}' removed from the list")
        else:
            print(f"'{remove_item}' not in list")

    return shopping_list

def view_item(shopping_list):
    """To view the items in your list"""
    if len(shopping_list) == 0:
        print(f"\n Their is no item in your list")
        return shopping_list
    else:
        print(f"\n ---ITEMS IN YOUR LIST---")
        for item in shopping_list:
            print(f" ∎ {item}")

    return shopping_list

def sort_item(shopping_list):
    """To sort your items alphabetically"""
    if len(shopping_list) == 0:
        print(f"\n Their is no item in your list")
        return shopping_list
    else:
        print(f"\n ---YOUR SORTED LIST---")
        for item in sorted(shopping_list):
            print(f" ∎ {item}")

def clear_list(shopping_list):
    if len(shopping_list) == 0:
        print(f"\n Their is no item in your list to clear")

    elif len(shopping_list) > 0:
        clear_list = input("\nAre you sure you want to clear ALL items in your list? YES OR NO? ").strip().lower()
        if clear_list == "yes":
            shopping_list.clear()
            print(f"\nYour shopping list is cleared!")

        else:
            print(f"Shopping List NOT Cleared!")

    return shopping_list
# The main program
def main():
    """loop function"""
    shopping_list = []

    while True:
        show_menu()
        choice = input("\n Enter your choice (1-6): ").strip()

        if choice == "1":
            add_item(shopping_list)

        elif choice == "2":
            remove_item(shopping_list)

        elif choice == "3":
            view_item(shopping_list)

        elif choice == "4":
            sort_item(shopping_list)

        elif choice == "5":
            clear_list(shopping_list)

        elif choice == "6":
            print("\nThank you for using the SHOPPING LIST APP 🤗. Happy shopping!")
            if shopping_list:
                print(f"📝 Your final list ({len(shopping_list)} items):")
                for item in sorted(shopping_list):
                    print(f"   • {item}")
            break

        else:
            print("\n❌ Invalid choice. Please enter 1, 2, 3, 4, or 5.")

        # Pause after actions (except exit)
        if choice in ["1", "2", "3", "4", "5"]:
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
