import goalkeepers as gk
import defenders as df
import midfielders as md
import forwards as fw
import team_database as tdb


### Provide the name of your team and formation below: ###
formation = [4, 2, 3, 1]
team = tdb.germany
### -------------------------------------------------- ###


gks = team['available_goalkeepers_list']
dfs = team['available_defenders_list']
mdfs = team['available_midfielders_list']
fws = team['available_forwards_list']


def match_day_team(gks, dfs, mdfs, fws, formation):
    dfs_number = formation[0]
    mdfs_number = formation[1]
    fws_number = formation[-1]

    line_up_length = dfs_number+mdfs_number+fws_number + 1

    while line_up_length <= 11:

        if line_up_length == 11:

            gkk = gk.choose_goalkeeper(gks)
            dfs = df.choose_defenders(dfs, dfs_number)
            mdfs = md.choose_midfielder(mdfs, mdfs_number)
            fws = fw.choose_forwards(fws, fws_number)
            print(gkk+dfs+mdfs+fws)
            break

        else:
            length_of_formation = len(formation)
            if length_of_formation == 4:
                mdfs_number += formation[2]
                line_up_length += formation[2]
            elif length_of_formation == 5:
                mdfs_number = int(formation[1]) + \
                    int(formation[2]) + int(formation[3])
                line_up_length = int(formation[2]) + int(formation[3])


match_day_team(gks, dfs,
               mdfs, fws, formation)
