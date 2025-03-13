"""
Домашнее задание №2

Работа с файлами


1. Скачайте файл по ссылке https://www.dropbox.com/s/sipsmqpw1gwzd37/referat.txt?dl=0
2. Прочитайте содержимое файла в перменную, подсчитайте длинну получившейся строки
3. Подсчитайте количество слов в тексте
4. Замените точки в тексте на восклицательные знаки
5. Сохраните результат в файл referat2.txt
"""


def Print_text():  # Вывод самого текста в консоли
    with open("referat.txt", "r", encoding="utf8") as file:
        for line in file:
            print(line)


def All_Letters():  # Подсчет символов и вывод
    with open("referat.txt", "r", encoding="utf8") as file:
        text = file.read()
        text_len = len(text)
    print(f"Символов в тексте: {text_len}")


def All_list_items():  # Подсчет слов и вывод
    with open("referat.txt", "r", encoding="utf8") as file:
        text_spis = file.readline()
        text_spis_len = len(text_spis)
    print(f"Слов в тексте: {text_spis_len}")


def Changes():  # Смена знака "." на "!"
    with open("referat.txt", "r", encoding="utf8") as file:
        text = file.read()
        for i in range(len(text)):
            if text[i] == ".":
                text = text[:i] + "!" + text[i + 1 :]
    # print(text) #Вывод Измененного текста в консоли для проверки
    return text


def Save_res(text_len):
    # input = open("Test.txt", "r", encoding="utf8")
    output = open("referat2.txt", "w", encoding="utf8")
    # res=input.read()
    res = text_len
    output.write(res)
    # input.close()
    output.close


def main():
    # Print_text() #Вывод самого текста в консоли
    All_Letters()  # Подсчет символов и вывод
    All_list_items()  # Подсчет слов и вывод
    # Changes() # Если только изменить без сохранения
    Save_res(
        Changes()
    )  # Если сохранить изменения в файл (txt перезаписывается с каждым запуском программы)


if __name__ == "__main__":
    main()  # Можно было бы сразу сюда вставить функции, но оставил main()
