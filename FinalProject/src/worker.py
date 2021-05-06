from jobs import q, update_job_status
import matplotlib.pyplot as plt
import time
import redis

redis_ip = '10.105.227.117'
rd_job = redis.StrictRedis(host=redis_ip, port=6379, db=0)

# Analysis Job goes here:
# Create a graph of the Animal Type by date?

@q.worker
def execute_job(jid):
    update_job_status(jid, 'in progress')
    time.sleep(15)
    update_job_status(jid, 'complete')
    x_values_to_plot = []
    y_values_to_plot = []

    for key in raw_data.keys():       # raw_data.keys() is a client to the raw data stored in redis
        if (int(start) <= key['date'] <= int(end)):
            x_values_to_plot.append(key['interesting_property_1'])
            y_values_to_plot.append(key['interesting_property_2'])

    plt.scatter(x_values_to_plot, y_values_to_plot)
    plt.savefig('/output_image.png')
    
if __name__ == '__main__':
    execute_job()
