from random import * #Random Liberary * mean All
import speech_recognition as sr
import pyaudio

r=sr.Recognizer()

def math():
    num1 = randint(1,10)
    num2 = randint(1, 10)
    symbol = randint(1,3)
    if symbol == 1:
        question = int(input("What is " + str(num1) + "+" + str(num2) + "?"))
        answer = num1 + num2
        if question == answer:
            print("You are Genius! its Right Answer")
        else:
            print("You loss! wrong Answer")

    elif symbol == 2:
        question = int(input("What is " + str(num1) + "-" + str(num2) + "?"))
        answer = num1 - num2
        if question == answer:
            print("You are Genius! its Right Answer")
        else:
            print("You loss! wrong Answer")

    elif symbol == 3:
        question = int(input("What is " + str(num1) + "*" + str(num2) + "?"))
        answer = num1 * num2
        if question == answer:
            print("You are Genius! its Right Answer")
        else:
            print("You loss! wrong Answer")


for i in range(10):
    math()
