import re

from cpf.generator import generate_cpf
from cpf.validator import validate_cpf


def test_generate_cpf_formatted():
    cpf = generate_cpf(formatted=True)
    assert re.match(r'^\d{3}\.\d{3}\.\d{3}-\d{2}$', cpf)
    assert validate_cpf(cpf)


def test_generate_cpf_unformatted():
    cpf = generate_cpf(formatted=False)
    assert cpf.isdigit()
    assert len(cpf) == 11
    assert validate_cpf(cpf)
