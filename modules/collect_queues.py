import requests


def collect_queues(url):
    result = requests.get(url)
    return result.json()


def extract_queue(url):
    return collect_queues(url).get("pendingTasks")
