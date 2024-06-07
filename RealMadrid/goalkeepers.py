import random

available_goalkeepers_list = ['Thibaut Courtois', 'Kepa Arrizabalaga',
                              'Andriy Lunin']


def choose_goalkeeper(available_goalkeepers):

    goalkeeper_number = random.randint(0, 2)
    selected_goalkeeper = available_goalkeepers[goalkeeper_number]

    return selected_goalkeeper


goalkeeper_for_match_day = choose_goalkeeper(available_goalkeepers_list)
print(goalkeeper_for_match_day)
