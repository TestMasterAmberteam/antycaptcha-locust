from locust import HttpUser

from locustfiles.exercise1 import Exercise1Tasks
from locustfiles.exercise2 import Exercise2Tasks


class AntyCaptchaTest(HttpUser):
    tasks = {Exercise1Tasks: 50,
             Exercise2Tasks: 50}
    host = 'https://antycaptcha.amberteam.pl'
