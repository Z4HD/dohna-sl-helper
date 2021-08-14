from dohna_sl_helper.ui import intValidation

def test_int_validation():
    assert not intValidation('adsfasf')
    assert intValidation('250')
    assert not intValidation("00aadas")
    assert not intValidation("aadas1120")