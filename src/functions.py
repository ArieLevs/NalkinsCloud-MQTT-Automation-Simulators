
from pkg_resources import get_distribution, DistributionNotFound


def is_valid_topic(topic):
    if type(topic) is not str:
        return False

    parsed_topic = topic.split('/')
    for i in range(len(parsed_topic)):
        if not parsed_topic[i]:  # Check if string inside each array cell is not null or empty
            return False
    return len(parsed_topic) == 3


def get_self_version(dist_name):
    """
    Return version number of input distribution name,
    If distribution not found return not found indication
    :param dist_name: string
    :return: version as string
    """
    try:
        return get_distribution(dist_name).version
    except DistributionNotFound:
        return 'version not found'
