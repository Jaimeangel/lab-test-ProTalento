import unittest
from datetime import datetime

class Greeter:
    def greet(self, name, now=None):
        # Trim input
        trimmed_name = name.strip().capitalize()
        greeting = ''
        
        # Get current time
        if now is None:
            now = datetime.now()
        hour = now.hour

        # Determine the appropriate greeting based on the time
        if 6 <= hour < 12:
            greeting = 'Good morning'
        elif 12 <= hour < 18:
            greeting = 'Hello'
        elif 18 <= hour < 22:
            greeting = 'Good evening'
        else:
            greeting = 'Good night'

        # Construct the greeting message
        message = f"{greeting} {trimmed_name}"
        print(message)
        # Return the message
        return message

class TestGreeter(unittest.TestCase):
    def test_trim_input_name(self):
        greeter = Greeter()
        result = greeter.greet('  john  ')
        self.assertIn('John', result)

    def test_capitalize_first_letter_of_name(self):
        greeter = Greeter()
        result = greeter.greet('john')
        self.assertIn('John', result)

    def test_greet_good_morning_between_06_00_and_12_00(self):
        greeter = Greeter()
        test_time = datetime(2024, 5, 16, 8, 0, 0)  # 08:00 AM
        result = greeter.greet('john', test_time)
        self.assertTrue(result.startswith('Good morning'))

    def test_greet_good_evening_between_18_00_and_22_00(self):
        greeter = Greeter()
        test_time = datetime(2024, 5, 16, 19, 0, 0)  # 07:00 PM
        result = greeter.greet('john', test_time)
        self.assertTrue(result.startswith('Good evening'))

    def test_greet_good_night_between_22_00_and_06_00(self):
        greeter = Greeter()
        test_time = datetime(2024, 5, 16, 23, 0, 0)  # 11:00 PM
        result = greeter.greet('john', test_time)
        self.assertTrue(result.startswith('Good night'))
        
        test_time = datetime(2024, 5, 16, 5, 0, 0)  # 05:00 AM
        result = greeter.greet('john', test_time)
        self.assertTrue(result.startswith('Good night'))

    def test_greet_hello_between_12_00_and_18_00(self):
        greeter = Greeter()
        test_time = datetime(2024, 5, 16, 14, 0, 0)  # 02:00 PM
        result = greeter.greet('john', test_time)
        self.assertTrue(result.startswith('Hello'))

if __name__ == '__main__':
    unittest.main()
