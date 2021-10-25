from unidecode import unidecode


def lower_dict_keys(dic: dict):
    return {key.lower(): value for key, value in dic.items()}


def normalize_string(string: str):
    white = string.strip()
    accents = unidecode(str(white).lower())
    return accents
