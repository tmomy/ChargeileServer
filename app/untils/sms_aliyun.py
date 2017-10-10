#!/usr/bin/env python
# encoding: utf-8
"""
@author: WL
@time: 2017/9/26 18:07
"""
import sys
from datetime import datetime
import uuid
import requests
import json
from lib.utils import logging
reload(sys)
sys.setdefaultencoding('utf8')
from app.conf import config
R_SMS = config.R_SMS

access_key_id = R_SMS['ACCESS_KEY_ID']
access_key_secret = R_SMS['ACCESS_KEY_SECRET']
template_code = R_SMS['template_code']
sign_name = R_SMS['sign_name']
server_address = 'dysmsapi.aliyuncs.com'


def send_sms_al(phone, param_string):

    url = 'https://sms.aliyuncs.com/'
    ts = datetime.utcnow().strftime('%Y-%m-%dT%H:%M:%SZ')
    once = str(uuid.uuid4())
    data = {
        'Action': 'SingleSendSms',
        'SignName': sign_name,
        'TemplateCode': template_code,
        'RecNum': phone,
        'ParamString': param_string,
        'Format': 'JSON',
        'Version': '2016-09-27',
        'AccessKeyId': access_key_id,
        'SignatureMethod': 'HMAC-SHA1',
        'Timestamp': ts,
        'SignatureVersion': '1.0',
        'SignatureNonce': once,
    }

    def __percent_encode(s):
        import urllib
        s = str(s)
        s = urllib.quote(s.decode('utf8').encode('utf8'), '')
        s = s.replace('+', '%20')
        s = s.replace('*', '%2A')
        s = s.replace('%7E', '~')
        return s

    def __gen_signature(data, req_method, secret):
        import hashlib
        import hmac
        import base64

        sorted_data = sorted(data, key=lambda v: v[0])
        vals = []
        for k, v in sorted_data:
            vals.append(__percent_encode(k) + '=' + __percent_encode(v))

        params = '&'.join(vals)
        string_to_sign = req_method + '&%2F&' + __percent_encode(params)
        key = secret + '&'
        signature = base64.encodestring(hmac.new(key, string_to_sign, hashlib.sha1).digest()).strip()
        return signature

    try:
        headers = {
            'Content-Type': 'application/x-www-form-urlencoded',
        }

        signature = __gen_signature(data.items(), 'POST', access_key_secret)
        data['Signature'] = signature

        r = requests.post(url, data=data, headers=headers)
        resp = r.json()
        logging.info('fun_out: [sms_response: %2s]', json.dumps(resp))
        print resp
        if resp.get('Model'):
            return True
    except Exception, e:
        logging.error('sms_err: [sms_err: %2s]', e)




