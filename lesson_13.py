import re


def result_task():
    regexp = RegExp(pattern, list_str, number_task)
    for line in regexp:
        if line:
            print(line)


class RegExp:
    def __init__(self, pattern, list_str, number_task):
        self.pattern = pattern
        self.list_str = list_str
        self.index = 0
        self.number_task = number_task

    def __iter__(self):
        return self

    def __next__(self):
        if self.index < len(self.list_str):
            self.index += 1
            if self.number_task in [1, 2, 3, 4]:
                match = re.search(self.pattern, self.list_str[self.index - 1])
                if match:
                    return self.list_str[self.index - 1]
            elif self.number_task == 6:
                self.list_str[self.index - 1] = re.sub(self.pattern, 'computer', self.list_str[self.index - 1])
                self.list_str[self.index - 1] = self.list_str[self.index - 1].capitalize()
                return self.list_str[self.index - 1]
            elif self.number_task == 9:
                self.list_str[self.index - 1] = re.sub(self.pattern, r'\1', self.list_str[self.index - 1])
                return self.list_str[self.index - 1]
        else:
            raise StopIteration


"""1)	Вам дана последовательность строк.
Выведите строки, содержащие "cat"."""

print("Start Task #1")

list_str = ["Roses are red, violets are blue",
            "The cat sat on the mat, that's true",
            "In a world of chaos and strife",
            "A cute little cat can brighten your life",
            "As the sun sets in the western sky",
            "The cat purrs softly, a lullaby",
            "Dreams of adventures, both near and far",
            "Follow the cat, like a guiding star",
            "Through forests and meadows, it boldly roams",
            "With a curious spirit, it explores new homes",
            ]

pattern = r'cat'
number_task = 1

result_task()

print("End Task #1\n")

"""
2)	Выведите строки, содержащие две буквы "z", между которыми ровно три символа.
"""

print("Start Task #2")

list_str = ["The quick brown zasdz fox jumps over the lazy dog",
            "A zasz bird in the hand is worth two in the bush",
            "All's fair in love and zaz war",
            "You can't judge a book by its zaaazaaaz cover",
            "Actions speak louder than z   z words"
            ]

pattern = r'z...z'
number_task = 2

result_task()

print("End Task #2\n")

"""3)	
Номер должен быть длиной 10 знаков и начинаться с 8 или 9. Есть список телефонных номеров, и нужно проверить их, используя регулярные выражения в Python
"""

print("Start Task #3")

list_str = ["1234567",
            "9876543",
            "5555555",
            "123456789",
            "77777777",
            "888888888a",
            "5555555555",
            "9999а99999",
            "9999999999",
            "8888888888",
            "1234567890",
            "4444444444"
            ]

pattern = r'^[89]\d{9}$'
number_task = 3

result_task()

print("End Task #3\n")

"""4)	Дана строка, выведите все вхождения слов, начинающиеся на гласную букву."""

print("Start Task #4")

some_str = "a apple banana cat dog elephant fish grape hat igloo jelly kite lemon monkey narwhal octopus penguin quokka raccoon squirrel tiger unicorn vulture walrus x-ray yak zebra"

#по строке
# pattern = r'\b[aeiouAEIOU][a-zA-Z]*\b'
# matches = re.findall(pattern, some_str)
# for word in matches:
#     print(word)

#по строке, но через лист
list_str = some_str.split()
pattern = r'^[aeiouAEIOU]'
number_task = 4
result_task()

print("End Task #4\n")

"""5)	Дана строка. Вывести все числа этой строки, как отрицательные так и положительные. """

print("Start Task #5")

some_str = "Apple 01..23 Sky -45 Table 6789 Dog -3.14 Moon 87 Laptop -42 Rain 5678 Chair 9.8 Sun 1234 Cat 56 Tree 7890 Book 2.71 Car 12345 Ocean 6.626 Hat 54321 House 3.0 Phone 98765 Star 1.618 Desk -101010 Pen 1234567 Mountain 314159 Cookie -271828 Snow 7777.7"

# по строке
pattern = r'[-+]?(?:\d+(?:\.\d+)?)'
matches = re.findall(pattern, some_str)
number_task = 5
for word in matches:
    print(word)

print("End Task #5\n")

"""6)	В каждой строке замените все вхождения подстроки "human" на подстроку "computer" и выведите полученные строки."""

print("Start Task #6")

list_str = [
    "Humans are the only species capable of advanced language.",
    "Primates, including chimpanzees and gorillas, share a common ancestor with humans.",
    "The study of primate behavior provides valuable insights into human evolution.",
    "Human intelligence sets us apart from other primates.",
    "In some cultures, humans have a tradition of using masks in ceremonies.",
    "Primates exhibit a wide range of social behaviors.",
    "Human beings have a remarkable ability to adapt to different environments.",
    "The human brain is the most complex organ in the primate kingdom.",
    "Researchers study primates to better understand the origins of human behavior.",
    "Human rights are fundamental to a just and equitable society."
]
number_task = 6

pattern = re.compile(r'\bhuman', re.IGNORECASE)
result_task()

print("End Task #6\n")

"""7)	
Извлечь дату из строки. Формат даты dd–mm-yyyy.
"""

print("Start Task #7")

some_str = "The conference is scheduled for October 07-09-2023 08-09-2023"

pattern = r'\d{2}\-\d{2}\-\d{4}'
number_task = 7

matches = re.findall(pattern,some_str)

for date in matches:
    print(date)

print("End Task #7\n")

"""8)	Найти все слова, в которых есть хотя бы одна буква ‘b’"""

print("Start Task #8")

some_str = "I see a red door and I want it painted black No colors anymore I want them to turn black I see the girls walk by dressed in their summer clothes I have to turn my head until my darkness goes"

pattern = r'\b\w*b\w*\b'
number_task = 8

matches = re.findall(pattern,some_str)

for word in matches:
    print(word)

print("End Task #8\n")

"""9)	В каждой строке замените все вхождения нескольких одинаковых букв на одну букву. Буквой считается символ из группы \w."""

print("Start Task #9")

list_str = ["Rosesss are red, violets are blue",
            "The cat sat on the mat, that's true",
            "In a world of chaos and strife",
            "A cute little cat can brighten your life",
            "As the sun sets in the western sky",
            "The cat purrs softly, a lullaby",
            "Dreams of adventures, both near and far",
            "Follow the cat, like a guiding star",
            "Through forests and meadows, it boldly roams",
            "With a curious spirit, it explores new homes",
            ]

pattern = r'(\w)\1+'
number_task = 9

result_task()

print("End Task #9\n")
