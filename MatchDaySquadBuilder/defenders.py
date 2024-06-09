import random


def choose_defenders(available_defenders, total_defenders_needed):

    available_defenders_number = len(available_defenders)
    selected_numbers = []

    # total_defenders_needed = int(input(
    #     "Provide the number of defenders needed in your squad for today's match \n"))

    while (total_defenders_needed > available_defenders_number):
        total_defenders_needed = int(input(
            f'Total defenders available for selection is {available_defenders_number} which less than your requirement. So please select a number which is less than or equal to this.'))

    total_defenders_choosen = 0

    while total_defenders_choosen < total_defenders_needed:

        random_palyer_number = random.randint(0, 4)
        if random_palyer_number not in selected_numbers:
            selected_numbers.append(random_palyer_number)
            total_defenders_choosen += 1

    my_defenders_combinations_for_todays_game = [
        available_defenders[player_number] for player_number in selected_numbers]

    return my_defenders_combinations_for_todays_game


# defenders_for_match_day = choose_defenders(available_defenders_list)
# print(defenders_for_match_day)
