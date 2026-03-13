from django.http import HttpResponse
def product_list(request):
    return HttpResponse("<h1 style='color: #2c3e50; font-family: sans-serif;'>🛍️ Bizning mahsulotlar</h1><p>iPhone 15, MacBook Pro, Airpods</p>")
def product_detail(request):
    return HttpResponse("<div style='background-color: #f1c40f; padding: 20px; border-radius: 15px;'><h2>Mahsulot narxi: $1200</h2></div>")