

def is_valid_topic(topic):
    print("Validating topic - '" + topic + "'")
    parsed_topic = topic.split('/')
    for i in range(len(parsed_topic)):
        if not parsed_topic[i]:  # Check if string inside each array cell is not null or empty
            return False
    return len(parsed_topic) == 3
