import random

print("🎲 Добре дошъл в Number Guessing Game!")
print("Опитай се да познаеш числото от 1 до 100.")

# Генерираме произволно число
secret_number = random.randint(1, 100)
attempts = 0
guess = None

while guess != secret_number:
    try:
        guess = int(input("Въведи число: "))
        attempts += 1

        if guess < secret_number:
            print("🔼 По-голямо е!")
        elif guess > secret_number:
            print("🔽 По-малко е!")
        else:
            print(f"🎉 Позна! Числото беше {secret_number}.")
            print(f"Ти успя за {attempts} опита.")
    except ValueError:
        print("❌ Моля, въведи валидно число!")
