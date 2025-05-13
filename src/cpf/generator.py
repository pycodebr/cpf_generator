import random


def generate_cpf(formatted: bool = True) -> str:
    def calculate_digit(digits):
        total = sum(
            (len(digits) + 1 - i) * int(n) for i, n in enumerate(digits)
        )
        remainder = 11 - (total % 11)
        return '0' if remainder > 9 else str(remainder)

    base = ''.join(str(random.randint(0, 9)) for _ in range(9))
    d1 = calculate_digit(base)
    d2 = calculate_digit(base + d1)
    cpf = base + d1 + d2
    if formatted:
        return f'{cpf[:3]}.{cpf[3:6]}.{cpf[6:9]}-{cpf[9:]}'
    return cpf
