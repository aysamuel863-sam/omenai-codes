# Matchstick solver
# Step 1: Seven-segment digit representation
DIGITS = {
    "0": set("abcdef"),
    "1": set("bc"),
    "2": set("abdeg"),
    "3": set("abcdg"),
    "4": set("bcfg"),
    "5": set("acdfg"),
    "6": set("acdefg"),
    "7": set("abc"),
    "8": set("abcdefg"),
    "9": set("abcdfg"),
}

SYMBOLS = {
   "+": set("gh"),
   "-": set("g"),
   "=": set("gd"),
}

def get_segments(character):
    if character in DIGITS:
        return DIGITS[character]
    elif character in SYMBOLS:
        return SYMBOLS[character] 
    else:
        return None

def count_matchsticks(equation):
    total = 0
    for character in equation:
        segments = get_segments(character)
        if segments is not None:
            total += len(segments)
    return total

def parse_equation(equation):
    if "=" not in equation:
        return None
    left_side, right_side = equation.split("=")

    if "+" in left_side:
        numbers = left_side.split("+")
        operator = "+"
    elif "-" in left_side:
        numbers = left_side.split("-")
        operator = "-"
    else:
        return None

    if len(numbers) != 2:
        return None

    left_number = int(numbers[0])
    right_number = int(numbers[1])
    answer = int(right_side)

    return left_number, operator, right_number, answer

for digit, segments in DIGITS.items():
    print(digit, segments)

print("===== MATCHSTICK SOLVER =====")
equation = input("Enter the equation: ")
print(f"You entered {equation}")
parts = list(equation)
print(f"Parts: {parts}")

total_matches = count_matchsticks(equation)
print(f"Total matchsticks: {total_matches}")

parsed = parse_equation(equation)

if parsed is None:
    print("Invalid equation format.")
else:
    left_number, operator, right_number, answer = parsed

    print(f"Left_number: {left_number}")
    print(f"Operator: {operator}")
    print(f"Right number: {right_number}")
    print(f"Answer: {answer}")

for part in parts:
    segments = get_segments(part)
    if segments is None: 
        print(f"Unknown character: {part}")
        continue
    print(f"{part} uses {len(segments)} matchsticks")