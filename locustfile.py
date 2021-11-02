from locust import HttpUser

from locustfiles.exercise1 import Exercise1Tasks


class AntyCaptchaTest(HttpUser):
    tasks = {Exercise1Tasks: 100}
    host = 'https://antycaptcha.amberteam.pl'
