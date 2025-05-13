from cpf.validator import validate_cpf


def test_validate_formatted_valid_cpf():
    assert validate_cpf('529.982.247-25')


def test_validate_unformatted_valid_cpf():
    assert validate_cpf('52998224725')


def test_validate_formatted_invalid_cpf():
    assert not validate_cpf('123.456.789-00')
    assert not validate_cpf('000.000.000-00')


def test_validate_unformatted_invalid_cpf():
    assert not validate_cpf('12345678900')
    assert not validate_cpf('00000000000')


def test_validate_short_and_empty_input():
    assert not validate_cpf('123')
    assert not validate_cpf('')


def test_repeated_digits_invalid():
    for d in '0123456789':
        assert not validate_cpf(d * 11)
