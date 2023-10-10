from django.urls import path, re_path
import example.views as v

urlpatterns2 = [
    path('', v.check, name="cheked"),
    path('edit/', v.edit, name="edited")
]

urlpatterns = [
    path('', v.starts, name="shoped"),
    path('catalog2/', v.shop2, name="shoped2"),
    path('catalog2/add', v.add, name="added"),
    path('check/<int:a>/'),
    path('feedback/', v.feedback, name="fb")

    # ^ начало адреса
    # $ конец адреса
    # t символ встречается 1 или более раз
    # t{n} символ встречается n раз
    # t{n, m} символ встречается n раз до m раз
    # \d обозначение цифры
    # \D обозначение символов (не цифр)
    # \w обозначение буквенных символов (не спец символов)
]