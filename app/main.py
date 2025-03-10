from flask import Flask, jsonify
import redis
import os

app = Flask(__name__)

# Connect to Redis
redis_client = redis.Redis(
    host=os.getenv("REDIS_HOST", "localhost"),
    port=int(os.getenv("REDIS_PORT", 6379)),
    decode_responses=True
)

@app.route('/')
def home():
    redis_client.incr('hits')  # Increment a counter in Redis
    count = redis_client.get('hits')
    return jsonify({"message": "Hello, Flask with Redis!", "hits": count})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
