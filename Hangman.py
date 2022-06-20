# =============================================================================
# hangman test
# =============================================================================
import tkinter as tk
from tkinter import filedialog as fd
from random import choice as c
def hangman():
    """
    простецкая виселица со случайным выбором слова, вроде работает
    """
    root = tk.Tk()
    root.withdraw()
    root.wm_attributes('-topmost', 1)
    err = 0  # отслеживаем кол-во неправильно угаданных букв
    err_draw = [r"",
                r"________ ",
                r"|      |",
                r"|    (👀) ",
                r"|     \_/ ",
                r"|     /|\ ",
                r"|     / \ ",
                r"| "
                ]  # рисунок виселицы для построчного вывода
    # пул со словами
    file_path = fd.askopenfilename(parent=root)
    with open(file_path, 'r', encoding='utf-8') as file:
        wordpool = [line.split()[0] for line in file.readlines()]
    # случайное слово из пула
    word = wordpool[c(range(len(wordpool)))]
    letters = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"  # доступные буквы
    chars = list(word)  # список с буквами, которые нужно угадать
    board = ["__"] * len(word)  # строка для вывода на экран
    win = 0  # отслеживаем статус угадывания (1 - угадали)
    while err < len(err_draw)-1:
        print("\n")
        print(" ".join(board))
        char = input("Введите букву:").lower()
        # проверяем на некорректный ввод (символы, цифры, другая раскладка и др.)
        if len(char) == 1 and char in letters:
            if char in chars:
                board[chars.index(char)] = char
                # если в слове повторяются буквы, index будет искать только первую
                # заменяем угаданный символ на "-", чтобы это обойти
                chars[chars.index(char)] = '-'
            else:
                # увеличиваем счетчик ошибок
                err += 1
        else:
            print('Некорректный ввод, попробуй снова')
        if err < len(err_draw)-1:
            # выводим на экран рисунок виселицы в зависимости от текущего кол-ва ошибок
            print("\n".join(err_draw[:err+1]))
        if "__" not in board:
            # поздравляем и выводим загаданное слово
            print("\nПобеда! Угадано слово:", "".join(board))
            win = 1
            break
    if win != 1:
        # сочувствуем и тоже выводим загаданное слово
        print("\n".join(err_draw[:err+1]))
        print('Проиграл! Загаданное слово: ', word)
hangman()
