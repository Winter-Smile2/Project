import base64
import copy
import hmac
import json
import time


class Jwt:
    def __init__(self):
        pass

    @staticmethod
    def b64encode(j_s):
        return base64.urlsafe_b64encode(j_s).replace(b'=', b'')

    @staticmethod
    def b64decode(b_s):
        rem = len(b_s)%4
        if rem > 0:
            b_s += b'=' * (4-rem)
        return base64.urlsafe_b64decode(b_s)
    @staticmethod
    def encode(payload,key,exp=300):
        # init header
        header = {'alg':'HS256','typ':'JWT'}
        my_payload = copy.deepcopy(payload)
        my_payload['exp'] = time.time()+int(exp)
        header = json.dumps(header, sort_keys=True,separators=(',',':'))
        payload = json.dumps(my_payload, sort_keys=True,separators=(',',':'))
        str_ = Jwt.b64encode(header.encode())+b'.'+Jwt.b64encode(payload.encode())
        if isinstance(key, str):
            key = key.encode()
        h = hmac.new(key, str_, digestmod='SHA256')
        h_bs = Jwt.b64encode(h.digest())
        return str_ + b'.' + h_bs
    @staticmethod
    def decode(jwt_s, key):
        msg = jwt_s.split(b'.')
        header_bs = msg[0]
        payload_bs = msg[1]
        if isinstance(key,str):
            key = key.encode()
        hm = hmac.new(key, header_bs+b"."+payload_bs,digestmod='SHA256')
        new_sign_bs = Jwt.b64encode(hm.digest())
        if new_sign_bs != msg[2]:
            raise
        # 检查payload中的时间
        payload = json.loads(Jwt.b64decode(payload_bs))
        exp = payload['exp']
        now_t = time.time()
        if now_t>exp:
            raise
        return payload

if __name__ == '__main__':
    s = Jwt.encode({'username':'winter'}, 'summer', 100)
    print(s)
    d = Jwt.decode(s,'summer')
    print(d)
    n = int(input())