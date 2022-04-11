def assert_equals(user_answer, correct_answer):
    if not (str(user_answer) == str(correct_answer)):
        print(str(user_answer) + " should be equal " + str(correct_answer))
    else:
        print('Success: ' + str(user_answer))
