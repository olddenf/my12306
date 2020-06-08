# -*- coding: utf-8 -*-
# @time:2020/6/8 20:23
# @author: 垃圾小邓
import requests

# 涉及到的登录坐标
# (40,40),(114,35),(192,39),(257,36),(42,115),(119,107),(185,124),(272,117)

code_list = {
    '1': '40,40',
    '2': '114,35',
    '3': '192,39',
    '4': '257,36',
    '5': '42,115',
    '6': '119,107',
    '7': '185,124',
    '8': '272,117'
}
# 创建会话
session = requests.session()
# headers设置
headers = {
    'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) '
                  'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
                  '83.0.4103.97 Mobile Safari/537.36',
    'Referer': 'https://kyfw.12306.cn/otn/login/init',
}
# 验证码的地址
url = 'https://kyfw.12306.cn/passport/captcha/captcha-image?' \
      'login_site=E&module=login&rand=sjrand'
r = session.get(url, headers=headers, verify=False)
# 不做证书验证
# 保存图片
with open('code.png', 'wb') as f:
    f.write(r.content)
print('请输入验证码坐标代号：')
code=input()
write=code.split(',')
codes=''
for i in write:
    codes+=code_list[i]

data = {
    'answer': codes,
    'login_site': 'E',
    'rand': 'sjrand'
}
url = 'https://kyfw.12306.cn/passport/captcha/captcha-check'
r = session.post('https://kyfw.12306.cn/passport/captcha/captcha-check', headers=headers, data=data)
print(r.text)
print(data)
print(code)
