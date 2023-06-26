from locust import SequentialTaskSet, task, between, HttpUser, run_single_user
import locust_plugins
from lxml import html


class Exercise3Tasks(SequentialTaskSet):
    wait_time = between(4, 6)

    @task
    def GET_https_antycaptcha_amberteam_pl_2022377847__exercises_exercise3_1359873973_7117410998266986988(self):
        response = self.client.get(
            url='/exercises/exercise3',
            name='30-10 /exercises/exercise3',
            timeout=30,
            allow_redirects=False,
            verify=False,
            headers={'upgrade-insecure-requests': '1',
                     'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36',
                     'sec-ch-ua': '"Google Chrome";v="95", "Chromium";v="95", ";Not A Brand";v="99"',
                     'sec-ch-ua-mobile': '?0',
                     'sec-ch-ua-platform': '"Windows"'})
        tree = html.fromstring(response.text)
        self.v = tree.cssselect('code')[1].text[-1]
        pass

    @task
    def POST_https_antycaptcha_amberteam_pl_2022377847__exercises_exercise3_dropdown_2807237457_5053799924764131226(
            self):
        response = self.client.post(
            url='/exercises/exercise3/dropdown',
            name='30-20 /exercises/exercise3/dropdown',
            timeout=30,
            verify=False,
            allow_redirects=False,
            headers={'accept': 'application/json, text/*',
                     'content-type': 'application/json; charset=UTF-8',
                     'referer': 'https://antycaptcha.amberteam.pl/exercises/exercise3',
                     'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36',
                     'sec-ch-ua': '"Google Chrome";v="95", "Chromium";v="95", ";Not A Brand";v="99"',
                     'sec-ch-ua-mobile': '?0',
                     'sec-ch-ua-platform': '"Windows"'},
            json={'s13': f'v{self.v}'})

    @task
    def POST_https_antycaptcha_amberteam_pl_2022377847__exercises_exercise3_solution_2816150369_3087939721231510724(
            self):
        with self.client.post(
                url='/exercises/exercise3/solution',
                name='30-30 /exercises/exercise3/solution',
                timeout=30,
                catch_response=True,
                verify=False,
                allow_redirects=False,
                headers={'accept': 'application/json, text/*',
                         'content-type': 'application/json; charset=UTF-8',
                         'referer': 'https://antycaptcha.amberteam.pl/exercises/exercise3',
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


if __name__ == '__main__':
    class Exercise3(HttpUser):
        tasks = [Exercise3Tasks]
        host = 'https://antycaptcha.amberteam.pl'


    run_single_user(Exercise3)
