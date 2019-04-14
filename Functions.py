# coding=euc-kr
import os
import time
import speech_recognition as sr
import pyaudio
from word2number import w2n
from w2n_k import *
#import MB_gTTS

def make_mp3_file(mp3_file): #make .mp3 file
    mp3_file = mp3_file + '.wav'
    return str(mp3_file)


def speech_func(mp3_file): #play mp3 file in Rpi
    mp3_file = make_mp3_file(mp3_file)
    mp3_file = './' + mp3_file
    #os.system('sudo omxplayer -o local ' + mp3_file)


def make_words_speech(words , mp3_file): # use translator api query to get voice
    mp3_file = make_mp3_file(mp3_file)
    mp3_file = './' + mp3_file
    label = words
    sentence = str('wget -q -U Mozilla -O ' + mp3_file + ' "http://translate.google.com/translate_tts?ie=UTF-8&total=1&idx=0&textlen=32&client=tw-ob&q=' + label + '.&tl=ko-kr"')
    os.system('sudo ' + sentence)


def voice():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)
        print("Answer Please")
        audio = r.listen(source)
    try:
        text = r.recognize_google(audio)
        text = korean_pron(text)
        print(text)
        valid = [str(i) for i in range(-50, 50)] #숫자가 해당 범위에 있는지 확인
        if text in valid: #있으면 숫자 출력
            return int(text)
        else:
            print("11111111111111")
            make_words_speech("please Say again", mp3_file=str(''))
            speech_func(mp3_file=str(''))
            return voice()

    except sr.UnknownValueError:
        print("222222222222222")
        make_words_speech("please Say again", mp3_file=str(''))
        speech_func(mp3_file=str(''))
        return voice()



# def word2num(user_voice): #conver text into numbers
#     try:
#         answer = w2n.word_to_num("{0}".format(user_voice))
#         print(answer)
#         return answer
#     except :
#         print("Please pronounced Correctly")
#         return voice_input()