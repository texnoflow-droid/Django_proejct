from django.http import HttpResponse

def book_list(request):
    return HttpResponse("<h1 style='color: #d35400; border-bottom: 2px solid #d35400;'>📚 Kutubxonadagi kitoblar</h1><ul><li>O'tkan kunlar</li><li>Sariq devni minib</li></ul>")