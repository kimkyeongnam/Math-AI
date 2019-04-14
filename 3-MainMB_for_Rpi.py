from random import *
from Functions import *

def math():
    num1 = randint(1, 5)
    num2 = randint(1, 5)
    symbol = randint(1, 4)
    if symbol == 1: #check for postive sign
        print(str(num1) + "+" + str(num2) + "=?")
        if ((num2 % 10) == 1 or (num2 % 10) == 3 or (num2 % 10) == 6 or (num2 % 10) == 7 or (num2 % 10) == 8 or (num2 % 10) == 0):
            make_words_speech(str(num1) + "더하기" + str(num2) + "은?", mp3_file='')
        elif ((num2 % 10) == 2 or (num2 % 10) == 4 or (num2 % 10) == 5 or (num2 % 10) == 9):
            make_words_speech(str(num1) + "더하기" + str(num2) + "는?", mp3_file='')
        question = num1 + num2
        if question == voice():
            make_words_speech("어머나 천재에요! 정답이에요.", mp3_file=str(num1 + num2))
        else:
            make_words_speech("땡! 틀렸어요.", mp3_file=str(num1 + num2))

    elif symbol == 2:#check for Negative sign
        print(str(num1) + "-" + str(num2) + "=?")
        if ((num2 % 10) == 1 or (num2 % 10) == 3 or (num2 % 10) == 6 or (num2 % 10) == 7 or (num2 % 10) == 8 or (num2 % 10) == 0):
            make_words_speech(str(num1) + "빼기" + str(num2) + "은?", mp3_file='')
        elif ((num2 % 10) == 2 or (num2 % 10) == 4 or (num2 % 10) == 5 or (num2 % 10) == 9):
            make_words_speech(str(num1) + "빼기" + str(num2) + "는?", mp3_file='')
        question = num1 - num2
        if question == voice():
            make_words_speech("어머나 천재에요! 정답이에요.", mp3_file=str(num1 - num2))
        else:
            make_words_speech("땡! 틀렸어요.", mp3_file=str(num1 - num2))

    elif symbol == 3:#check for Division sign
        print(str(num1) + "*" + str(num2) + "=?")
        if ((num2 % 10) == 1 or (num2 % 10) == 3 or (num2 % 10) == 6 or (num2 % 10) == 7 or (num2 % 10) == 8 or (num2 % 10) == 0):
            make_words_speech(str(num1) + "곱하기" + str(num2) + "은?", mp3_file='')
        elif ((num2 % 10) == 2 or (num2 % 10) == 4 or (num2 % 10) == 5 or (num2 % 10) == 9):
            make_words_speech(str(num1) + "곱하기" + str(num2) + "는?", mp3_file='')
        question = num1 * num2
        if question == voice():
            make_words_speech("어머나 천재에요! 정답이에요.", mp3_file=str(num1 * num2))
        else:
            make_words_speech("땡! 틀렸어요.", mp3_file=str(num1 * num2))

    elif symbol == 4:#check for Division sign
        print(str(num1) + "/" + str(num2) + "=?")
        if ((num2 % 10) == 1 or (num2 % 10) == 3 or (num2 % 10) == 6 or (num2 % 10) == 7 or (num2 % 10) == 8 or (num2 % 10) == 0):
            make_words_speech(str(num1) + "나누기" + str(num2) + "은?", mp3_file='')
        elif ((num2 % 10) == 2 or (num2 % 10) == 4 or (num2 % 10) == 5 or (num2 % 10) == 9):
            make_words_speech(str(num1) + "나누기" + str(num2) + "는?", mp3_file='')
        question = num1 / num2
        if question == voice():
            make_words_speech("어머나 천재에요! 정답이에요.", mp3_file=str(num1 / num2))
        else:
            make_words_speech("땡! 틀렸어요.", mp3_file=str(num1 / num2))



for i in range(10):
    math()
