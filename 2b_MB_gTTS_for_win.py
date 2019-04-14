import speech_recognition as sr
from random import *
from gtts import gTTS
import pyglet
import time
import os
from timeit import default_timer as timer

def voice():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)
        print(r.energy_threshold)
        start = timer()
        audio = r.listen(source)
        end = timer()
        print(end - start)
    try:
        comm_words = {"own": "1", "on": "1", "won": "1", "to": "2", "too": "2","tree":"3", "for": "4", "fur": "4",
                      "phor": "4","ford":"4","fight":"5","pipe":"5","pip":"5","sex": "6", "zex": "6","zeban":"7",
                      "salmon":"7","ate":"8","eat":"8","night": "9","nyne":'9',"ben":"10","then":"10"}
        valid = [str(i) for i in range(-50, 50)]
        user = r.recognize_google(audio)
        user = str(user).lower()
        print(user)
        if user in comm_words.keys():
            num = comm_words[user]
            return int(num)
        elif user in valid:
            return int(user)
        else:
            print(user)
            # print("please Say again ")
            make_words_speech("please Say again ", mp3_file='')
            return voice()

    except sr.UnknownValueError :
        print("please Say again Error")
        make_words_speech("please Say again ", mp3_file='')
        return voice()


def make_mp3_file(mp3_file):  # make .mp3 file
        mp3_file = mp3_file + '.wav'
        return str(mp3_file)


def make_words_speech(words, mp3_file):  # use translator api query to get voice
    mp3_file = make_mp3_file(mp3_file)
    mp3_file = "./" + mp3_file
    label = words
    tts = gTTS(label, lang='en')
    tts.save(mp3_file)
    music = pyglet.media.load(mp3_file, streaming=False)
    music.play()
    time.sleep(music.duration)
    os.remove(mp3_file)
    # os.system(mp3_file)


def math():
    num1 = randint(1, 5)
    num2 = randint(1, 5)
    symbol = randint(1, 3)
    if symbol == 1:  # check for postive sign
        print("What is " + str(num1) + "+" + str(num2) + "?" )
        question = num1 + num2
        make_words_speech("What is " + str(num1) + "plus" + str(num2) + "?", mp3_file='')
        answer = voice()
        if int(question) == answer:
            print("its Right Answer")
            make_words_speech("its Right Answer", mp3_file='')
        else:
            print("its wrong Answer")
            make_words_speech("its wrong Answer", mp3_file='')

    elif symbol == 2:  # check for Negative sign
        print("What is " + str(num1) + "-" + str(num2) + "?" )
        question = num1 - num2
        make_words_speech("What is " + str(num1) + "minus" + str(num2) + "?", mp3_file='')
        answer = voice()
        if int(question) == answer:
            print("its Right Answer")
            make_words_speech("its Right Answer", mp3_file='')
        else:
            print("its wrong Answer")
            make_words_speech("its wrong Answer", mp3_file='')

    elif symbol == 3:  # check for Multiply sign
        print("What is " + str(num1) + "*" + str(num2) + "?" )
        question = num1 * num2
        make_words_speech("What is " + str(num1) + "multiply" + str(num2) + "?", mp3_file='')
        answer = voice()
        if int(question) == answer:
            print("its Right Answer")
            make_words_speech("its Right Answer", mp3_file='')
        else:
            print("its wrong Answer")
            make_words_speech("its wrong Answer", mp3_file='')


for i in range(5):
    math()


