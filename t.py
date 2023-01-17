# coding: utf-8
from web.utils.serializer import jwt_encode, jwt_decode, JWTData


if __name__ == '__main__':
    k = 'good-idea'
    p = {'a': 'b', 'c': 'd'}
    r = jwt_encode(JWTData.build(data=p), k)
    print(r)
    print(jwt_decode(r, k))
    print(jwt_decode(r+'aaa', k) is None)
