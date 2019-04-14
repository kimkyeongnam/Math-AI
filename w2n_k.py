korean_rule = {
    '영': [],
    '일': ['일', '한'],
    '이': ['이', '두'],
    '삼': ['삼', '상', '탐', '샴', '참', '담', '밤', '세', '쎄', '쌔', '새', '쉐', '쇠'],
    '사': ['사', '샤', '자', '타', '차', '하', '네', '내'],
    '오': ['오', '다섯'],
    '육': ['육', '륙', '뉵', '여섯'],
    '칠': ['칠', '질', '진', '일곱'],
    '팔': ['팔', '발', '빨', '여덟'],
    '구': ['구', '꾸', '쿠', '궁', '국', '북', '아홉'],
    '십': ['십', '입', '열']
}

korean_number_system = {
    '영': 0,
    '일': 1,
    '이': 2,
    '삼': 3,
    '사': 4,
    '오': 5,
    '육': 6,
    '칠': 7,
    '팔': 8,
    '구': 9
}


def korean_pron(text):
    # print("바꾸기전:" + text)

    for i, j in korean_rule.items():
        for k in j:
            if (text == k):
                text = i
    # print("바뀐후(문자):" + text)

    for i, j in korean_number_system.items():
        for k in i:
            if (text == k):
                text = str(j)
    # print("바뀐후(숫자):" + text)

    text = text.replace(" ", "")
    # print("바뀐후(공백제거):" + text)

    text = text.replace("마이너스", "-")
    text = text.replace("빼기", "-")
    # print("바뀐후(음수):" + text)

    text = text.replace("번", "")
    return text
