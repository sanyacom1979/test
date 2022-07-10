# использую пакет TextBlob для перевода (функция определения языка в пакете не работает)
from textblob import TextBlob
# использую пакет py3langid для определения языка
from py3langid.langid import classify

def tr_string(t):
    try:
        text = TextBlob(t)
        l = classify(t)
        # в l содежится информация типа ('en', -51.70071)
        # язык вытаскиваем l[0]
        # далее возвращаем перевод
        return text.translate(from_lang=l[0], to="ru")
    except:
        # уход по ошибке
        return "Не могу перевести"
