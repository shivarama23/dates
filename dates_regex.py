import re

def check_exp_expiration(input_string):
    input_string = input_string.lower()
    pattern = r"(?<![a-zA-Z0-9_])(exp|expiration)(?![a-zA-Z0-9_])"
    matches = re.findall(pattern, input_string)
    return bool(matches)
