from django.core.exceptions import ValidationError
from datetime import date, datetime


def clean_price(value):
    if value < 0:
        raise ValidationError("Неверная цена")
    return value

def clean_settle_date(value):
    today       = date.today()
    if datetime.date(value) < today:
        raise ValidationError("Неверная дата")
    return value 

def clean_comment_text(value):
    if value == NULL:
        raise ValidationError("Поле пусто")
    return value 