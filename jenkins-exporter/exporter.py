import time
import random

from prometheus_client import start_http_server, Gauge
from jenkinsapi.jenkins import Jenkins

jenkins_client = Jenkins('http://jenkins:8080/', username = 'admin', password = 'admin')

JENKINS_JOB_COUNT = Gauge('jenkins_jobs_count', "Number of Jenkins jobs")
JENKINS_JOB_RUNNING_COUNT = Gauge('jenkins_jobs_running_count', "Number of running Jenkins jobs")


def get_metrics():
    JENKINS_JOB_COUNT.set(len(list(jenkins_client.get_jobs())))
    runningJobs = []
    for job_name, job_instance in jenkins_client.get_jobs():
        if job_instance.is_running():
            runningJobs += [job_instance.name]
    JENKINS_JOB_RUNNING_COUNT.set(len(runningJobs)) 

    
if __name__ == '__main__':

    # Start up the server to expose the metrics.
    start_http_server(8000)
    while True:
        get_metrics()
        time.sleep(random.randrange(1,10))