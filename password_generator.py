
import random
import string

def generate_password(length=12, use_digits=True, use_specials=True):
    chars = string.ascii_letters
    if use_digits:
        chars += string.digits
    if use_specials:
        chars += string.punctuation

    password = ''.join(random.choice(chars) for _ in range(length))
    return password

def main():
    print("🔐 Password Generator")
    try:
        length = int(input("Enter password length (e.g., 12): "))
        use_digits = input("Include digits? (y/n): ").strip().lower() == 'y'
        use_specials = input("Include special characters? (y/n): ").strip().lower() == 'y'

        password = generate_password(length, use_digits, use_specials)
        print(f"✅ Generated Password: {password}")
    except Exception as e:
        print(f"❌ Error: {e}")

if __name__ == "__main__":
    main()
