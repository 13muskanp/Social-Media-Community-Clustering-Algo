import re
from loco_nlp.preprocessing.space_cleaner import clean_spaces

all_punct = "/-'#$%\'()*+-/:/.!?,;<=>@[\\]^_`{|}~`" + '""“”’' + '∞θ÷α•−β∅³π‘₹´°£€\×™√²—–&।'


def all_punct_cleaning(text, punct=None, replacement=' '):
    if not punct:
        punct = all_punct
    else:
        sub_punct = set(all_punct) - set(punct)
        punct = ''.join(sub_punct)

    def remove_punct(sentence):
        sentence = sentence.translate(str.maketrans(punct, replacement * len(punct))).strip()
        sentence = clean_spaces(sentence)
        return sentence

    return list(map(remove_punct, text)) if type(text) is list else remove_punct(text)


def primary_punct_cleaning(text):
    punct = "/-'#$%\'()*+-/:;<=>@[\\]^_`{|}~`" + '""“”’' + '∞θ÷α•−β∅³π‘₹´°£€\×™√²—–&'

    def remove_punct(sentence):
        sentence = sentence.translate(str.maketrans('', '', punct)).strip()
        sentence = re.sub(r'[\?\.\!\,]+(?=[\?\.\!\,])', '', sentence).strip()
        return sentence

    return list(map(remove_punct, text)) if type(text) is list else remove_punct(text)


if __name__ == "__main__":
    print('ok')
    print(primary_punct_cleaning("test #$^ . 1dnf ! dsjngaj > ?"))
    print(primary_punct_cleaning(["test #$^ . 1dnf !!! dsjngaj > ?", "test 2 !@#%&** ."]))
    print(primary_punct_cleaning(["RT @MahindraAutoNA: !!!!!! Engineered in Michigan. Built in Michigan. Creating Jobs in Michigan. Come visit the Mahindra Automotive North America booth at the North American International Auto Show !… https://t.co/HPrVCYLa3O"]))
    print(all_punct_cleaning(["test #$^ . ? ? 1dnf !!! dsjngaj > ?", "test ,.!?2 !@#%&** ."], punct=['!','?']))