import re


def validate_cpf(cpf: str) -> bool:
    cpf = re.sub(r'[^0-9]', '', cpf)
    if len(cpf) != 11 or cpf == cpf[0] * 11:
        return False

    def calculate_digit(digits):
        total = sum(
            (len(digits) + 1 - i) * int(n) for i, n in enumerate(digits)
        )
        remainder = 11 - (total % 11)
        return '0' if remainder > 9 else str(remainder)

    d1 = calculate_digit(cpf[:9])
    d2 = calculate_digit(cpf[:9] + d1)
    return cpf.endswith(d1 + d2)
