from locust import HttpUser, between, SequentialTaskSet, task
from locust_plugins import run_single_user
from lxml import html


class Exercise1Tasks(SequentialTaskSet):
    wait_time = between(4, 6)

    @task
    def GET_https_antycaptcha_amberteam_pl_2022377847__exercises_exercise1_1359742899_8059969736143727959(self):
        response = self.client.get(
            url='/exercises/exercise1',
            name='10-10 /exercises/exercise1',
            timeout=30, allow_redirects=False,
            verify=False,
            headers={'referer': 'https://antycaptcha.amberteam.pl/', 'upgrade-insecure-requests': '1',
                     'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36',
                     'sec-ch-ua': '"Google Chrome";v="95", "Chromium";v="95", ";Not A Brand";v="99"',
                     'sec-ch-ua-mobile': '?0', 'sec-ch-ua-platform': '"Windows"'})
        tree = html.fromstring(response.text)
        buttons = tree.cssselect('code')
        self.button1 = buttons[0].text[-1]
        self.button2 = buttons[1].text[-1]
        self.button3 = buttons[2].text[-1]
        pass

    @task
    def POST_https_antycaptcha_amberteam_pl_2022377847__exercises_exercise1_button2_2616658608_7104982136376662838(
            self):
        response = self.client.post(url=f'/exercises/exercise1/button{self.button1}',
                                    name='10-20 /exercises/exercise1/button1', timeout=30, verify=False,
                                    allow_redirects=False, headers={'accept': 'application/json, text/*',
                                                                    'content-type': 'application/json; charset=utf-8',
                                                                    'referer': 'https://antycaptcha.amberteam.pl/exercises/exercise1?seed=c59b002c-b9f2-4f8c-91a0-980eeb80dbb8',
                                                                    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36',
                                                                    'sec-ch-ua': '"Google Chrome";v="95", "Chromium";v="95", ";Not A Brand";v="99"',
                                                                    'sec-ch-ua-mobile': '?0',
                                                                    'sec-ch-ua-platform': '"Windows"'})

    @task
    def POST_https_antycaptcha_amberteam_pl_2022377847__exercises_exercise1_button2_2616658608_5732882860546841492(
            self):
        response = self.client.post(url=f'/exercises/exercise1/button{self.button2}',
                                    name='10-30 /exercises/exercise1/button2', timeout=30, verify=False,
                                    allow_redirects=False, headers={'accept': 'application/json, text/*',
                                                                    'content-type': 'application/json; charset=utf-8',
                                                                    'referer': 'https://antycaptcha.amberteam.pl/exercises/exercise1?seed=c59b002c-b9f2-4f8c-91a0-980eeb80dbb8',
                                                                    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36',
                                                                    'sec-ch-ua': '"Google Chrome";v="95", "Chromium";v="95", ";Not A Brand";v="99"',
                                                                    'sec-ch-ua-mobile': '?0',
                                                                    'sec-ch-ua-platform': '"Windows"'})

    @task
    def POST_https_antycaptcha_amberteam_pl_2022377847__exercises_exercise1_button2_2616658608_6717462467804921238(
            self):
        response = self.client.post(url=f'/exercises/exercise1/button{self.button3}',
                                    name='10-40 /exercises/exercise1/button3', timeout=30, verify=False,
                                    allow_redirects=False, headers={'accept': 'application/json, text/*',
                                                                    'content-type': 'application/json; charset=utf-8',
                                                                    'referer': 'https://antycaptcha.amberteam.pl/exercises/exercise1?seed=c59b002c-b9f2-4f8c-91a0-980eeb80dbb8',
                                                                    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36',
                                                                    'sec-ch-ua': '"Google Chrome";v="95", "Chromium";v="95", ";Not A Brand";v="99"',
                                                                    'sec-ch-ua-mobile': '?0',
                                                                    'sec-ch-ua-platform': '"Windows"'})

    @task
    def POST_https_antycaptcha_amberteam_pl_2022377847__exercises_exercise1_solution_2814839647_2347838174168288982(
            self):
        with self.client.post(url='/exercises/exercise1/solution',
                              name='10-50 /exercises/exercise1/solution',
                              timeout=30,
                              catch_response=True,
                              verify=False,
                              allow_redirects=False, headers={'accept': 'application/json, text/*',
                                                              'content-type': 'application/json; charset=utf-8',
                                                              'referer': '/exercises/exercise1?seed=c59b002c-b9f2-4f8c-91a0-980eeb80dbb8',
                                                              'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36',
                                                              'sec-ch-ua': '"Google Chrome";v="95", "Chromium";v="95", ";Not A Brand";v="99"',
                                                              'sec-ch-ua-mobile': '?0',
                                                              'sec-ch-ua-platform': '"Windows"'}) as response:
            trail = response.json()['trail']
            if trail != 'OK. Good answer':
                response.failure('Not a good answer.')
            pass

    @task
    def last(self):
        self.interrupt()


# just for debugging
if __name__ == '__main__':
    class Exercise1(HttpUser):
        tasks = [Exercise1Tasks]
        host = 'https://antycaptcha.amberteam.pl'


    run_single_user(Exercise1)
