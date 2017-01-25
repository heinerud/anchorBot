import tweepy, json, time

CONSUMER_KEY = ''
CONSUMER_SECRET = ''
ACCESS_KEY = ''
ACCESS_SECRET = ''
AUTH = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
AUTH.set_access_token(ACCESS_KEY, ACCESS_SECRET)
API = tweepy.API(AUTH, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

# TODO: Tune virality
def virality(status):
    return (1.0*status.retweet_count)/status.user.followers_count

def getTimeline():
    page = 1
    newTimeline = API.home_timeline(since_id=lastRetweeted.retweeted_status.id, page=page)
    timeline = newTimeline
    while len(newTimeline) > 0:
        page += 1
        newTimeline = API.home_timeline(since_id=lastRetweeted.retweeted_status.id, page=page)
        timeline = newTimeline + timeline
    return timeline

lastRetweeted = API.user_timeline()[0]
print(lastRetweeted.text)
print

timeline = getTimeline()
bestStatus = timeline[0]

while True:
    for status in timeline:
        if virality(status) > virality(bestStatus):
            bestStatus = status

    compareId = bestStatus.id
    if bestStatus.retweeted:
        compareId = bestStatus.retweeted_status.id

    if lastRetweeted.retweeted_status.id != compareId:
        #print json.dumps(lastRetweeted._json, indent=4)
        #print "---------------------------------------------"
        #print json.dumps(bestStatus._json, indent=4)
        #print
        API.retweet(bestStatus.id)
        lastRetweeted = API.user_timeline()[0]
        print "RT!"
        print bestStatus.text

    print "Sleeping..."
    time.sleep(60)
    timeline = getTimeline()
