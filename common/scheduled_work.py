
#in debug model, this will execute twice
import time

from common.blacklist import token_blacklist
from apscheduler.schedulers.background import BackgroundScheduler

#if the token in the blacklist has already expires, it is invalid even not in the blacklist.
# So remove it from the blacklist.
def clear():
    for token in token_blacklist:
        if token_blacklist[token] < time.time():
            token_blacklist.pop(token)


scheduler = BackgroundScheduler()
scheduler.add_job(clear, 'interval', minutes=30)
scheduler.start()