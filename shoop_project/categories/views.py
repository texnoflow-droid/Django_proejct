from django.http import HttpResponse

def category_list(request):
    return HttpResponse("""
        <h1 style='color: #8e44ad; font-family: Arial;'>📂 Mahsulot Kategoriyalari</h1>
        <ul style='font-size: 20px;'>
            <li>📱 Elektronika</li>
            <li>👕 Kiyim-kechak</li>
            <li>🏠 Uy jihozlari</li>
        </ul>
    """)