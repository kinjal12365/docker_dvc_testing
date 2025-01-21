from flask import Flask
import redis
import time

redis_cache = redis.Redis(host='redis',port=6379)
app=Flask(__name__)

def get_hit_count():
    retries=5
    while True:
        try:
            # redis_cache.reset_retry_count()
            return redis_cache.incr('hits')
        except redis.exceptions.ConnectionError as exc:
            if retries ==0:
                raise exc
            retries -=1
            time.sleep(0.5)


@app.route('/')
def get_count():
    count=get_hit_count()
    return f'hello kinjal ! i have been seen {count} times.\n'
    
    