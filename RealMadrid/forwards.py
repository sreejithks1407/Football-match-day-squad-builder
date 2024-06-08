import random

available_forwards_list = ['Kylian Mbappe',
                           'Rodrygo', 'Vinicius Junior', 'Endrick', 'Joselu', 'Brahim Diaz']


def choose_forwards(available_forwards):

    available_forwards_number = len(available_forwards)
    selected_numbers = []

    total_forwards_needed = int(input(
        "Provide the number of midfielders needed in your squad for today's match \n"))

    while (total_forwards_needed > available_forwards_number):
        total_forwards_needed = int(input(
            f'Total forwards available for selection is {available_forwards_number} which less than your requirement. So please select a number which is less than or equal to this.'))

    total_forwards_choosen = 0

    while total_forwards_choosen < total_forwards_needed:

        random_palyer_number = random.randint(0, 4)
        if random_palyer_number not in selected_numbers:
            selected_numbers.append(random_palyer_number)
            total_forwards_choosen += 1

    my_forwards_combinations_for_todays_game = [
        available_forwards[player_number] for player_number in selected_numbers]

    return my_forwards_combinations_for_todays_game


forwards_for_match_day = choose_forwards(available_forwards_list)
print(forwards_for_match_day)
