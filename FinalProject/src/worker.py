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
    jobid, status, start, end = rd_job.hmget(generate_job_key(jid), 'id', 'status', 'start', 'end', 'animal_type')
    x_values_to_plot = []
    y_values_to_plot = []

    # Fill values to plot...
    # Want x values to be Time, and y values to be the number of intakes on the date
    start = job['start']
    end = job['end']
    
    # Use datetime to pull the request startdate and enddate
    startdate = datetime.datetime.strptime(start,'%m-$d-%Y')

    enddate = datetime.datetime.strptime(end, '%m-%d-$Y')

    for key in rd.keys():
        datetimekey = str(rd.get(key, 'DateTime')
        if (int(start) <= key['DateTime'] <= int(end)):
            x_values_to_plot.append(key)
            y_values_to_plot.append(key)

    plt.scatter(x_values_to_plot, y_values_to_plot)
    plt.xlabel('Time')
    plt.ylabel('Number of Intakes')
    plt.savefig('/output_image.png')


    with open('/output_image.png', 'rb') as f:
        img = f.read()

    rd.hset(jobid, 'image', img)
    rd.hset(jobid, 'status', 'finished')

if __name__ == '__main__':
    execute_job()
