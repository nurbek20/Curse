from django.shortcuts import render, HttpResponse

# Create your views here.
def main(request):
    return HttpResponse("Helle world!")
def test(request):
    return HttpResponse("Test")
def test1(request):
    return HttpResponse("Test1")
def test2(request):
    return HttpResponse("Test2")
def test3(request):
    return HttpResponse("Test3")
def main1(request):
    return HttpResponse("<h1>НУРБЕК</h1>")
def hoby(request):
    return HttpResponse("<h1>Мой хобби, свободные времена ехать на машине далеко и  увидеть новые земли</h1> ")
def skills(request):
    return HttpResponse("<h1>Я учусь в курсе ITCBOOTCAMP и я сейчас знаю язык python, HTML/CSS, Beckend, SQL,....</h1>")
def sport(request):
    return HttpResponse("<h1>Я играю фудбол, шахмать и  теннис</h1>")
def books(request):
    return HttpResponse("<h1>Книга я не читаю я слушаю болше аудиокнига</h1>")
