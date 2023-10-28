# Importa a função de cifragem encrypt_message do módulo challenges.
from challenges.challenge_encrypt_message import encrypt_message
# Importa a biblioteca pytest para realizar testes.
import pytest


# Testa a função de cifragem encrypt_message.
def test_encrypt_message():
    # Verifica se um TypeError é levantado ao fornecer uma string como chave.
    with pytest.raises(TypeError):
        encrypt_message('message', 'str')

    # Verifica se a cifragem de 'maior' com chave 10 resulta em 'roiam'.
    assert encrypt_message('maior', 10) == 'roiam'

    # Verifica se a cifragem de 'par' com chave 2 resulta em 'r_ap'.
    assert encrypt_message('par', 2) == 'r_ap'

    # Verifica se a cifragem de 'impar' com chave 3 resulta em 'pmi_ra'.
    assert encrypt_message('impar', 3) == 'pmi_ra'
