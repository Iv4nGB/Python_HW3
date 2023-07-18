# В большой текстовой строке подсчитать количество встречаемых слов и вернуть 10 самых частых.
# Не учитывать знаки препинания и регистр символов.
# За основу возьмите любую статью из википедии или из документации к языку.
from typing import Dict, Any

# Текст для обработки ресурс http://people.maths.ox.ac.uk/moulton/The_Adventures_of_Sherlock_Holmes.pdf
WORK_TEXT = "To Sherlock Holmes she is always THE woman. I have seldom heard him mention her under any other name. " \
            "In his eyes she eclipses and predominates the whole of her sex. It was not that he felt any emotion akin to love " \
            "for Irene Adler. All emotions, and that one particularly, were abhorrent to his cold, precise but admirably " \
            "balanced mind. He was, I take it, the most perfect reasoning and observing machine that the world has seen " \
            "but as a lover he would have placed himself in a false position. He never spoke of the softer passions, save " \
            "with a gibe and a sneer. They were admirable things for the observer--excellent for drawing the veil from " \
            "men's motives and actions. But for the trained reasoner to admit such intrusions into his own delicate and " \
            "finely adjusted temperament was to introduce a distracting factor which might throw a doubt upon all his " \
            "mental results. Grit in a sensitive instrument, or a crack in one of his own high-power lenses, would not be " \
            "more disturbing than a strong emotion in a nature such as his. And yet there was but one woman to him, and " \
            "that woman was the late Irene Adler, of dubious and questionable memory. " 

           

# кол-во требуемых слов
FREQUENT_COUNT = 10


# Возврат count_words самых часто используемых слов из текста в виде строки, разделенных пробелами
def most_frequent_words(text: str, count_words: int) -> dict:
    # удалить знаки препинания, привести к единому регистру, тире ищем только как знак препинания,
    # дефис разделяющий части слова - является его частью
    words_list = text.upper() \
        .replace(".", " ") \
        .replace(",", " ") \
        .replace(";", " ") \
        .replace(":", " ") \
        .replace("!", " ") \
        .replace("?", " ") \
        .replace(" - ", " ") \
        .split()
    # подсчитываем кол-во слов, используем словарь для этого
    words_count = {}
    for w in words_list:
        words_count[w] = words_list.count(w)
    # сортируем словарь по значениям, отбираем только нужное количество
    return dict(sorted(words_count.items(), key=lambda item: item[1], reverse=True)[:count_words])


def main():
    for i, w in enumerate(most_frequent_words(WORK_TEXT, FREQUENT_COUNT).items(), 1):
        print(f"{i:2}. {w[0]:<10} - {w[1]}")


if __name__ == "__main__":
    main()
