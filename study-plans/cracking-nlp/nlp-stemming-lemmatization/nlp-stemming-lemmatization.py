def stem_and_lemmatize(word: str, lemma_dict: dict) -> dict:
    """
    Returns a dictionary with string values stem and lemma.
    """
    stem = word 
    lemma = lemma_dict.get(word, word)

    if word.endswith("ing") and len(word[:-3]) >= 3:
      stem = word[:-3]
    elif word.endswith("ly") and len(word[:-2]) >= 3:
      stem = word[:-2]
    elif word.endswith("ed") and len(word[:-2]) >= 3:
      stem = word[:-2]
    elif word.endswith("s") and not word.endswith("ss") and len(word[:-1]) >= 2:
      stem = word[:-1]
    elif word.endswith("er") and len(word[:-2]) >= 3:
      stem = word[:-2]
    elif word.endswith("tion") and len(word[:-4] + "te") >= 3:
      stem = word[:-4] + "te"
    else:
      stem = word

    return {
      "stem": stem,
      "lemma": lemma
    }