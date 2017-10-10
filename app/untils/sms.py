#!/usr/bin/env python
# encoding: utf-8
"""
@author: WL
@time: 2017/6/30 17:39
"""

import uuid
from app.conf.config import R_SMS
from lib.utils import logging
import top


def send_sms_dy(phone_number,template_param):
    req = top.api.AlibabaAliqinFcSmsNumSendRequest()
    req.set_app_info(top.appinfo(R_SMS['ACCESS_KEY_ID'], R_SMS['ACCESS_KEY_SECRET']))
    req.extend = uuid.uuid1()
    req.sms_type = "normal"
    req.sms_free_sign_name = R_SMS['sign_name']
    req.sms_param = template_param
    req.rec_num = phone_number
    req.sms_template_code = R_SMS['template_code']
    try:
        resp = req.getResponse()
        print resp
        logging.info('fun_out: [sms_response: %2s]', resp)
        if resp['alibaba_aliqin_fc_sms_num_send_response']['result']['err_code']=="0":
            return True
    except Exception, e:
        logging.info('fun_out: [sms_response: %2s]', e)



