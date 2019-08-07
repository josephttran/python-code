class Player:
    def __init__(self):
        self.__score = 0

    @property
    def score(self):
        return self.__score

    @score.setter
    def score(self, score):
        self.__score = score


class QuestionAnswer:
    def __init__(self, question, possible_answer_list, correct_answer):
        self._question = question
        self._possible_answer_list = possible_answer_list
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
        self.__question_answer_list = [
            QuestionAnswer(
                'What is a noun?',
                ['person', 'place', 'thing', 'all the above'],
                'all the above'
            ),
            QuestionAnswer(
                'What are the three states of matter?',
                ['1, 2, 3', 'solid, liquid, gas', 'water, ice, air', 'none'],
                'solid, liquid, gas'
            ),
            QuestionAnswer(
                'What is an ostrich?',
                ['place', 'stream', 'bird', 'ostrich not real'],
                'bird'
            ),
            QuestionAnswer(
                'Which is a not framework?',
                ['Flutter', 'Flux', 'Rocket', 'Laravel'],
                'Flux'
            ),
        ]

    def get_question_answer_list(self):
        return self.__question_answer_list


def is_user_answer_valid(possible_answer_list, user_answer):
    for i in range(len(possible_answer_list)):
        if user_answer == possible_answer_list[i]:
            return True

    return False


def print_game_result(player_one, player_two):
    print('\n## Game Over ##')
    print('Player 1 score: ', player_one.score)
    print('Player 2 score: ', player_two.score)

    if player_one.score > player_two.score:
        print('Player 1 Win')
    elif player_one.score < player_two.score:
        print('Player 2 Win')
    else:
        print("This game end in a draw")


def run_game(question_answer_list, player_one, player_two):
    for i in range(len(question_answer_list)):
        if i % 2 == 0:
            print('\n## Player 1 turn ##', end='\n\n')
        else:
            print('\n## Player 2 turn ##', end='\n\n')

        # Display question to console
        print(question_answer_list[i]._question)

        # Display all possible answers to console
        print(*question_answer_list[i]._possible_answer_list, sep='\n', end='\n\n')

        # Store player answer
        player_answer = input('Enter your answer: ')

        # Validate user input,
        # while player's input is not valid
        # display question and possible answers
        while not is_user_answer_valid(
                question_answer_list[i]._possible_answer_list,
                player_answer):
            print('Your answer does not match available possible_answer! try again.\n')
            print(question_answer_list[i]._question)
            print(*question_answer_list[i]._possible_answer_list, sep='\n', end='\n\n')
            player_answer = input('Enter your answer: ')

        # Check if player's answer is correct and increment if it is
        if player_answer != question_answer_list[i]._correct_answer:
            print('Incorrect! The correct answer is ', question_answer_list[i]._correct_answer)
        else:
            print('Correct!')
            if i % 2 == 0:
                player_one.score += 1
            else:
                player_two.score += 1


def main():
    player_one = Player()
    player_two = Player()
    trivia = Trivia()
    trivia.create_question_answer()
    question_answer_list = trivia.get_question_answer_list()

    run_game(question_answer_list, player_one, player_two)
    print_game_result(player_one, player_two)


main()
