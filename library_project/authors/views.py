from django.http import HttpResponse

def author_list(request):
    return HttpResponse("<h1 style='color: #2980b9;'>✍️ Mashhur mualliflar</h1><p>Abdulla Qodiriy, Xudoyberdi To'xtaboyev</p>")