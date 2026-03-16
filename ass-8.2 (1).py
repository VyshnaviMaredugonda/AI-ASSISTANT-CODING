#generate a code with strong password in python and generate a  unit test test cases  to check the funtionality of the password generator.
import random
import string
def generate_strong_password(length):
    if length < 8:
        raise ValueError("Password length should be at least 8 characters.")
    
    # Define the character sets
    uppercase_letters = string.ascii_uppercase
    lowercase_letters = string.ascii_lowercase
    digits = string.digits
    special_characters = string.punctuation
    
    # Ensure the password includes at least one character from each set
    password = [
        random.choice(uppercase_letters),
        random.choice(lowercase_letters),
        random.choice(digits),
        random.choice(special_characters)
    ]
    
    # Fill the remaining length with a mix of all character sets
    all_characters = uppercase_letters + lowercase_letters + digits + special_characters
    password += random.choices(all_characters, k=length - 4)
    
    # Shuffle the password list to ensure randomness
    random.shuffle(password)
    
    # Join the list into a string and return
    return ''.join(password)
# Unit test cases for the password generator
import unittest
class TestPasswordGenerator(unittest.TestCase):
    def test_password_length(self):
        password = generate_strong_password(12)
        self.assertEqual(len(password), 12)

    def test_password_contains_uppercase(self):
        password = generate_strong_password(12)
        self.assertTrue(any(char.isupper() for char in password))

    def test_password_contains_lowercase(self):
        password = generate_strong_password(12)
        self.assertTrue(any(char.islower() for char in password))

    def test_password_contains_digits(self):
        password = generate_strong_password(12)
        self.assertTrue(any(char.isdigit() for char in password))

    def test_password_contains_special_characters(self):
        password = generate_strong_password(12)
        self.assertTrue(any(char in string.punctuation for char in password))

    def test_password_length_too_short(self):
        with self.assertRaises(ValueError):
            generate_strong_password(6)
if __name__ == '__main__':
    unittest.main()