from jobs import q, update_job_status
import matplotlib.pyplot as plt
import time
import redis

redis_ip = '10.105.227.117'
rd_job = redis.StrictRedis(host=redis_ip, port=6379, db=0)

@q.worker
def execute_job(jid):
    update_job_status(jid, 'in progress')
    time.sleep(15)
    update_job_status(jid, 'complete')
    
if __name__ == '__main__':
    execute_job()
