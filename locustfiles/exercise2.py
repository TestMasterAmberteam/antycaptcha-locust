from locust import SequentialTaskSet, HttpUser, task, between, FastHttpUser
from locust_plugins import run_single_user
from lxml import html


class Exercise2Tasks(SequentialTaskSet):
    wait_time = between(4, 6)

    @task
    def GET_https_antycaptcha_amberteam_pl_2022377847__exercises_exercise2_1359808436_6391876201501907287(self):
        response = self.client.get(
            path='/exercises/exercise2',
            name='20-10 /exercises/exercise2',
            timeout=30,
            allow_redirects=False,
            verify=False,
            headers={'upgrade-insecure-requests': '1',
                     'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36',
                     'sec-ch-ua': '"Google Chrome";v="95", "Chromium";v="95", ";Not A Brand";v="99"',
                     'sec-ch-ua-mobile': '?0',
                     'sec-ch-ua-platform': '"Windows"'})
        tree = html.fromstring(response.text)
        self.text = tree.cssselect('code')[0].text
        pass

    @task
    def POST_https_antycaptcha_amberteam_pl_2022377847__exercises_exercise2_button1_2617182896_3188366066458871254(
            self):
        response = self.client.post(
            path='/exercises/exercise2/button1',
            name='20-20 /exercises/exercise2/button1',
            timeout=30,
            allow_redirects=False,
            verify=False,
            headers={'accept': 'application/json, text/*',
                     # 'content-type': 'application/json; charset=UTF-8',
                     'referer': 'https://antycaptcha.amberteam.pl/exercises/exercise2',
                     'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36',
                     'sec-ch-ua': '"Google Chrome";v="95", "Chromium";v="95", ";Not A Brand";v="99"',
                     'sec-ch-ua-mobile': '?0',
                     'sec-ch-ua-platform': '"Windows"'},
            json={'t14': f'{self.text}'})

    @task
    def POST_https_antycaptcha_amberteam_pl_2022377847__exercises_exercise2_solution_2815495008_640161414438082191(
            self):
        with self.client.post(
                path='/exercises/exercise2/solution',
                name='20-30 /exercises/exercise2/solution',
                timeout=30,
                allow_redirects=False,
                catch_response=True,
                verify=False,
                headers={'accept': 'application/json, text/*',
                         # 'content-type': 'application/json; charset=UTF-8',
                         'referer': 'https://antycaptcha.amberteam.pl/exercises/exercise2',
                         'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36',
                         'sec-ch-ua': '"Google Chrome";v="95", "Chromium";v="95", ";Not A Brand";v="99"',
                         'sec-ch-ua-mobile': '?0',
                         'sec-ch-ua-platform': '"Windows"'}, json=0) as response:
            trail = response.json()['trail']
            if trail != 'OK. Good answer':
                response.failure('Not a good answer.')
            pass

    @task
    def last(self):
        self.interrupt()


# just for debugging
if __name__ == '__main__':
    class Exercise1(FastHttpUser):
        tasks = [Exercise2Tasks]
        host = 'https://antycaptcha.amberteam.pl'


    run_single_user(Exercise1)
