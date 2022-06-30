import string                                                       # Нужен для того чтобы достать
                                                                    # все Англ. буквы

class Alphabet:                                                     # Создаём класс родитель

    def __init__(self, lang, letters):                              #  Определяем параметры
        self.lang = lang
        self.letters = letters                                      # Если вдруг закралось что-то
        for i in self.letters:                                      # помимо букв, то удаляем это
            if i.isalpha():
                continue
            else:
                self.letters = self.letters.replace(i, "")
        self.letters = list(self.letters)                           # Создаём список из введённых букв

    def print_let(self):                                            # Метод для вывода алфавита
        print(f"Буквы алфавита - {self.letters}")

    def letters_num(self):                                          # Метод для вывода кол-ва букв
        print(f"Количество букв в алфавите = {len(self.letters)}")  # в алфавите

class EngAlphabet(Alphabet):                                        # Создаём класс потомок

    __letters_num = 26                                              # Гуглим количество букв в английском

    def __init__(self):                                             # Наследуем инит у родителя и задаём
        super().__init__("Eng", string.ascii_lowercase)             # параметры name = ENG и
                                                                    # letters = буквам в англ. алфавите

    def is_en_letter(self, letter):                                 # Проверка на принадлежность буквы к
        if letter.lower() in self.letters:                          # Английскому алфавиту
            print(f"Буква {letter} есть в Английском алфавите")
        else:
            print(f"Буквы {letter} нет в Английском алфавите")

    def letters_num(self):                                          # Вывод кол-ва букв в англ. алфавите
        print(EngAlphabet.__letters_num)

    @staticmethod                                                   # Вывод примера текста на инглише
    def example():
        print("EXAMPLE: Some English text here")
#---------Проверка родителя-----------------------
alpha = Alphabet("RU", "А, Б, В, Г")

alpha.print_let()
alpha.letters_num()
#---------Проверка дитёнка-----------------------
beta = EngAlphabet()

beta.print_let()
beta.letters_num()
beta.is_en_letter("I")
beta.is_en_letter("А")
EngAlphabet.example()
