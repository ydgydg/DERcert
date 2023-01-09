
from redis import *
import json

f = open("config.json", "r")
fs = json.loads(f.read())
f.close()
dstHost = fs["destHost"]
rsHost = fs["redisHost"]

port = int(fs["redisPort"])
redis_pass = fs["redisPass"]

ScanListRs = StrictRedis(host=rsHost, port=port, password=redis_pass, db=1)


ResListRs = StrictRedis(host=rsHost, port=port, password=redis_pass, db=2)
SuccessListRs = StrictRedis(host=rsHost, port=port, password=redis_pass, db=3)
LogRedis = StrictRedis(host=rsHost, port=port, password=redis_pass, db=5)
broker = "redis://{password}@{host}:{port}/4".format(password=redis_pass, host=rsHost, port=port)
backend = "redis://{password}@{host}:{port}/5".format(password=redis_pass, host=rsHost, port=port)

# Timeout period
timeout = int(fs["timeout"])

