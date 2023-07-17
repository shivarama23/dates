import re

def check_exp_expiration(input_string):
    input_string = input_string.lower()
    pattern = r"(?<![a-zA-Z0-9_])(exp|expiration)(?![a-zA-Z0-9_])"
    matches = re.findall(pattern, input_string)
    return bool(matches)

def replace_exp_with_space(input_string):
    pattern = r"EXP(?=Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)"
    replaced_string = re.sub(pattern, "EXP ", input_string)
    return replaced_string
