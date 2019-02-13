# Pending Queue Monitor

## Monitors the pending tasks queue on different machines for Taskcluster Infrastructure.

### List of clusters to be monitored

- #### Releng Hardware

    - gecko-t-win10-64-ms
    - gecko-t-osx-1010
    - gecko-t-linux-talos
    - gecko-t-linux-talos-b
    - gecko-t-osx-1010-beta
    - gecko-t-win10-64-us

- #### AWS Provisioner

    - gecko-t-linux-xlarge
    - gecko-t-linux-large
    - gecko-t-win7-32
    - gecko-3-b-win2012
    - gecko-3-b-linux
    - gecko-t-win7-32-gpu
    - gecko-t-win10-64
    - gecko-1-b-linux
    - gecko-1-b-win2012
    - mobile-3-b-andrcmp
    - gecko-t-win10-64-gpu
    - github-worker
    - releng-svc
    - gecko-1-b-android
    - gecko-3-b-android
    - releng-svc-prod
    - symbol-upload
    - gecko-3-decision
    - gecko-misc
    - releng-svc-memory
    - wpt-docker-worker
    - servo-docker-worker
    - gecko-1-decision
    - application-services-r
    - gecko-2-decision
    - gecko-focus
    - mobile-1-b-fenix
    - mobile-1-decision
    - mobile-3-decision
    - taskcluster-images
    - gecko-1-images
    - gecko-3-images
    - gecko-t-win10-64-alpha
    - hg-worker
    - mobile-1-b-andrcmp
    - mobile-1-images
    - servo-win2016
    - taskcluster-generic
    - android-components-g
    - gecko-1-b-linux-large
    - gecko-3-b-linux-large
    - gecko-decision
    - gecko-t-win10-64-cu
    - gecko-t-win7-32-cu
    - mobile-3-b-fenix
    - releng-svc-compute
    - servo-docker-untrusted
    - tutorial
    - win2012r2-cu

### Getting data from taskcluster

It is done using the Queue API/Service from taskcluster and a typical request looks like:

for the releng-hardware

```html
https://queue.taskcluster.net/v1/pending/releng-hardware/gecko-t-osx-1010
```

and for AWS-Provisioned machines:

```html
https://queue.taskcluster.net/v1/pending/aws-provisioner-v1/gecko-t-linux-xlarge
```

The repose is a JSON that looks like:

```json
{

    "provisionerId": "releng-hardware",
    "workerType": "gecko-t-win10-64-ms",
    "pendingTasks": 0

}
```

We are going to do a request once at 5-10 minutes, so that would be 10-12 requests and hour for each cluster type.

### How to display the values/data

For the moment we want to display a few graphs with fixed time-base:
- one day
- one week
- one month
- 3 months
- 6 months
- 1 year
- All time

### Storing data

Since all of this data is going to be later used and graphs updated as times fly,  we are putting the problem of how are we going to store all of the data.
The most suited case for this would be CSV files for each type of clusters.

#### Storing the generated graphs

Short answer would be: **Adding them to the github repository and embedding them in a markdown.**


For later use:
 - https://plot.ly/python/time-series/#reference
 - https://realpython.com/python-csv/
 - https://guides.github.com/features/mastering-markdown/
