from jovian.pythondsa import evaluate_test_cases
import math
tests = [{'input': {'cards': [13, 11, 10, 7, 4, 3, 1, 0], 'query': 7}, 'output': 3},
 {'input': {'cards': [13, 11, 10, 7, 4, 3, 1, 0], 'query': 1}, 'output': 6},
 {'input': {'cards': [4, 2, 1, -1], 'query': 4}, 'output': 0},
 {'input': {'cards': [3, -1, -9, -127], 'query': -127}, 'output': 3},
 {'input': {'cards': [6], 'query': 6}, 'output': 0},
 {'input': {'cards': [9, 7, 5, 2, -9], 'query': 4}, 'output': -1},
 {'input': {'cards': [], 'query': 7}, 'output': -1},
 {'input': {'cards': [8, 8, 6, 6, 6, 6, 6, 3, 2, 2, 2, 0, 0, 0], 'query': 3},
  'output': 7},
 {'input': {'cards': [8, 8, 6, 6, 6, 6, 6, 6, 3, 2, 2, 2, 0, 0, 0],
   'query': 6},
  'output': 7}]

def locate_card(cards, query):
    """
    finds the location of the card
    :param cards: input query
    :param query: value of search
    :return: -1 if the card does not contain that
    """
    if len(cards) == 0:
        return -1
    else:
        l = 0
        r = len(cards) - 1
        while l <= r:
            m = math.floor((r+l)/2)
            if cards[m] == query:
                return m
            elif cards[m] < query:
                r = m - 1
            elif cards[m] > query:
                l = m + 1
        return -1

evaluate_test_cases(locate_card, tests)
#print(locate_card([6],6))