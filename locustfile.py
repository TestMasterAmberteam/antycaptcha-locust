from locust import HttpUser, FastHttpUser

from locustfiles.exercise1 import Exercise1Tasks
from locustfiles.exercise2 import Exercise2Tasks
from locustfiles.exercise3 import Exercise3Tasks


class AntyCaptchaTest(FastHttpUser):
    tasks = {Exercise1Tasks: 25,
             Exercise2Tasks: 40,
             Exercise3Tasks: 35
             }
    host = 'https://antycaptcha.amberteam.pl'
