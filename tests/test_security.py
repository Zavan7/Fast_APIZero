from jwt import decode

from fastapi_zero.security import ALGORITHM, SECRET_KEY, creat_access_token


def test_jwt():
    data = {'test': 'test'}
    token = creat_access_token(data)

    decoded = decode(token, SECRET_KEY, algorithms=ALGORITHM)

    assert decoded['test'] == data['test']
