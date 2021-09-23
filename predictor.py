import random
random_str = str()
balance = 1000

def random_string():
    print('Please give AI some data to learn...')
    print('The current data length is 0, 100 symbols left')
    global random_str
    random_str = str()
    filtr_input_string = str()
    while len(random_str) < 100:
        print('Print a random string containing 0 or 1: ')
        print()
        input_string = input()
        for item in input_string:
            if item == '0' or item == '1':
                filtr_input_string = filtr_input_string + item
        random_str = random_str + filtr_input_string
        if 100 - len(random_str) > 0:
            print(f'The current data length is {len(random_str)}, {100 - len(random_str)} symbols left')
        else:
            pass
    print()
    print(f'Final data string:\n{random_str}')
    print()
    print('You have $1000. Every time the system successfully predicts your next press, you lose $1.')
    print('''Otherwise, you earn $1. Print "enough" to leave the game. Let's go!''')
    print()
def analyzing_input(random_str):
    global an_in
    an_in = {'000': [0, 0], '001': [0, 0], '010': [0, 0], '011': [0, 0], '100': [0, 0], '101': [0, 0], '110': [0, 0],
             '111': [0, 0]}


    for item in range(8):
        triad = bin(item)
        triad = str(triad[2:].zfill(3))
        index = 0
        triad_0 = 0
        triad_1 = 0
        while index != -1:
            index = random_str.find(triad, index, len(random_str) - 1)
            if index == -1:
                break
            elif random_str[index + 3] == '0':
                triad_0 += 1
            elif random_str[index + 3] == '1':
                triad_1 += 1
            index = index + 1
            an_in.update({triad: [triad_0, triad_1]})
            #an[triad] = [an_in.get(triad)[0] + triad_0, an_in.get(triad)[0] + triad_1]


def test_string():
    while True:
        global test_str
        test_str = str()
        print('Print a random string containing 0 or 1: ')
        input_str = input()
        if input_str == 'enough':
            print('Game over!')
            exit()

        for item in input_str:
            if item == '0' or item == '1':
                test_str = test_str + item

        if len(test_str) == 0:
            print('some wrong input')

        else:
            break
def input_forecast(test_str):
    guessed_right = 0
    global balance
    prediction_string = ''.join(random.choices('01', k=3))
    for i in range(3, len(test_str)):
        triad = test_str[i-3: i]
        if an_in.get(triad)[0] > an_in.get(triad)[1]:
            prediction_string = prediction_string + '0'
        elif an_in.get(triad)[0] < an_in.get(triad)[1]:
            prediction_string = prediction_string + '1'
        else:
            prediction_string = prediction_string + ''.join(random.choices('01'))
        if str(test_str[i]) == str(prediction_string[i]):
            guessed_right += 1
    balance = balance - 2 * guessed_right + len(prediction_string) - 3
            #balance -= 1
        #else:
            #balance += 1
    print('prediction: ')
    print(prediction_string)
    print()
    percent = round(guessed_right /(len(test_str) - 3) * 100, 2 )
    print(f'Computer guessed right {guessed_right} out of {len(test_str) - 3} symbols ({percent} %)')
    print(f'Your balance is now ${balance}')
    print()
random_string()
analyzing_input(random_str)
while True:
    test_string()
    input_forecast(test_str)

    analyzing_input(test_str)