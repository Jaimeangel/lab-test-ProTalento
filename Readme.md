# IMPORTANTE

# Author : Jaime Angel

## Hay dos archivos main.py y main2.py.

### El primero main.py es un trabajo en el cual se hace todos los test,
sin embargo, 3 de esos test fallaran porque dependen de la hora del dia,
y solamente uno pasara. Porque es la unica correcta posible.

### El segundo main2.py es un test que permite testear cada uno de los
posibles casos, pasando como argumento una hora especifica. De manera que todos los test pasan.



# Reto Curso Django - Ada School
## Reto tomado de wix/tdd-katas

## Greeter
Before you start:
* Try not to read ahead.
* Do one task at a time. The trick is to learn to work incrementally.

This kata demonstrates the problems of static scoped functions and objects.

All tests should always pass, regardless of environment conditions.

* Write a Greeter class with greet function that receives a name as input and outputs Hello <name>. The signature of greet should not change throughout the kata. You are allowed to construct Greeter object as you please.
* greet trims the input
* greet capitalizes the first letter of the name
* greet returns Good morning <name> when the time is 06:00-12:00
* greet returns Good evening <name> when the time is 18:00-22:00
* greet returns Good night <name> when the time is 22:00-06:00
* greet logs into console each time it is called