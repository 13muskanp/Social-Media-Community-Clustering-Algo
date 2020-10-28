import re
from loco_nlp.config import REPLACEMENTS
from loco_nlp.preprocessing.word_segment import segment_words


def extract_hashtags(text):
    replacer = segment_words(text)
    return replacer


def clean_hashtags(text, replacement=REPLACEMENTS['hashtag']):
    replacer = lambda sentence: re.sub(r'#[\w]+', replacement, sentence).strip()
    return list(map(replacer, text)) if type(text) is list else replacer(text)


def get_hashtags(text):
    detector = lambda sentence: re.findall(r'#[\w]+', sentence)
    return list(map(detector, text)) if type(text) is list else detector(text)


if __name__ == "__main__":
    print("ok")
    # print(clean_hashtags('test #thisistest'))
    print(extract_hashtags(['test #thisistest', 'test 2 #thisis test']))
    # print(get_hashtags('test #thisistest #goodboy'))
    # print(get_hashtags(['test #thisistest', 'test 2 #thisis test']))
