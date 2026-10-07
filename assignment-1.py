# A simple greeting card generator

print("=== Greeting Card Generator ===")
print()                               # print() with nothing inside prints a blank line

name = input("Who is this card for? ")
occasion = input("What's the occasion? (birthday, graduation, etc.) ")
sender = input("Who is it from? ")

name = name.strip().upper()       # Chaining: strip() runs first, then upper() runs on the result
occasion = occasion.strip().lower()
sender = sender.strip().upper()

print()
print("╔══════════════════════════════╗")
print(f"   Happy {occasion}, {name}!")
print()
print("   Wishing you all the best.")
print(f"   — {sender}")
print("╚══════════════════════════════╝")
