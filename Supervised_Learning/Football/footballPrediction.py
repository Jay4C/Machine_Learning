from datetime import date, timedelta
import time
import wwwFootballDataOrg

# Global variables
score_team_1 = 0
score_team_2 = 0
# Global variables


# Méthodes de comparaisons des équipes

# attribuer un point à l'équipe qui a le plus de victoires durant leur classement.
def more_matchs_won(team_1, team_2):
    try:
        global score_team_1
        global score_team_2

        if team_1 > team_2:
            score_team_1 += 1

        elif team_1 == team_2:
            score_team_1 += 1
            score_team_2 += 1

        else:
            score_team_2 += 1
    except Exception as e:
        print('error more_matchs_won : ' + str(e))


# attribuer un point à l'équipe qui est mieux positionné dans le classement.
def best_position(team_1, team_2):
    try:
        global score_team_1
        global score_team_2

        if team_1 < team_2:
            score_team_1 += 1

        elif team_1 == team_2:
            score_team_1 += 1
            score_team_2 += 1

        else:
            score_team_2 += 1
    except Exception as e:
        print('error best_position : ' + str(e))


# attribuer un point pour l'équipe qui a le moins de matchs perdus.
def less_matchs_lost(team_1, team_2):
    try:
        global score_team_1
        global score_team_2

        if team_1 > team_2:
            score_team_2 += 1

        elif team_1 == team_2:
            score_team_1 += 1
            score_team_2 += 1

        else:
            score_team_1 += 1
    except Exception as e:
        print("error less_matchs_lost : " + str(e))


# attribuer un point à l'équipe qui a le moins de matchs nuls.
def less_matchs_draw(team_1, team_2):
    try:
        global score_team_1
        global score_team_2

        if team_1 > team_2:
            score_team_2 += 1

        elif team_1 == team_2:
            score_team_1 += 1
            score_team_2 += 1

        else:
            score_team_1 += 1
    except Exception as e:
        print('error less_matchs_draw : ' + str(e))


# attribuer un point à l'équipe qui a le plus de buts marqués.
def more_goal_for(team_1, team_2):
    try:
        global score_team_1
        global score_team_2

        if team_1 > team_2:
            score_team_1 += 1

        elif team_1 == team_2:
            score_team_1 += 1
            score_team_2 += 1

        else:
            score_team_2 += 1
    except Exception as e:
        print('error more_goal_for : ' + str(e))


# attribuer un point à l'équipe qui a le moins de buts encaissés dans leur classement en cours.
def less_goal_against(team_1, team_2):
    try:
        global score_team_1
        global score_team_2

        if team_1 > team_2:
            score_team_2 += 1

        elif team_1 == team_2:
            score_team_1 += 1
            score_team_2 += 1

        else:
            score_team_1 += 1
    except Exception as e:
        print('error less_goal_against : ' + str(e))


# attribuer un point à l'équipe qui a le plus de points.
def more_points(team_1, team_2):
    try:
        global score_team_1
        global score_team_2

        if team_1 > team_2:
            score_team_1 += 1

        elif team_1 < team_2:
            score_team_2 += 1

        else:
            score_team_1 += 1
            score_team_2 += 1
    except Exception as e:
        print('error more_points : ' + str(e))


# attribuer un point à l'équipe qui a le plus de buts de différence.
def more_goal_difference(team_1, team_2):
    try:
        global score_team_1
        global score_team_2

        if team_1 > team_2:
            score_team_1 += 1

        elif team_1 < team_2:
            score_team_2 += 1

        else:
            score_team_1 += 1
            score_team_2 += 1
    except Exception as e:
        print('error more_goal_difference : ' + str(e))


# attribuer un point à l'équipe qui a joué le plus de matchs.
def more_played_games(team_1, team_2):
    try:
        global score_team_1
        global score_team_2

        if team_1 > team_2:
            score_team_1 += 1

        elif team_1 < team_2:
            score_team_2 += 1

        else:
            score_team_1 += 1
            score_team_2 += 1
    except Exception as e:
        print("error more_played_games : " + str(e))


# attribuer un point à l'équipe qui a gagné le plus de matchs lors des dernières rencontres.
def results_last_matchs_in_same_standing_full_time(team_1, team_2, idCompetition, dateFrom, dateTo, status):
    global score_team_1
    global score_team_2

    try:
        json_response = wwwFootballDataOrg.v2_competition_id_matches_filters(
            idCompetition,
            dateFrom,
            dateTo,
            status
        )

        matchs = json_response['matches']

        for match in matchs:
            if team_1 == match['homeTeam']['name'] and team_2 == match['awayTeam']['name']:
                if match['score']['fullTime']['homeTeam'] > match['score']['fullTime']['awayTeam']:
                    score_team_1 += 1
                elif match['score']['fullTime']['homeTeam'] == match['score']['fullTime']['awayTeam']:
                    score_team_1 += 1
                    score_team_2 += 1
                else:
                    score_team_2 += 1
            elif team_1 == match['awayTeam']['name'] and team_2 == match['homeTeam']['name']:
                if match['score']['fullTime']['homeTeam'] > match['score']['fullTime']['awayTeam']:
                    score_team_2 += 1
                elif match['score']['fullTime']['homeTeam'] == match['score']['fullTime']['awayTeam']:
                    score_team_1 += 1
                    score_team_2 += 1
                else:
                    score_team_1 += 1
    except Exception as e:
        print("error results_last_matchs_in_same_standing_full_time : " + str(e))


# attribuer un point à l'équipe qui a gagné le plus de matchs lors des dernières rencontres durant la première
# période du match (halfTime)
def results_last_matchs_in_same_standing_half_time(team_1, team_2, idCompetition, dateFrom, dateTo, status):
    global score_team_1
    global score_team_2

    try:
        json_response = wwwFootballDataOrg.v2_competition_id_matches_filters(idCompetition, dateFrom, dateTo, status)

        matchs = json_response['matches']

        for match in matchs:
            if team_1 == match['homeTeam']['name'] and team_2 == match['awayTeam']['name']:
                if match['score']['halfTime']['homeTeam'] > match['score']['halfTime']['awayTeam']:
                    score_team_1 += 1
                elif match['score']['halfTime']['homeTeam'] == match['score']['halfTime']['awayTeam']:
                    score_team_1 += 1
                    score_team_2 += 1
                else:
                    score_team_2 += 1
            elif team_1 == match['awayTeam']['name'] and team_2 == match['homeTeam']['name']:
                if match['score']['halfTime']['homeTeam'] > match['score']['halfTime']['awayTeam']:
                    score_team_2 += 1
                elif match['score']['halfTime']['homeTeam'] == match['score']['halfTime']['awayTeam']:
                    score_team_1 += 1
                    score_team_2 += 1
                else:
                    score_team_1 += 1
    except Exception as e:
        print('error results_last_matchs_in_same_standing_half_time : ' + str(e))


# retourner le resultat du match.
def resultat_match(score_team1, score_team2, team1, team2):
    try:
        if score_team1 > score_team2:
            resultat = {
                "equipe_1": team1,
                "equipe_2": team2,
                "vainqueur": team1
            }
            return resultat
        elif score_team_1 == score_team_2:
            resultat = {
                "equipe_1": team1,
                "equipe_2": team2,
                "vainqueur": "match nul"
            }
            return resultat
        else:
            resultat = {
                "equipe_1": team1,
                "equipe_2": team2,
                "vainqueur": team2
            }
            return resultat
    except Exception as e:
        print("error resultat_match : " + str(e))


# appliquer des comparaisons des équipes par rapport au classement.
def methode_comparaison_equipes_classement(team_1, team_2, position_of_teams):
    try:
        # vérifier les équipes avant de démarrer les calculs.
        for position_of_team in position_of_teams:
            if team_1 == position_of_team['team']['id']:
                team_1 = position_of_team
            elif team_2 == position_of_team['team']['id']:
                team_2 = position_of_team

        # position
        best_position(team_1['position'], team_2['position'])

        # more_matchs_won
        more_matchs_won(team_1['won'], team_2['won'])

        # less_matchs_draw
        less_matchs_draw(team_1['draw'], team_2['draw'])

        # less_matchs_lost
        less_matchs_lost(team_1['lost'], team_2['lost'])

        # more_points
        more_points(team_1['points'], team_2['points'])

        # more_goal_for
        more_goal_for(team_1['goalsFor'], team_2['goalsFor'])

        # less_goal_against
        less_goal_against(team_1['goalsAgainst'], team_2['goalsAgainst'])

        # more_goal_difference
        more_goal_difference(team_1['goalDifference'], team_2['goalDifference'])

        # more_played_games
        more_played_games(team_1['playedGames'], team_2['playedGames'])
    except Exception as e:
        print('error methode_comparaison_equipes_classement : ' + str(e))

# Méthodes de comparaisons des équipes


# prédire les matchs à venir.
def prediction_matchs(idCompetition, dateFrom, dateTo):
    try:
        global score_team_1
        global score_team_2

        resultat_matchs = []

        classements = []

        json_response_v2_competitions_id_standings = wwwFootballDataOrg.v2_competitions_id_standings(idCompetition)

        time.sleep(25)

        standings = json_response_v2_competitions_id_standings['standings']

        for standing in standings:
            classements.append(standing)

        rencontres = []

        rencontres_ligue = wwwFootballDataOrg.v2_competition_id_matches_filters(
            idCompetition,
            dateFrom,
            dateTo,
            'SCHEDULED'
        )

        time.sleep(25)

        for rencontre_ligue in rencontres_ligue['matches']:
            rencontres.append(rencontre_ligue)

        for rencontre in rencontres:
            a = rencontre['homeTeam']['id']
            b = rencontre['awayTeam']['id']

            today = dateFrom

            past = (date.today() - timedelta(days=730)).strftime('%Y-%m-%d')

            results_last_matchs_in_same_standing_full_time(
                a,
                b,
                idCompetition,
                past,
                today,
                'FINISHED'
            )

            time.sleep(25)

            results_last_matchs_in_same_standing_half_time(
                a,
                b,
                idCompetition,
                past,
                today,
                'FINISHED'
            )

            time.sleep(25)

            try:
                # TOTAL
                methode_comparaison_equipes_classement(a, b, classements[0]['table'])
            except Exception as e:
                print('error prediction_matchs methode_comparaison_equipes_classement TOTAL : ' + str(e))

            try:
                resultat_match_to_be_added = resultat_match(
                    score_team_1,
                    score_team_2,
                    rencontre['homeTeam']['name'],
                    rencontre['awayTeam']['name']
                )
                resultat_matchs.append(resultat_match_to_be_added)
                print("resultat_match : " + str(resultat_match_to_be_added))
            except Exception as e:
                print('error resultat_matchs.append : ' + str(e))

            score_team_1 = 0
            score_team_2 = 0

        return resultat_matchs
    except Exception as e:
        print('error prediction_matchs : ' + str(e))
