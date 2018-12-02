#On a Python file, initially import the necessary modules we’ll be using. 
#In addition to importing the packages we’ve just installed, we’ll also need 
#other packages like datetime and json. 

from random import choice
from datetime import datetime
import json
import requests
from bs4 import BeautifulSoup
import pymysql
import pymysql.cursors

#Next, we’ll define a USER_AGENTS variable which will hold a few options for 
#mocking a browser request to the Instagram web app. The script will randomly 
#choose one of the values you’ll define here. This is to minimise the risk for 
#getting blocked of making requests to the website on the assumption that we’re spamming.

USER_AGENTS = ['Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36']


#Next up, we’ll write an InstagramScraper object, which will accept the string url 
#for our destination page (i.e link to the Instagram profile page). The InstagramScraper 
#object will expose two methods, page_metrics and post_metrics.

#Once we initiate an object, we’ll be able to call either of these methods to get the 
#page/post data we want.

class InstagramScraper:
    def _init_(self, url, user_agents=None):
        self.url = url
        self.user_agents = user_agents

    def __random_agent(self):
        if self.user_agents and isinstance(self.user_agents, list):
            return choice(self.user_agents)
        return choice(USER_AGENTS)

    def __request_url(self):
        try:
            response = requests.get(
                        self.url,
                        headers={'User-Agent': self.__random_agent()})
            response.raise_for_status()
        except requests.HTTPError:
            raise requests.HTTPError('Received non-200 status code.')
        except requests.RequestException:
            raise requests.RequestException
        else:
            return response.text
    @staticmethod
    def extract_json(html):
        soup = BeautifulSoup(html, 'html.parser')
        body = soup.find('body')
        script_tag = body.find('script')
        raw_string = script_tag.text.strip().replace('window._sharedData =', '').replace(';', '')
        return json.loads(raw_string)
    
    def page_metrics(self):
        results = {}
        try:
            response = self.__request_url(self.url)
            json_data = self.extract_json(response)
            metrics = json_data['entry_data']['ProfilePage'][0]['graphql']['user']
        except Exception as e:
            raise e
        else:
            for key, value in metrics.items():
                if key != 'edge_owner_to_timeline_media':
                    if value and isinstance(value, dict):
                        value = value['count']
                        result[key] = value
        return results
    def post_metrics(self):
        results = []
        try:
            response = self.__request_url()
            json_data = self.extract_json(response)
            metrics = json_data['entry_data']['ProfilePage'][0]['graphql']['user']['edge_owner_to_timeline_media']['edges']
        except Exception as e:
            raise e
        else:
            for node in metrics:
                node = node.get('node')
                if node and isinstance(node,dict):
                    results.append(node)
        return results

#Now that we have defined our object class, we can now create a scraper object and call 
#either one of the methods.

// Define the URL for the profile page.
url = 'https://www.instagram.com/rhody9595/?hl=en'

// Initiate a scraper object and call one of the methods.
instagram = InstagramScraper(url)
post_metrics = instagram.post_metrics()

#MySQL

connection = pymysql.connect(host=DB_IP,
                             user=DB_USER,
                             password=DB_PASSWORD,
                             db=DB_NAME,
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)

update_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

for m in metrics:
    i_id = str(m['id'])
    i_post_time = datetime.fromtimestamp(
        m['taken_at_timestamp']).strftime('%Y-%m-%d %H:%M:%S')
    i_likes = int(m['edge_liked_by']['count'])
    i_comments = int(m['edge_media_to_comment']['count'])
    i_media = m['display_url']
    i_video = bool(m['is_video'])

    with connection.cursor() as cursor:
        sql = "INSERT INTO `data` (`update_time`, `post_id`, `post_time`, `post_likes`, `post_comments`, `post_media`, `post_is_video`) VALUES (%s, %s, %s, %s, %s, %s, %s)"
        cursor.execute(sql, (update_time, i_id, i_post_time,
                             i_likes, i_comments, i_media, i_video))

    connection.commit()

connection.close()