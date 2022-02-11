def choose(paragraphs, select, k):
    """Return the Kth paragraph from PARAGRAPHS for which SELECT called on the
    paragraph returns true. If there are fewer than K such paragraphs, return
    the empty string.
    """
    # BEGIN PROBLEM 1
    list = []
    for i in range(0, len(paragraphs)):
        s = i
        if select(paragraphs[s]):
            list.append(paragraphs[s])
    if k < len(list):
        return list[k]
    else:
        return ''
    # END PROBLEM 1


def about(topic):
    """Return a select function that returns whether a paragraph contains one
    of the words in TOPIC.

    >>> about_dogs = about(['dog', 'dogs', 'pup', 'puppy'])
    >>> choose(['Cute Dog!', 'That is a cat.', 'Nice pup!'], about_dogs, 0)
    'Cute Dog!'
    >>> choose(['Cute Dog!', 'That is a cat.', 'Nice pup.'], about_dogs, 1)
    'Nice pup.'
    """
    x = ()
    print(x)
    return True

about_dogs = about(['dog', 'dogs', 'pup', 'puppy'])
choose(['Cute Dog!', 'That is a cat.', 'Nice pup!'], about_dogs, 0)

for i in range(0, len(topic)):
    s = i
    if topic[s] in list:
        return true
    return False

    list = split('Cute Dog!')
    for i in range(0, len(list)):
        lower_key = lower(list[i])
        if str(lower_key) in topic:
            return True
        return False


    key1 = dict_diff.keys()
    reverse = sorted(key1, reverse=True)
    dict_reverse = {i:dict_diff.get(i) for i in reverse}


def autocorrect(user_word, valid_words, diff_function, limit):
    """Returns the element of VALID_WORDS that has the smallest difference
    from USER_WORD. Instead returns USER_WORD if that difference is greater
    than or equal to LIMIT.
    """
    # BEGIN PROBLEM 5
    list_diff = []
    dict_diff = {}
    dict_sequence = {}
    for i in range(0, len(valid_words)):
        list_diff.append(diff_function(user_word, valid_words[i], limit))
        dict_diff[diff_function(user_word, valid_words[i], limit)] = [valid_words[i]]
        dict_sequence[i] = [valid_words[i]]
    if min(tuple(list_diff)) >= limit:
        return user_word
    elif user_word in valid_words:
        return user_word
    elif min(tuple(list_diff)) == max(tuple(list_diff)):
        return dict_sequence.get(0)[0]
    else:
        return dict_diff.get(min(tuple(list_diff)))[0]


def autocorrect(user_word, valid_words, diff_function, limit):
    """Returns the element of VALID_WORDS that has the smallest difference
    from USER_WORD. Instead returns USER_WORD if that difference is greater
    than or equal to LIMIT.
    """
    # BEGIN PROBLEM 5
    list_diff = []
    list_words = []
    for i in range(0, len(valid_words)):
        list_diff.append(diff_function(user_word, valid_words[i], limit))
    for k in range(0, len(valid_words)):
        if diff_function(user_word, valid_words[k], limit) == min(tuple(list_diff)):
            list_words.append(valid_words[k])
    if min(tuple(list_diff)) >= limit:
        return user_word
    elif user_word in valid_words:
        return user_word
    else:
        return list_words[0]
    # END PROBLEM 5



def edit_diff(start, goal, limit):
    """A diff function that computes the edit distance from START to GOAL."""
    list_start = list(start)
    list_goal = list(goal)
    def count_changes(lst_start, lst_goal, total):
        if lst_start[0] == lst_goal[0]:
            return count_changes(lst_start[1: ], lst_goal[1: ], total)
        else:
            if lst_start[0] != lst_goal[0]:
                total += 1
                if total > limit:
                    return total
                return count_changes(lst_start[1: ], lst_goal[1: ], total)
            else:
                return count_changes(lst_start[1: ], lst_goal[1: ], total)
    return count_changes(list_start, list_goal, 0)



def minDistance(word1, word2):
    if not word1:
        return len(word2 or '') or 0
    if not word2:
        return len(word1 or '') or 0
    size1 = len(word1)
    size2 = len(word2)
    last = 0
    tmp = range(size2 + 1)
    value = None
    for i in range(size1):
        tmp[0] = i + 1
        last = i
        # print word1[i], last, tmp
        for j in range(size2):
            if word1[i] == word2[j]:
                value = last
            else:
                value = 1 + min(last, tmp[j], tmp[j + 1])
                # print(last, tmp[j], tmp[j + 1], value)
            last = tmp[j+1]
            tmp[j+1] = value
        # print tmp
    return value

def levenshtein_distance(first,second):
    if len(first) == 0 or len(second) == 0:
        return len(first) + len(second)
    first_length = len(first) + 1
    second_length = len(second) + 1
    distance_matrix = [range(second_length) for i in range(first_length)]
    for i in range(1, first_length):
        for j in range(1, second_length):
            deletion = distance_matrix[i-1][j] + 1
            insertion = distance_matrix[i][j-1] + 1
            substitution = distance_matrix[i-1][j-1]
            if first[i-1] != second[j-1]:
                substitution += 1
            distance_matrix[i][j] = min(insertion, deletion, substitution)
    return distance_matrix[first_length-1][second_length-1]


start_length = 5
goal_length = 5
goal_lane = [0 for i in range(goal_length)]
edit_matrix = [goal_lane for i in range(start_length)]
edit_matrix[0] = [i for i in range(goal_length)]
for i in range(0, start_length):
    edit_matrix[i][0] = i

print (edit_matrix)