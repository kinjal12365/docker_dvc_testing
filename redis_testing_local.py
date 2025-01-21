from flask import Flask
import redis

# Initialize Redis connection
redis_cache = redis.Redis(host='localhost', port=6379)

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello, world!'

@app.route('/set/<string:key>/<string:value>')
def set_key(key, value):
    if redis_cache.exists(key):
        return f'Key "{key}" already exists with value "{redis_cache.get(key)}".', 200
    else:
        redis_cache.set(key, value)
        return f'Key "{key}" set with value "{value}".', 201

@app.route('/get/<string:key>')
def get_value(key):
    if redis_cache.exists(key):
        value = redis_cache.get(key)
        return f'Value for key "{key}" is "{value}".', 200
    else:
        return f'Value for key "{key}" does not exist.', 404

if __name__ == '__main__':
    app.run(debug=True)
