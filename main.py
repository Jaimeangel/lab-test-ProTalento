import unittest
from datetime import datetime

class Greeter:
    def greet(self, name):
        # Trim input
        trimmed_name = name.strip().capitalize()
        greeting=''
        # Get current time
        now = datetime.now()
        hour = now.hour

        # Determine the appropriate greeting based on the time
        if 6 <= hour < 12:
            greeting = 'Good morning'
        elif 18 <= hour < 22:
            greeting = 'Good evening'
        elif 22 <= hour < 6:
            greeting = 'Good night'
        else:
            greeting = 'Hello'

        # Construct the greeting message with both "Hello" and the time-based greeting
        message = f"{greeting} {trimmed_name}"
        # Return the message
        print(message)
        return message

# Dependiendo de la hora del dia el saludo sera diferente
# Esto quiere decir siempre habran 3 test que fallaran
# Debido a que solo es posible que se retorne un saludo de los cuatro posibles
# Segun la hora
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
        result = greeter.greet('john')
        self.assertTrue(result.startswith('Good morning'))

    def test_greet_good_evening_between_18_00_and_22_00(self):
        greeter = Greeter()
        result = greeter.greet('john')
        self.assertTrue(result.startswith('Good evening'))

    def test_greet_good_night_between_22_00_and_06_00(self):
        greeter = Greeter()
        result = greeter.greet('john')
        self.assertTrue(result.startswith('Good night'))
    
    def test_greet_good_night_between_12_00_and_18_00(self):
        greeter = Greeter()
        result = greeter.greet('john')
        self.assertTrue(result.startswith('Hello'))


if __name__ == '__main__':
    unittest.main()