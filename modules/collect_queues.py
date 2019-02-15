"""
Functions to handle the queues from queues.taskcluster.com
Collecting the queues number is done via a json request, that get's parsed to
a result that is then converted using .json(), thus making the variable return
the "pendingTasks" when a request is done via get().
"""
import requests


def collect_queues(url):
    """
    Requests the data from the API.
    :param url: API url to do the request
    :return: returns a json formatted object
    """
    result = requests.get(url)
    return result.json()


def extract_queue(url):
    """
    Extracts the pending tasks calling the get() function on the JSON object.
    :param url: API url to do the request that get's parsed to collect_queues()
    function.
    :return: returns an int with the number of pending tasks.
    """
    return collect_queues(url).get("pendingTasks")

