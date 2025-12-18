import string

class Alphabet:
    default_lang = "UA"
    default_letters = list("абвгґдеєжзиіїйклмнопрстуфхцчшщьюя")

    def __init__(self, lang=None, letters=None):
        self.lang = lang if lang else Alphabet.default_lang
        self.letters = letters if letters else Alphabet.default_letters

    def print_alphabet(self):
        print(f"Алфавіт мови {self.lang}: {self.letters}")

    def letters_num(self):
        return len(self.letters)

    def is_ua_lang(self, text):
        text = text.lower()

        for char in text:
            if char.isalpha():
                if char not in Alphabet.default_letters:
                    return False
        return True


class EngAlphabet(Alphabet):
    __en_letters_num = 26

    def __init__(self):
        super().__init__('En', list(string.ascii_lowercase))

    def is_en_letter(self, letter):
        return letter.lower() in self.letters

    def letters_num(self):
        return EngAlphabet.__en_letters_num

    @staticmethod
    def example():
        return "The quick brown fox jumps over the lazy dog."


eng_alphabet = EngAlphabet()
eng_alphabet.print_alphabet()

print(f"Кількість букв в алфавіті: {eng_alphabet.letters_num()}")

check_j = eng_alphabet.is_en_letter('J')
print(f"Чи належить 'J' до англійського алфавіту: {check_j}")

check_shch = eng_alphabet.is_ua_lang('Щ')
print(f"Чи належить 'Щ' до української мови: {check_shch}")

print(f"Чи є слово 'Hello' українським: {eng_alphabet.is_ua_lang('Hello')}")

print(f"Приклад тексту англійською: {EngAlphabet.example()}")