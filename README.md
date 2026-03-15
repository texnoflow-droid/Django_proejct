{ "schemaVersion": 1, "label": "Dj", "message": "project", "color": "orange" }
# 🎸 Django Professional Project Structure

![Django](https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=django&logoColor=white)
![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=for-the-badge&logo=python&logoColor=white)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-336791?style=for-the-badge&logo=postgresql&logoColor=white)
![Status](https://img.shields.io/badge/Status-In_Development-yellow?style=for-the-badge)

Ushbu loyiha Django frameworkida backend tizimlarini qurish uchun mustahkam poydevor (boilerplate) hisoblanadi. Loyiha zamonaviy backend talablariga mos ravishda, xavfsizlik va kengayuvchanlik prinsiplari asosida tuzilgan.

---

## 🛠 Texnologiyalar Steki

* **Framework:** Django 4.x / 5.x
* **Ma'lumotlar bazasi:** PostgreSQL (yoki SQLite konfiguratsiyasi bilan)
* **Muhit boshqaruvi:** `python-dotenv` (maxfiy ma'lumotlar uchun)
* **Backend tili:** Python 3.10+

---

## 🚀 Loyihaning o'ziga xosliklari

- [x] **Modular Architecture:** Har bir funksiya alohida `apps` ko'rinishida ajratilgan.
- [x] **Secure Config:** API kalitlari va Database parollari `.env` faylida xavfsiz saqlanadi.
- [x] **DRF Ready:** REST API yaratish uchun asosiy sozlamalar mavjud.
- [x] **Custom User Model:** Foydalanuvchilar tizimini moslashtirish uchun tayyor struktura.

---

## 📂 Loyiha tuzilmasi (Project Tree)

```text
├── core/                # Loyihaning asosiy sozlamalari (settings, urls, wsgi)
├── apps/                # Barcha yaratilgan ilovalar (models, views, serializers)
├── static/              # CSS, JS va rasmlar to'plami
├── templates/           # HTML fayllari
├── .env.example         # Muhit o'zgaruvchilari namunasi
├── manage.py            # Django boshqaruv skripti
└── requirements.txt     # Kerakli kutubxonalar ro'yxati
