#!/usr/bin/env python
# encoding: utf-8
"""
@author: WL
@time: 2017/10/10 15:56
"""
"""
系统全局配置文件
"""
db_type = {
    "mongodb": "mongodb",
    "mysql": "mysql",
    "redis": "redis"
}

# web
web = {
    "url_pre": "/api/tiptop",
    "api_version": ["v1"],
    "ip": "0.0.0.0",
    "enable_rule": False,
    "enable_admin": False,
    "role": "admin",
    "opr": ["add", "modify", "delete", "search"],
    "rule_redis_pix": "sys_rule_id_",
    "switch_redis_pix": "sys_switch_",
    "switch_opr_timeout": 60,
    "port": 1111,
    "session_timeout": 60 * 60 * 24 * 30,
    "push_time":60 * 30,
    "token_key": "zhong_lv_YLKJ",
    "default_avatar": "/static_file/public/@3px.png",
    # "log_pix": "F:\\dgg\\src\\branches\\1.0\\src\\backend\\",
    "key_len": 20,
    "pwd_err_code": 3,
    "pwd_err_freeze": 8,
    "account_freeze_time": 60*10,
    "debug": True,
    "frontend_port": 8899,
    # 图片上传路径
    "upload_path": "/static_file/uploads/",
    "pic_pix": "/static_file/",
    # 开关延期时间
    "switch_delay_time": 2,
    # 极光推送生产开关
    "apns_production": False
}



mysql_pool_configs = {
    "url": "mysql+pymysql://dgg:youlu_dc_666666@127.0.0.1:10003/dgg?charset=utf8mb4",
    "pool_size": 100,
    "max_overflow": 10,
    "pool_recycle": 2*60*60

}


# 日志配置
log = {
    "name": "myapp",
    "level": "debug",
    "console": False,
    "format": "%(thread)d:%(asctime)s %(funcName)s:%(lineno)d %(filename)s - %(name)s %(levelname)s - %(message)s",
    "file": {
        "enable": False,
        "path": ""
    },
    "syslog": {
        "enable": True,
        "ip": "127.0.0.1",
        "port": 10514,
        "facility": "local5"
    }
}

sqltime_log_config = {
    "name": "sqltime",
    "level": "debug",
    "console": False,
    "format": "%(asctime)s %(funcName)s:%(lineno)d %(filename)s - %(name)s %(levelname)s - %(message)s",
    "file": {
        "enable": False,
        "path": ""
    },
    "syslog": {
        "enable": True,
        "ip": "127.0.0.1",
        "port": 10514,
        "facility": "local5"
    }
}

pool_log_config = {
    "name": "sqlalchemy.pool",
    "level": "debug",
    "console": False,
    "format": "%(asctime)s %(funcName)s:%(lineno)d %(filename)s - %(name)s %(levelname)s - %(message)s",
    "file": {
        "enable": False,
        "path": ""
    },
    "syslog": {
        "enable": True,
        "ip": "127.0.0.1",
        "port": 10514,
        "facility": "local5"
    }
}
# 邮件
email = {
    "smtp_addr": "smtp.qq.com",
    "from_email": "446330342@qq.com",
    "from_email_pwd": "vibwzctxgecpbhba",
    "subject": "邮箱验证"
}


# 注册短信验证码配置参数
R_SMS = {
    # 秘钥ID
    "ACCESS_KEY_ID": "LTAICHTV2KkBTnT3",
    "ACCESS_KEY_SECRET": "fvrR7gcA4Nos7BQbx7rlXJeZt6p4E0",
    "template_code": "SMS_99935005",
    "sign_name": "中农润民",
    "template_string": "num",
    "redis_timeout": 15*60
}

# redis 各模块存储前缀
red_pre = {
    # 修改绑定手机号验证码
    "sms_lock_pix": "tel_pix_",
    # 修改密码验证码
    "pwd_lock_pix": "password_pix_",
    # 用户激活码(code -> email)
    "code": "c_a_",
    # 用户对应的平台的ssid(email + platform + placeholder -> ssid )
    "acc_plat_ssid": "a_pp_s_",
    # 账户详细信息(ssid -> account)
    "ssid_acc": "s_a_",
    # 验证码（uuid -> captcha）
    "captcha": "u_cp_",
    # 用户密码输入错误次数统计（email -> counts）
    "acc_login_err": "e_c_"
}