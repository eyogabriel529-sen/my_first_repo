"""Functions for tracking poker hands and assorted card tasks.

Python list documentation: https://docs.python.org/3/tutorial/datastructures.html
"""


def get_rounds(number):
    """Create a list containing the current and next two round numbers.

    :param number: int - current round number.
    :return: list - current round and the two that follow.
    """

    return [number, number + 1, number + 2]


def concatenate_rounds(rounds_1, rounds_2):
    """Concatenate two lists of round numbers.

    :param rounds_1: list - first rounds played.
    :param rounds_2: list - second set of rounds played.
    :return: list - all rounds played.
    """

    return rounds_1 + rounds_2


def list_contains_round(rounds, number):
    """Check if the list of rounds contains the specified number.

    :param rounds: list - rounds played.
    :param number: int - round number.
    :return: bool - was the round played?
    """

    return number in rounds
        
        


def card_average(hand):
    """Calculate and returns the average card value from the list.

    :param hand: list - cards in hand.
    :return: float - average value of the cards in the hand.
    """

    return sum(hand) / len(hand)


def approx_average_is_average(hand):
    """Return if the (average of first and last card values) OR ('middle' card) == calculated average.

    :param hand: list - cards in hand.
    :return: bool - does one of the approximate averages equal the `true average`?
    """

    list_length = len(hand)
    
    # Calculate the true average of all cards
    true_average = sum(hand) / list_length
    
    # Calculate the first approximation: average of the first and last cards
    first_approx = (hand[0] + hand[-1]) / 2
    
    # Check if the first approximation equals the true average
    if first_approx == true_average:
        return True
    
    # Calculate the second approximation: the middle card value(s)
    # If the list length is odd, there is one middle element
    if list_length % 2 == 1:
        middle_index = list_length // 2
        middle_card_value = hand[middle_index]
        if middle_card_value == true_average:
            return True
            
    # If the list length is even, there are two middle elements
    else:
        middle_index_1 = list_length // 2 - 1
        middle_index_2 = list_length // 2
        # The prompt implies a single 'middle' card so this logic is an interpretation.
        # A more robust solution might average these two cards.
        if hand[middle_index_1] == true_average or hand[middle_index_2] == true_average:
            return True
            
    # If neither approximation matches, return False
    return False


def average_even_is_average_odd(hand):
    """Return if the (average of even indexed card values) == (average of odd indexed card values).

    :param hand: list - cards in hand.
    :return: bool - are even and odd averages equal?
    """

    sum_even = 0
    count_even = 0
    sum_odd = 0
    count_odd = 0
    
    # Iterate through the list using its indices
    for i in range(len(hand)):
        # Check if the index is even or odd
        if i % 2 == 0:
            sum_even += hand[i]
            count_even += 1
        else:
            sum_odd += hand[i]
            count_odd += 1

    # Check for division by zero if lists are empty
    # Note: A simple 'hand' of [1, 2] will have sum_odd and count_odd = 2
    if count_even == 0 or count_odd == 0:
        return False
        
    # Calculate averages
    avg_even = sum_even / count_even
    avg_odd = sum_odd / count_odd
    
    # Compare the averages and return the result
    return avg_even == avg_odd


def maybe_double_last(hand):
    """Multiply a Jack card value in the last index position by 2.

    :param hand: list - cards in hand.
    :return: list - hand with Jacks (if present) value doubled.
    """

    last_card_index = -1
    
    # Check if the list is not empty before accessing the element
    if hand:
        # Check if the value of the last card is 11
        if hand[last_card_index] == 11:
            # If it's a Jack, double its value
            hand[last_card_index] *= 2
            
    # Return the modified (or unmodified) hand
    return hand
