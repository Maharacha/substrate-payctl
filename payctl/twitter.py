import tweepy
from .utils import *


class Twitter():
    def __init__(self, config):
        self.auth = tweepy.OAuthHandler(
            config['Twitter'].get('consumerkey'),
            config['Twitter'].get('consumersecret')
        )
        self.auth.set_access_token(
            config['Twitter'].get('accesstokenkey'),
            config['Twitter'].get('accesstokensecret')
        )

    def update_status(self, text):
        api = tweepy.API(self.auth)
        try:
            api.update_status(status=text) 
        except tweepy.error.TweepError as e:
            print('Update twitter status failed: ' + str(e))

    @staticmethod
    def generate_tweet_text(eras_payment_info):
        total_reward = 0
        for era in eras_payment_info:
            for accountId in eras_payment_info[era]:
                if eras_payment_info[era][accountId]['claimed'] is not True:
                    total_reward = total_reward + eras_payment_info[era][accountId]['amount']
        total_reward = round(total_reward, 4)
        tweet_text = 'Payout has been made for eras: ' + ', '.join([str(era) for era in eras_payment_info])
        tweet_text = tweet_text + '\nA total of {} KSM\nCongratulation all stakers!'.format(total_reward)
        return tweet_text
