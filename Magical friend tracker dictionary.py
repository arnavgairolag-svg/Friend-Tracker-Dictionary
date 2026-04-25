# 🧙‍♂️✨ Wizard's Magical Phonebook ✨🧙‍♂️
# Using dictionary as the spellbook

import os

# 🎨 Magical colors (works in most terminals)
class Colors:
    HEADER = '\033[95m'
    BLUE = '\033[94m'
    CYAN = '\033[96m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    END = '\033[0m'
    BOLD = '\033[1m'

# 🪄 The grand spellbook dictionary
phone_book = {}

# ✨ Function to clear the screen
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

# 🌟 Add a new friend
def add_friend():
    print(f"{Colors.CYAN}\n╔════════════════════╗")
    print("      Add a Friend      ")
    print("╚════════════════════╝\n" + Colors.END)
    
    name = input("👤 Friend's Name: ").title()
    number = input("📞 Phone Number: ")
    
    if name in phone_book:
        print(f"{Colors.YELLOW}⚠️ {name} is already in your spellbook!{Colors.END}")
    else:
        phone_book[name] = number
        print(f"{Colors.GREEN}✅ {name} has been magically added!{Colors.END}")

# 🔎 Find a friend
def find_friend():
    print(f"{Colors.CYAN}\n╔════════════════════╗")
    print("      Find a Friend      ")
    print("╚════════════════════╝\n" + Colors.END)
    
    name = input("👤 Enter Friend's Name: ").title()
    
    if name in phone_book:
        print(f"{Colors.GREEN}✨ {name}'s number is: {phone_book[name]} ✨{Colors.END}")
    else:
        print(f"{Colors.RED}❌ {name} is not in your spellbook!{Colors.END}")

# 📜 Display all friends
def display_friends():
    print(f"{Colors.CYAN}\n╔════════════════════╗")
    print("      Your Friends      ")
    print("╚════════════════════╝\n" + Colors.END)
    
    if not phone_book:
        print(f"{Colors.RED}😢 Your spellbook is empty!{Colors.END}")
    else:
        for i, (name, number) in enumerate(phone_book.items(), start=1):
            print(f"{Colors.YELLOW}{i}. 👤 {name} ➡️ 📞 {number}{Colors.END}")

# 🧩 Main adventure loop
def magical_phone_adventure():
    while True:
        print(f"{Colors.HEADER}\n✨🪄 Wizard's Magical Phonebook 🪄✨{Colors.END}")
        print(f"{Colors.BLUE}1️⃣ Add a Friend\n2️⃣ Find a Friend\n3️⃣ Display All Friends\n4️⃣ Exit the Spellbook{Colors.END}")
        
        choice = input("Choose your magical action (1-4): ")
        
        if choice == "1":
            clear()
            add_friend()
        elif choice == "2":
            clear()
            find_friend()
        elif choice == "3":
            clear()
            display_friends()
        elif choice == "4":
            print(f"{Colors.GREEN}👋 Farewell, young wizard! May your phonebook stay enchanted! ✨{Colors.END}")
            break
        else:
            print(f"{Colors.RED}❌ Invalid choice! Try again.{Colors.END}")

# 🌈 Start the adventure
magical_phone_adventure()
