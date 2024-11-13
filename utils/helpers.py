import re

def extract_numbers(text):
    # Extrai apenas números usando regex
    numbers = re.findall(r'\d+', text)
    return [int(num) for num in numbers]
