"""Functions for organizing and calculating student exam scores."""


def round_scores(student_scores):
    """Round all provided student scores.

    :param student_scores: list - float or int of student exam scores.
    :return: list - student scores *rounded* to nearest integer value.
    """

    rounded = []
    for score in student_scores:
        rounded.append(round(score))
    return rounded


def count_failed_students(student_scores):
    """Count the number of failing students out of the group provided.

    :param student_scores: list - containing int student scores.y
    :return: int - count of student scores at or below 40.
    """

    fail = []
    for score in student_scores:
        if score <= 40:
            fail.append(score)
    return len(fail)


def above_threshold(student_scores, threshold):
    """Determine how many of the provided student scores were 'the best' based on the provided threshold.

    :param student_scores: list - of integer scores.
    :param threshold: int - threshold to cross to be the "best" score.
    :return: list - of integer scores that are at or above the "best" threshold.
    """

    best = []
    for score in student_scores:
        if score >= threshold:
            best.append(score)
    return best
     
    

def letter_grades(highest):
    """Create a list of grade thresholds based on the provided highest grade.

    :param highest: int - value of highest exam score.
    :return: list - of lower threshold scores for each D-A letter grade interval.
            For example, where the highest score is 100, and failing is <= 40,
            The result would be [41, 56, 71, 86]:

            41 <= "D" <= 55
            56 <= "C" <= 70
            71 <= "B" <= 85
            86 <= "A" <= 100
    """

    FAILING_THRESHOLD = 40
    NUM_GRADES = 4 # D, C, B, A

    # 1. Calculate the total score range available for letter grades (above 40)
    score_range = highest - FAILING_THRESHOLD

    # 2. Calculate the step size (the width) of each of the four equal intervals.
    step_size = score_range // NUM_GRADES

    # 3. Calculate the lower threshold for each grade (D, C, B, A)

    thresholds = []

   
    for i in range(NUM_GRADES):
        # Calculate the upper bound of the *previous* grade's interval (or F's upper bound for i=0).
        # upper_bound_prev = FAILING_THRESHOLD + i * step_size

        # The lower threshold for the current grade is 1 point above the previous
        # calculated upper bound.
        lower_threshold = FAILING_THRESHOLD + (i * step_size) + 1
        thresholds.append(lower_threshold)

    return thresholds




def student_ranking(student_scores, student_names):
    """Organize the student's rank, name, and grade information in descending order.

    :param student_scores: list - of scores in descending order.
    :param student_names: list - of string names by exam score in descending order.
    :return: list - of strings in format ["<rank>. <student name>: <score>"].
    """

    # Combine scores and names using zip, then sort by score descending
    # But since both are already in descending order, we can pair directly
    ranked = []
    for rank, (score, name) in enumerate(zip(student_scores, student_names), 1):
        ranked.append(f"{rank}. {name}: {score}")
    return ranked


def perfect_score(student_info):
    """Create a list that contains the name and grade of the first student to make a perfect score on the exam.

    :param student_info: list - of [<student name>, <score>] lists.
    :return: list - first `[<student name>, 100]` or `[]` if no student score of 100 is found.
    """

    for student in student_info:
        # Check if the score (the second element, index 1) is 100
        # The score is assumed to be an integer (as per the example).
        if student[1] == 100:
            # If a perfect score is found, return the entire student record immediately.
            # We return the FIRST match, as required by the prompt.
            return student

    # If the loop finishes without finding any score of 100, return an empty list.
    return []

