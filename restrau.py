# ==========================================================
# RESTAURANT MANAGEMENT SYSTEM (RMS)
# Built using Python (Functions, Dictionaries, Loops)
# ==========================================================

import time

# Nested Dictionary for Menu Storage (O(1) fast lookup)
MENU = {
    "Starters": {
        "Spring Rolls": 150,
        "Garlic Bread": 120,
        "Tomato Soup": 100,
        "Paneer Tikka": 220
    },
    "Main Course": {
        "Burger": 250,
        "Pizza": 400,
        "Pasta": 300,
        "Paneer Butter Masala": 350,
        "Fried Rice": 220
    },
    "Beverages": {
        "Coke": 60,
        "Iced Tea": 90,
        "Cold Coffee": 120,
        "Mineral Water": 30
    },
    "Desserts": {
        "Ice Cream": 120,
        "Chocolate Brownie": 150,
        "Gulab Jamun": 100
    }
}

def display_menu():
    """Displays the categorized menu with prices neatly."""
    print("\n" + "="*45)
    print(" " * 14 + "🍽️ MENU CARD 🍽️")
    print("="*45)
    for category, items in MENU.items():
        print(f"\n📂 [{category}]")
        for item, price in items.items():
            print(f"   • {item:<22} : ₹{price}")
    print("="*45)

def restaurant_system():
    cart = {}
    print("\n" + "★"*55)
    print("       WELCOME TO PYTHON BISTRO & RESTAURANT       ")
    print("★"*55)
    
    while True:
        display_menu()
        item_input = input("\nEnter the item name you want to order (or type 'done' to finish): ").strip().title()
        
        # Exit condition for ordering
        if item_input.lower() == 'done':
            break
            
        # Check if item exists in menu dictionary
        found = False
        item_price = 0
        for category, items in MENU.items():
            if item_input in items:
                found = True
                item_price = items[item_input]
                break
                
        if found:
            try:
                qty_input = input(f"Enter quantity for {item_input}: ")
                qty = int(qty_input)
                
                if qty <= 0:
                    print("❌ Quantity must be greater than 0. Please try again.")
                    continue
                
                # Add or update item in cart
                if item_input in cart:
                    cart[item_input]['qty'] += qty
                else:
                    cart[item_input] = {
                        'price': item_price,
                        'qty': qty
                    }
                print(f"✅ Added {qty} x {item_input}(s) to your cart.")
                
            except ValueError:
                print("❌ Invalid quantity! Please enter a valid number.")
        else:
            print("❌ Item not found in the menu! Please check your spelling.")

    # Bill Generation Section
    if not cart:
        print("\n❌ No items ordered. Thank you for visiting Python Bistro!")
        return

    print("\n" + "═"*55)
    print("                 FINAL INVOICE / RECEIPT                  ")
    print("═"*55)
    print(f"{'Item Name':<22} | {'Qty':<5} | {'Price':<7} | {'Total':<8}")
    print("-" * 55)
    
    subtotal = 0
    for item, details in cart.items():
        item_total = details['price'] * details['qty']
        subtotal += item_total
        print(f"{item:<22} | {details['qty']:<5} | ₹{details['price']:<6} | ₹{item_total:<7}")
        
    tax = subtotal * 0.05  # 5% GST Calculation
    grand_total = subtotal + tax
    
    print("-" * 55)
    print(f"{'Subtotal:':<38} ₹{subtotal:.2f}")
    print(f"{'GST (5%):':<38} ₹{tax:.2f}")
    print("=" * 55)
    print(f"{'Grand Total:':<38} ₹{grand_total:.2f}")
    print("=" * 55)
    print("        Thank you for dining with us! Please visit again.     ")
    print("═"*55)

if __name__ == "__main__":
    restaurant_system()
