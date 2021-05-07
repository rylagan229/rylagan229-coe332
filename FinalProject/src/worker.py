from jobs import q, update_job_status
import matplotlib.pyplot as plt
import time
import datetime
import redis

redis_ip = '10.105.120.63'
rd_job = redis.StrictRedis(host=redis_ip, port=6379, db=0)
rd = redis.StrictRedis(host=redis_ip, port=6379, db=0)

# Analysis Job goes here:
# Create a graph of the Animal Type by date

@q.worker
def execute_job(jid):
    data = json.loads(rd.get('data'))
    dates = []
    intakecount = []

    # Fill values to plot...
    # Want x values to be Time, and y values to be the number of intakes on the date
    start = rd_job.hget(job_id,'start').decode('utf-8'))
    end = rd_job.hget(job_id, 'end').decode('utf-8'))
    
    # Use datetime to pull the request startdate and enddate
    startdate = datetime.datetime.strptime(start,'%m-$d-%Y')

    enddate = datetime.datetime.strptime(end, '%m-%d-$Y')
    
    # initialize the base animal count per day at 0
    dailyintakecount = 0
    jsonList = data['intakes']
    for i in data:
        datetime = i['DateTime']
        if (start <= DateTime and end >= end)
            dates.append(DateTime)
            dailyintakecount = dailyintakecount + 1
            
        intakecount.append(dailyintakecount)

    plt.scatter(dates, intakecount)
    plt.xlabel('Time')
    plt.ylabel('Number of Intakes')
    plt.savefig('/output_image.png')


    with open('/output_image.png', 'rb') as f:
        img = f.read()

    rd.hset(jobid, 'image', img)
    rd.hset(jobid, 'status', 'finished')

if __name__ == '__main__':
    execute_job()
