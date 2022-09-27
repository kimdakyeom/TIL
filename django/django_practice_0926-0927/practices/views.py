from django.shortcuts import render
import random


def index(request):
    return render(request, "practices/index.html")


def ping(request):
    return render(request, "practices/ping.html")


def pong(request):
    return render(request, "practices/pong.html", {"name": request.GET.get("ball")})


def isoddeven(request, number_):
    if int(number_) == 0:
        result = "0"
    elif int(number_) % 2 == 0:
        result = "짝수"
    elif int(number_) % 2 == 1:
        result = "홀수"

    context = {
        "number_": number_,
        "result": result,
    }
    return render(request, "practices/is-odd-even.html", context)


def calculator(request, number1, number2):
    add = int(number1) + int(number2)
    min = int(number1) - int(number2)
    mul = int(number1) * int(number2)
    div = int(number1) // int(number2)

    context = {
        "number1": number1,
        "number2": number2,
        "add": add,
        "min": min,
        "mul": mul,
        "div": div,
    }
    return render(request, "practices/calculator.html", context)


def name(request):
    return render(request, "practices/name.html")


def prev(request):
    animals = [
        {"ani": "쥐", "img": "https://en.pimg.jp/043/712/987/1/43712987.jpg"},
        {"ani": "소", "img": "https://en.pimg.jp/043/712/989/1/43712989.jpg"},
        {"ani": "호랑이", "img": "https://en.pimg.jp/081/090/880/1/81090880.jpg"},
        {"ani": "토끼", "img": "https://en.pimg.jp/001/699/947/1/1699947.jpg"},
        {"ani": "용", "img": "https://en.pimg.jp/003/379/135/1/3379135.jpg"},
        {"ani": "뱀", "img": "https://en.pimg.jp/091/607/650/1/91607650.jpg"},
        {"ani": "말", "img": "https://en.pimg.jp/006/691/487/1/6691487.jpg"},
        {"ani": "양", "img": "https://en.pimg.jp/083/122/923/1/83122923.jpg"},
        {"ani": "원숭이", "img": "https://en.pimg.jp/083/122/921/1/83122921.jpg"},
        {"ani": "닭", "img": "https://en.pimg.jp/020/758/410/1/20758410.jpg"},
        {"ani": "개", "img": "https://en.pimg.jp/050/477/629/1/50477629.jpg"},
        {"ani": "돼지", "img": "https://en.pimg.jp/093/806/307/1/93806307.jpg"},
    ]
    animal = random.choice(animals)
    name = request.GET.get("name")

    context = {
        "name": name,
        "prev": animal,
    }

    return render(request, "practices/prev.html", context)


def sentence(request):
    return render(request, "practices/sentence.html")


def lorem(request):
    words = ["짜장면", "바나나", "사과", "포도", "딸기"]
    sentence = int(request.GET.get("sentence"))
    word = request.GET.get("word")
    words_result_list = []

    for _ in range(sentence):
        words_result_list.append([random.choice(words) for i in range(int(word))])

    context = {
        "sentence": int(sentence),
        "words_result_list": words_result_list,
    }
    return render(request, "practices/lorem.html", context)
