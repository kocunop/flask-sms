import requests

HTTP_RPC_URL = 'http://api.sms24x7.ru/'

class SMS24x7(object):
  def __init__(self, email=None, passwd=None, default_from=None):
    self._email = email
    self._passwd = passwd
    #self.auth(email,passwd)
    self.default_from = default_from
    self.cookies = None

  def auth(self):
    params = {'method':'login', 'email':self._email, 'password':self._passwd, 'format':'JSON'}
    r = requests.get('http://api.sms24x7.ru/',params=params)
    self.cookies = r.cookies


  def send(self, text, phone, sender_name=None):
    assert self.cookies, "login first"
    pmsg = dict(method='push_msg',
                text=text,
                phone=phone,
                sender_name=sender_name or self.default_from,
                )
    r = requests.get('http://api.sms24x7.ru/',params=pmsg, cookies=self.cookies)
