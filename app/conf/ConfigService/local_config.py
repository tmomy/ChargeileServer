# !/usr/bin/env python
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
    "port": 8080,
    "debug": True
}

mysql_pool_configs = {
    "url": "mysql+pymysql://root:qwe1234567@10.10.51.30:3306/ChargePile?charset=utf8mb4",
    "pool_size": 1,
    "max_overflow": 10,
    "pool_recycle": 2*60*60

}

redis_pool_configs = {
        "type": db_type["redis"],
        "host": "10.10.51.30",
        "port": 6379,
        "pool_size": 5, # 0表示不使用连接池 最大连接数
        "user_name": "",
        "password": "",
        "db_name": "ChargePile"
}


# 日志配置
log = {
    "name": "myapp",
    "level": "debug",
    "console": True,
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
}