import requests
import random
from io import BytesIO
import deal


def get_code(code_img_url, img_data, img_headers, timeout):
    res = requests.get(url=code_img_url, data=img_data, headers=img_headers, timeout=timeout)

    return deal.OCR_lmj(BytesIO(res.content))


def run():
    vote_url = 'https://v.tiantianvote.com/v.php'
    code_img_url = 'https://v.tiantianvote.com/api/c2/captchas.png.php?rnd=15160133803350260314&type=2&id=3803350'

    headers = {}
    void_headers = {}
    img_headers = {}
    # 构造随机UA
    headers[
        'User-Agent'] = "Mozilla/5.0 (iPhone; CPU iPhone OS 10_1_2 like Mac OS X) AppleWebKit/537.51.2 (KHTML, like Gecko) Mobile/11D257 MicroMessenger/6.5.2.501 NetType/WIFI"

    img_headers[
        'Cookie'] = 'D5O_advice_brandid_0=1516013; D5O_back_sid_0=b9d2b7d7f55d6694; UM_distinctid=172c514e0da9c-0d9ec11c4b870c-143f6257-13c680-172c514e0dbd6a; D5O_advice_brandid_1=1516013; D5O_back_sid_1=b9d2b7d7f55d6694; D5O_enter=1516013; acw_tc=2760820215924485275232006e63b636a607e754676c3e300cfc50f6d63983; D5O_openinfos=%257B%2522uid%2522%253A1%252C%2522token%2522%253A%2522%2522%257D'
    # Referer 地址
    headers['Referer'] = "https://h5.tiantianvote.com/m.php?v=b9d2b7d7f55d6694"
    void_headers['Content-Type'] = 'application/x-www-form-urlencoded; charset=UTF-8'

    void_headers = dict(headers, **void_headers)
    img_headers = dict(headers, **img_headers)

    def send_num(n):
        str = ""
        for i in range(n):
            ch = chr(random.randrange(ord('0'), ord('9') + 1))
            str += ch
        return str

    img_data = {
        'rnd': '15160133803350' + send_num(6),
        'type': 2,
        'id': 3803350
    }

    try:
        code = get_code(code_img_url, img_data, img_headers, 3000)

        print('code是')
        data = {
            'brandid': 1516013,
            'itemid': 3803350,
            'yqm': input(),
            'rnd': img_data['rnd'],
            'ouid': 1,
            'sid': 'b9d2b7d7f55d6694',
            'token': ''
        }
        res = requests.post(url=vote_url, data=data, headers=void_headers, timeout=3000)
        print(res.content)
    except:
        run()


if __name__ == '__main__':
    run()
