import re

def get_link(str):

    match = re.search('\w{5}\W{3}\w{6}\W\w{3}\W\w*\W\w*', str)
    # регулярное выражение по поиску ссылки на гит
    msg = match[0]

    return msg

def get_variant(str):

    match = re.search('\w{7}\s\d{1,}', str)  # регулярное выражение для поиска нмоера варианта
    variant = match[0]

    return variant
