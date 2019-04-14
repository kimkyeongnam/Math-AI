from random import *
import speech_recognition as sr
from gtts import gTTS
import pyglet
import time
from w2n_k import *

r = sr.Recognizer()


def how_much():
    r0 = sr.Recognizer()
    with sr.Microphone() as num:
        r0.adjust_for_ambient_noise(num)
        how_much_play = r0.listen(num)

    try:
        text_num = r0.recognize_google(how_much_play)
        text_num = korean_pron(text_num)
        print(text_num)
        valid = [str(i) for i in range(0, 10)]
        if text_num in valid:
            how_much_play_pro = int(text_num)
            return how_much_play_pro
        else:
            print("인식 범위를 벗어났네요. 다시 말해주세요.")
            make_words_speech("인식 범위를 벗어났네요. 다시 말해주세요.", mp3_file='')
            return how_much()


    except sr.UnknownValueError:
        print("인식이 안 되네요. 다시 말해 주세요")
        make_words_speech("인식이 안 되네요. 다시 말해 주세요 ", mp3_file='')
        speech_func(mp3_file=str(''))
        return how_much()


def make_mp3_file(mp3_file):  # make .mp3 file
        mp3_file = mp3_file + '.wav'
        return str(mp3_file)


def speech_func(mp3_file): #play mp3 file in Rpi
    mp3_file = make_mp3_file(mp3_file)
    mp3_file = './' + mp3_file



def make_words_speech(words, mp3_file):  # use translator api query to get voice
        mp3_file = make_mp3_file(mp3_file)
        mp3_file = "./" + mp3_file
        label = words
        tts = gTTS(label, lang='ko')
        tts.save(mp3_file)
        music = pyglet.media.load(mp3_file, streaming=False)
        music.play()
        time.sleep(music.duration)


def voice():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)
        print("정답을 말해주세요")
        make_words_speech("정답을 말해주세요", mp3_file='')
        audio = r.listen(source)
    try:
        text = r.recognize_google(audio)
        text = korean_pron(text)
        print(text)
        valid = [str(i) for i in range(-1000000, 1000000)]
        if text in valid:
            num_text = int(text)
            return num_text

    except sr.UnknownValueError:
        print("인식이 안 되네요. 다시 말해 주세요")
        make_words_speech("인식이 안 되네요. 다시 말해 주세요 ", mp3_file='')
        speech_func(mp3_file=str(''))
        return voice()


def math():
    num1 = randint(0, 10) #임의의 숫자 num1 생성
    num2 = randint(0, 10) #임의의 숫자 num2 생성
    symbol = randint(1, 4) #연산자 +,-,*,/ 중 임의로 하나 선택

    if symbol == 1:  # +연산인 경우
        print(str(num1) + "+" + str(num2) + "=?")
        # 일의 자리에 따라 은/는 읽어야 하는 발음 다르므로 %10해서 구분하기
        if((num2%10)==1 or (num2%10)==3 or (num2%10)==6 or (num2%10)==7 or (num2%10)==8 or (num2%10)==0):
            make_words_speech( str(num1) + "더하기" + str(num2) + "은?", mp3_file='')
        elif ((num2%10)==2 or (num2%10)==4 or (num2%10)==5 or (num2%10)==9):
            make_words_speech(str(num1) + "더하기" + str(num2) + "는?", mp3_file='')
        question = num1 + num2
        answer = voice()
        if int(question) == answer: #question(문제의 정답) == answer(음성인식으로 받아들인 값)
            print("어머나 천재에요! 정답이에요.")
            make_words_speech("어머나 천재에요! 정답이에요.", mp3_file='')
        else:
            print("땡! 틀렸어요")
            make_words_speech("땡! 틀렸어요", mp3_file='')
            print("기회를 한 번 더 드릴게요.")
            make_words_speech("기회를 한 번 더 드릴게요.", mp3_file='')
            newanswer = voice()
            if(int(question) == newanswer):
                print("어머나 천재에요! 정답이에요.")
                make_words_speech("어머나 천재에요! 정답이에요.", mp3_file='')
            else:
                print("땡! 틀렸어요. 다음 문제로 넘어갈게요.")
                make_words_speech("땡! 틀렸어요. 다음 문제로 넘어갈게요.", mp3_file='')

    elif symbol == 2:  # -연산인 경우
        print(str(num1) + "-" + str(num2) + "=?")
        if ((num2%10)==1 or (num2%10)==3 or (num2%10)==6 or (num2%10)==7 or (num2%10)==8 or (num2%10)==0):
            make_words_speech( str(num1) + "빼기" + str(num2) + "은?", mp3_file='')
        elif ((num2%10)==2 or (num2%10)==4 or (num2%10)==5 or (num2%10)==9):
            make_words_speech(str(num1) + "빼기" + str(num2) + "는?", mp3_file='')
        question = num1 - num2
        answer = voice()
        if int(question) == answer:
            print("어머나 천재에요! 정답이에요.")
            make_words_speech("어머나 천재에요! 정답이에요.", mp3_file='')
        else:
            print("땡! 틀렸어요")
            make_words_speech("땡! 틀렸어요", mp3_file='')
            print("기회를 한 번 더 드릴게요.")
            make_words_speech("기회를 한 번 더 드릴게요.", mp3_file='')
            newanswer = voice()
            if (int(question) == newanswer):
                print("어머나 천재에요! 정답이에요.")
                make_words_speech("어머나 천재에요! 정답이에요.", mp3_file='')
            else:
                print("땡! 틀렸어요. 다음 문제로 넘어갈게요.")
                make_words_speech("땡! 틀렸어요. 다음 문제로 넘어갈게요.", mp3_file='')

    elif symbol == 3:  # *연산인 경우
        print(str(num1) + "*" + str(num2) + "=?")
        if ((num2%10)==1 or (num2%10)==3 or (num2%10)==6 or (num2%10)==7 or (num2%10)==8 or (num2%10)==0):
            make_words_speech( str(num1) + "곱하기" + str(num2) + "은?", mp3_file='')
        elif ((num2%10)==2 or (num2%10)==4 or (num2%10)==5 or (num2%10)==9):
            make_words_speech(str(num1) + "곱하기" + str(num2) + "는?", mp3_file='')
        question = num1 * num2
        answer = voice()
        if int(question) == answer:
            print("어머나 천재에요! 정답이에요.")
            make_words_speech("어머나 천재에요! 정답이에요.", mp3_file='')
        else:
            print("땡! 틀렸어요")
            make_words_speech("땡! 틀렸어요", mp3_file='')
            print("기회를 한 번 더 드릴게요.")
            make_words_speech("기회를 한 번 더 드릴게요.", mp3_file='')
            newanswer = voice()
            if (int(question) == newanswer):
                print("어머나 천재에요! 정답이에요.")
                make_words_speech("어머나 천재에요! 정답이에요.", mp3_file='')
            else:
                print("땡! 틀렸어요. 다음 문제로 넘어갈게요.")
                make_words_speech("땡! 틀렸어요. 다음 문제로 넘어갈게요.", mp3_file='')

    elif symbol == 4:  # /연산인 경우
        if num2 == 0: #분모는 0이 되면 안되므로, num2가 0일 땐, 0이 아닌 수가 나오도록 randint 돌려줘야 함
           num2 = randint(1, 10)
        print(str(num1) + "/" + str(num2) + "=?")
        if ((num2%10)==1 or (num2%10)==3 or (num2%10)==6 or (num2%10)==7 or (num2%10)==8 or (num2%10)==0):
            make_words_speech(str(num1) + "나누기" + str(num2) + "은?", mp3_file='')
        elif ((num2%10)==2 or (num2%10)==4 or (num2%10)==5 or (num2%10)==9):
            make_words_speech(str(num1) + "나누기" + str(num2) + "는?", mp3_file='')
        question = num1 / num2
        answer = voice()
        if int(question) == answer:
            print("어머나 천재에요! 정답이에요.")
            make_words_speech("어머나 천재에요! 정답이에요.", mp3_file='')
        else:
            print("땡! 틀렸어요")
            make_words_speech("땡! 틀렸어요", mp3_file='')
            print("기회를 한 번 더 드릴게요.")
            make_words_speech("기회를 한 번 더 드릴게요.", mp3_file='')
            newanswer = voice()
            if(int(question) == newanswer):
                print("어머나 천재에요! 정답이에요.")
                make_words_speech("어머나 천재에요! 정답이에요.", mp3_file='')
            else:
                print("땡! 틀렸어요. 다음 문제로 넘어갈게요.")
                make_words_speech("땡! 틀렸어요. 다음 문제로 넘어갈게요.", mp3_file='')


#---------몇 번 실행할 지를 사용자가 입력하게 하는 경우---------#

print("몇 번 실행하시겠어요? 실행할 횟수를 말해주세요. 최대 실행 횟수는 10번입니다.")  # 사용자 설정
make_words_speech("몇 번 실행하시겠어요? 실행할 횟수를 말해주세요. 최대 실행 횟수는 열번입니다.", mp3_file='')

play_time = how_much()

print("게임 룰을 설명해드리겠습니다. 다음 챗봇이 내는 수학 문제에 대한 답을 말해주시면 됩니다.")
make_words_speech("게임 룰을 설명해드리겠습니다. 다음 챗봇이 내는 수학 문제에 대한 답을 말해주시면 됩니다. 이 게임은 처음 선택하신 횟수만큼 진행됩니다. 나누기의 경우 소수점을 제외한 정수 부분만 말해주시면 됩니다.", mp3_file='')
#
# print("이 게임은 처음 선택하신 횟수만큼 진행됩니다. 나누기의 경우 소수점을 제외한 정수 부분만 말해주시면 됩니다.")
# make_words_speech("이 게임은 처음 선택하신 횟수만큼 진행됩니다. 나누기의 경우 소수점을 제외한 정수 부분만 말해주시면 됩니다.", mp3_file='')

print("그럼 시작하겠습니다.") #끝난 후
make_words_speech("그럼 시작하겠습니다.", mp3_file='')

for i in range(play_time): #입력받은 값 만큼 math 실행
    math()

print("수고하셨습니다") #끝난 후
make_words_speech("수고하셨습니다", mp3_file='')



#---------실행할 횟수를 초기화 하는 경우(ex)10번)---------#
# for i in range(10): #math 실행
#     math()
#
# print("수고하셨습니다") #끝난 후
# make_words_speech("수고하셨습니다", mp3_file='')
