import re
import long_responses as long


def message_probability(user_message, recognised_words, single_response=False, required_words=[]):
    message_certainty = 0
    has_required_words = True

    for word in user_message:
        if word in recognised_words:
            message_certainty += 1

    percentage = float(message_certainty) / float(len(recognised_words))

    for word in required_words:
        if word not in user_message:
            has_required_words = False
            break

    if has_required_words or single_response:
        return int(percentage * 100)
    else:
        return 0

def check_all_messages(message):
    highest_prob_list = {}

    def response(bot_response, list_of_words, single_response=False, required_words=[]):
        nonlocal highest_prob_list
        highest_prob_list[bot_response] = message_probability(message, list_of_words, single_response, required_words)

    response('Hey sasi!', ['hello', 'hi', 'hey', 'sup', 'heyo'], single_response=True)
    response('Goodbye Tata!', ['bye', 'goodbye'], single_response=True)
    response('I\'m fine, What about you?', ['how', 'are', 'you', 'doing'], required_words=['how'])
    response("That's great, How can I help you today", ['fine','good'], single_response=True)
    response("You are Welcome!", ['thank', 'thanks'], single_response=True)
    response('I am grateful!', ['i', 'love', 'code', 'palace'], required_words=['code', 'palace'])

    response(long.R_HATE, ['i', 'hate', 'you'], required_words=['i', 'hate', 'you'])
    response(long.R_SHOPPING, ['give', 'advice','budget','go','shopping'], required_words=['give', 'advice','budget','go','shopping'])
    response(long.R_WALKING, ['walking', 'I', 'walk'], required_words=['I', 'walk','walking'])

    best_match = max(highest_prob_list, key=highest_prob_list.get)

    return long.unknown() if highest_prob_list[best_match] < 1 else best_match

def get_response(user_input):
    split_message = re.split(r'\s+|[,;?!.-]\s*', user_input.lower())
    response = check_all_messages(split_message)
    return response

while True:
    print('Alice: ' + get_response(input('You: ')))