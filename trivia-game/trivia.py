class QuestionAnswer:
    def __init__(self, question, choice_list, correct_answer):
        self._question = question
        self._choice_list = choice_list
        self._correct_answer = correct_answer


class Trivia:
    def __init__(self):
        self._question = 'Is this default question?'
        self._answer_1 = 'maybe'
        self._answer_2 = 'yes'
        self._answer_3 = 'no'
        self._answer_4 = 'do not know'
        self._correct_answer = 'yes'

    def create_question_answer(self):
        question_answer_list = [
            QuestionAnswer('What is a noun?', 
                ['person', 'place', 'thing', 'all the above'], 
                'all the above'
            ),
            QuestionAnswer('What are the three states of matter?', 
                ['1, 2, 3', 'solid, liquid, gas', 'water, ice, air', 'none'], 
                'solid, liquid, gas'
            ),
            QuestionAnswer('What is an ostrich?', 
                ['place', 'stream', 'bird', 'ostrich not real'], 
                'bird'
            ),
            QuestionAnswer('Which is a not framework?', ['Flutter', 'Flux', 'Rocket', 'Laravel'], 'Flux'),
        ]

        return question_answer_list


def is_user_answer_valid(choice_list, user_answer):
    for choice_num in range(len(choice_list)):
        if user_answer == choice_list[choice_num]:
            return True

    return False


def main():
    player_1_score = 0
    player_2_score = 0
    trivia = Trivia()
    qaList = trivia.create_question_answer()

    for i in range(len(qaList)):
        if i % 2 == 0:
            print('\n## Player 1 turn ##', end='\n\n')
        else:
            print('\n## Player 2 turn ##', end='\n\n')

        # Display question to console
        print(qaList[i]._question)

        # Display all choice to console
        print(*qaList[i]._choice_list, sep='\n', end='\n\n')

        # Store player answer
        player_answer = input('Enter your answer: ')

        # Validate user input, display question and choice again while player's answer not valid
        while not is_user_answer_valid(qaList[i]._choice_list, player_answer):
            print('Your answer does not match available choice! try again.\n')
            print(qaList[i]._question)
            print(*qaList[i]._choice_list, sep='\n', end='\n\n')
            player_answer = input('Enter your answer: ')

        # Check if player's answer is correct and increment if it is
        if player_answer != qaList[i]._correct_answer:
            print('Incorrect! The correct answer is ', qaList[i]._correct_answer)
        else:
            print('Correct!')
            if i % 2 == 0:
                player_1_score += 1
            else:
                player_2_score += 1

    print('\n## Game Over ##')
    print('Player 1 score: ', player_1_score)
    print('Player 2 score: ', player_2_score)

    if player_1_score > player_2_score:
        print('Player 1 Win')
    elif player_1_score < player_2_score:
        print('Player 2 Win')
    else:
        print("This game end in a draw")


main()
