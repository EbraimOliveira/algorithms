from challenges.challenge_encrypt_message import encrypt_message
import pytest


def test_encrypt_message():
    with pytest.raises(TypeError, match='tipo inválido para key'):
        encrypt_message('string', 'string')
    with pytest.raises(TypeError, match='tipo inválido para message'):
        encrypt_message(666, 666)
    assert encrypt_message('arara', 2) == 'ara_ra'
    assert encrypt_message('arara', 3) == 'ara_ar'
    assert encrypt_message('string', 999) == 'gnirts'
