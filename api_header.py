import time
import hashlib
import base64

class DigitalRepositoryApiHeader:
    def get_digital_repository_api_header(self):
        appid = 'dispstorestats'
        timestamp = int(time.time()*1000)
        nonce = '9519'
        flag = '1'
        encodingAesKey = 'PAGODADISP'
        md5_message = 'appid={appid}&nonce={nonce}&timestamp={timestamp}&flag={flag}{encodingAesKey}'.format(appid=appid, nonce=nonce, timestamp=timestamp, flag=flag, encodingAesKey=encodingAesKey)

        md5_message_1 = 'appid=dispstorestats&nonce=9519&timestamp=1628594875639&flag=1PAGODADISP'
        hl_1 = hashlib.md5(md5_message_1.encode(encoding='utf-8'))

        hl = hashlib.md5(md5_message.encode(encoding='utf-8'))
        sign = hl.hexdigest()



        sign_2 = base64.b64encode(hl.digest()).decode('utf-8')
        sign_3 = base64.b64encode(hashlib.md5(md5_message.encode(encoding='utf-8')).digest())
        sign_4 = base64.b16encode(sign_3)

        print(sign)
        print(sign_2)
        print(sign_3)
        print(sign_4)

        print(bytearray(b'[B@6d06d69c'))

if __name__ == '__main__':
    DigitalRepositoryApiHeader().get_digital_repository_api_header()