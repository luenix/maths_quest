# maths_quest.py
# Text based adventure game for learning maths
# Requires python 3.8 (for the f strings)

import numpy as np
import time


class Stage:
    '''
    Object that produces 5 questions of 1 operator (1 level of a dungeon)
    :param op: operator of the questions. ('+', '-', '*', '/')
    :type op: str
    :param level: difficulty of the questions, decides ranges of x1 and x2 (1-5)
    :type level: int
    '''

    def __init__(self, op, level):
        self.op = op
        self.level = level
        self.solved = False
        if self.level > 5:  # Can't have questions that are higher then level 5
            print('You have completed this dungeon. Move on to the next area!')
        else:
            self.questions = self.make_questions()

    def make_questions(self):
        '''
        Makes the 5 questions of this stage
        '''
        qs = []
        for i in range(5):
            q = Question(self.op, self.level)
            qs.append(q)

        return (qs)

    def run_stage(self):
        '''
        Play this stage and the questions
        '''

        # Introduction
        print(f'\n\nYou have entered the dungeon of {self.op}, on level {self.level}.')

        # Check if this dungeon has been cleared (can't go past level 5
        if self.level > 5:
            print('You have completed this dungeon. Move on to the next area!')
            return None

        print('Answer the following questions to delve deeper into the dungeon!\n\n')
        correct = 0

        # Loop through the questions
        for q in self.questions:

            # Get an answer from the user
            user_ans = round(float(input(f'What is {q}?')), 2)

            if user_ans != q.ans:  # if they get it wrong
                print('\nOh No! You got it wrong.')
                print(f'You answered {user_ans}, but the correct answer was {q.ans}.')
                break

            else:
                print('Correct!\n\n')
                correct += 1

        # If you answer all the questions right
        if correct == len(self.questions):
            print('Congratulations, you passed this stage!')
            self.solved = True
        else:
            print('I am sorry, it looks like you have to start the dungeon again.')


class Question:
    '''
        Object that make the questions for the stages
        :param op: operator of the question. ('+', '-', '*', '/')
        :type op: str
        :param level: difficulty of the question, decides ranges of x1 and x2 (1-5)
        :type level: int
        '''

    def __init__(self, op, level):
        self.op = op

        # range of possible x1 and x2 values
        self.x1range = x1x2ranges[self.op][level][0]
        self.x2range = x1x2ranges[self.op][level][1]

        # choose a random number in the ranges for the question
        self.x1 = np.random.randint(self.x1range[0], self.x1range[1])
        self.x2 = np.random.randint(self.x2range[0], self.x2range[1])
        self.ans = round(eval(self.__str__()), 2)

    def __str__(self):
        # example: '3 + 5'
        return f'{self.x1} {self.op} {self.x2}'


# difficult range dictionary
# example: x1x2ranges[operator (str)][level (int)] = [ (x1min, x1max) , (x2min, x2max) ]

x1x2ranges = {
    '+': {1: [(1, 10), (1, 10)],
          2: [(10, 20), (20, 30)],
          3: [(30, 50), (50, 70)],
          4: [(50, 100), (100, 150)],
          5: [(500, 999), (100, 500)]
          },
    '-': {1: [(20, 30), (10, 20)],
          2: [(50, 70), (20, 50)],
          3: [(100, 150), (10, 100)],
          4: [(100, 999), (150, 500)],
          5: [(9999, 99999), (999, 9999)]
          },
    '*': {1: [(2, 5), (1, 12)],
          2: [(6, 12), (1, 12)],
          3: [(2, 5), (12, 50)],
          4: [(6, 12), (12, 50)],
          5: [(11, 19), (15, 30)]
          },
    '/': {1: [(10, 20), (1, 10)],
          2: [(30, 70), (1, 10)],
          3: [(30, 200), (1, 10)],
          4: [(200, 800), (1, 10)],
          5: [(30, 70), (50, 100)]
          }
}

# start a timer for highscores
start_time = time.time()

# welcome message
print('Welcome to Maths Quest!')

# inital levels
add_level = 1
sub_level = 1
mul_level = 1
div_level = 1

# start loop for playing
play = True

while play:

    # break the loop if all the dungeons are complete
    if add_level > 5 and sub_level > 5 and mul_level > 5 and div_level > 5:
        play = False
        continue

    print('\n\nChoose which dungeon you wish to explore:')

    # list the dungeons and the level
    for i, q in enumerate([('+', add_level), ('-', sub_level), ('*', mul_level), ('/', div_level)]):
        if q[1] > 5:
            # Show any dungeons you have completed
            print(f'\t{i + 1}~ Dungeon of {q[0]}, COMPLETE!')
        else:
            print(f'\t{i + 1}~ Dungeon of {q[0]}, level {q[1]}')

    stage_select = input('\nType a number to choose.')

    # play the stage depending on choice of input

    if stage_select == '1':
        stage = Stage('+', add_level)
        stage.run_stage()

        if stage.solved:  # check if you finished the stage
            add_level += 1

    elif stage_select == '2':
        stage = Stage('-', sub_level)
        stage.run_stage()

        if stage.solved:
            sub_level += 1


    elif stage_select == '3':
        stage = Stage('*', mul_level)
        stage.run_stage()

        if stage.solved:
            mul_level += 1

    elif stage_select == '4':
        stage = Stage('/', div_level)
        stage.run_stage()

        if stage.solved:
            div_level += 1

    # Catch the incorrect inputs
    else:
        print('I Don\'t understand that input.')

# stop the time and print how long it took
end_time = time.time() - start_time

print('You finished the game!')
print(f'Completed in {end_time / 60} minutes')
