import contractions

#Todo add contraction extractor

def contraction_handler(text, replacement=None):
    def cleaner(input_text):
        result = contractions.fix(input_text)
        result = result.replace("'s", '')
        return result
    return list(map(cleaner, text)) if type(text) is list else cleaner(text)



if __name__ == "__main__":
    print("ok")
    print(contraction_handler(" John's sister couldn't attend Jeff's party because she didn't study."))