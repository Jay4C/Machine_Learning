import json
import time
import unittest
from datetime import datetime, timedelta
import footballPrediction


class UnitTestsSupervisedLearningFootball(unittest.TestCase):
    # ok
    def test_football_prediction_uefa_champions_league(self):
        print('test_football_prediction_uefa_champions_league')

        try:
            today = datetime.now().strftime('%Y-%m-%d')

            today_more_days = (datetime.now() + timedelta(days=10)).strftime('%Y-%m-%d')

            resultat_matchs = footballPrediction.prediction_matchs("2001", today, today_more_days)

            print(json.dumps(resultat_matchs))
        except Exception as e:
            print("error : " + str(e))

    # ok
    def test_football_prediction_portugal_primeira_liga(self):
        print('test_football_prediction_portugal_primeira_liga')

        try:
            today = datetime.now().strftime('%Y-%m-%d')

            today_more_days = (datetime.now() + timedelta(days=10)).strftime('%Y-%m-%d')

            resultat_matchs = footballPrediction.prediction_matchs("2017", today, today_more_days)

            print(json.dumps(resultat_matchs))
        except Exception as e:
            print('error : ' + str(e))

    # ok
    def test_football_prediction_england_premier_league(self):
        print('test_football_prediction_england_premier_league')

        try:
            today = datetime.now().strftime('%Y-%m-%d')

            today_more_days = (datetime.now() + timedelta(days=10)).strftime('%Y-%m-%d')

            resultat_matchs = footballPrediction.prediction_matchs("2021", today, today_more_days)

            print(json.dumps(resultat_matchs))
        except Exception as e:
            print('error : ' + str(e))

    # ok
    def test_football_prediction_france_ligue_1(self):
        print('test_football_prediction_france_ligue_1')

        try:
            today = datetime.now().strftime('%Y-%m-%d')

            today_more_days = (datetime.now() + timedelta(days=10)).strftime('%Y-%m-%d')

            resultat_matchs = footballPrediction.prediction_matchs("2015", today, today_more_days)

            print(json.dumps(resultat_matchs))
        except Exception as e:
            print('error : ' + str(e))

    # ok
    def test_football_prediction_the_netherlands_eredivisie(self):
        print('test_football_prediction_the_netherlands_eredivisie')

        try:
            today = datetime.now().strftime('%Y-%m-%d')

            today_more_days = (datetime.now() + timedelta(days=10)).strftime('%Y-%m-%d')

            resultat_matchs = footballPrediction.prediction_matchs("2003", today, today_more_days)

            print(json.dumps(resultat_matchs))
        except Exception as e:
            print("error : " + str(e))

    # ok
    def test_football_prediction_germany_bundesliga(self):
        print("test_football_prediction_germany_bundesliga")

        try:
            today = datetime.now().strftime('%Y-%m-%d')

            today_more_days = (datetime.now() + timedelta(days=10)).strftime('%Y-%m-%d')

            resultat_matchs = footballPrediction.prediction_matchs("2002", today, today_more_days)

            print(json.dumps(resultat_matchs))
        except Exception as e:
            print("error : " + str(e))

    # ok
    def test_football_prediction_serie_a_brazil(self):
        print('test_football_prediction_serie_a_brazil')

        try:
            today = datetime.now().strftime('%Y-%m-%d')

            today_more_days = (datetime.now() + timedelta(days=10)).strftime('%Y-%m-%d')

            resultat_matchs = footballPrediction.prediction_matchs("2013", today, today_more_days)

            print(json.dumps(resultat_matchs))
        except Exception as e:
            print("error : " + str(e))

    # ok
    def test_football_prediction_spain_primera_division(self):
        print('test_football_prediction_spain_primera_division')

        try:
            today = datetime.now().strftime('%Y-%m-%d')

            today_more_days = (datetime.now() + timedelta(days=10)).strftime('%Y-%m-%d')

            resultat_matchs = footballPrediction.prediction_matchs("2014", today, today_more_days)

            print(json.dumps(resultat_matchs))
        except Exception as e:
            print('error : ' + str(e))

    # ok
    def test_football_prediction_england_championship(self):
        print('test_football_prediction_england_championship')

        try:
            today = datetime.now().strftime('%Y-%m-%d')

            today_more_days = (datetime.now() + timedelta(days=10)).strftime('%Y-%m-%d')

            resultat_matchs = footballPrediction.prediction_matchs("2016", today, today_more_days)

            print(json.dumps(resultat_matchs))
        except Exception as e:
            print("error : " + str(e))

    # ok
    def test_football_prediction_serie_a_italy(self):
        print('test_football_prediction_serie_a_italy')

        try:
            today = datetime.now().strftime('%Y-%m-%d')

            today_more_days = (datetime.now() + timedelta(days=10)).strftime('%Y-%m-%d')

            resultat_matchs = footballPrediction.prediction_matchs("2019", today, today_more_days)

            print(json.dumps(resultat_matchs))
        except Exception as e:
            print('error : ' + str(e))

    # ok
    def test_football_prediction_world_cup(self):
        print("test_football_prediction_world_cup")

        try:
            today = datetime.now().strftime('%Y-%m-%d')

            today_more_days = (datetime.now() + timedelta(days=10)).strftime('%Y-%m-%d')

            resultat_matchs = footballPrediction.prediction_matchs("2000", today, today_more_days)

            print(json.dumps(resultat_matchs))
        except Exception as e:
            print("error : " + str(e))

    # ok
    def test_football_prediction_european_championship(self):
        print("test_football_prediction_european_championship")

        try:
            today = datetime.now().strftime('%Y-%m-%d')

            today_more_days = (datetime.now() + timedelta(days=10)).strftime('%Y-%m-%d')

            resultat_matchs = footballPrediction.prediction_matchs("2018", today, today_more_days)

            print(json.dumps(resultat_matchs))
        except Exception as e:
            print("error : " + str(e))

    # ok
    def test_football_prediction_european_all_competitions_v1(self):
        print('test_football_prediction_european_all_competitions_v1')

        try:
            today = datetime.now().strftime('%Y-%m-%d')

            today_more_days = (datetime.now() + timedelta(days=10)).strftime('%Y-%m-%d')

            resultat_matchs = []

            # ligue_1
            resultat_matchs_ligue_1 = footballPrediction.prediction_matchs("2015", today, today_more_days)
            for resultat in resultat_matchs_ligue_1:
                resultat_matchs.append(resultat)

            # premier_league
            resultat_matchs_premier_league = footballPrediction.prediction_matchs("2021", today, today_more_days)
            for resultat in resultat_matchs_premier_league:
                resultat_matchs.append(resultat)

            # bundesliga
            resultat_matchs_bundesliga = footballPrediction.prediction_matchs("2002", today, today_more_days)
            for resultat in resultat_matchs_bundesliga:
                resultat_matchs.append(resultat)

            # serie_a_italy
            resultat_matchs_serie_a_italy = footballPrediction.prediction_matchs("2019", today, today_more_days)
            for resultat in resultat_matchs_serie_a_italy:
                resultat_matchs.append(resultat)

            # la_liga
            resultat_matchs_la_liga = footballPrediction.prediction_matchs("2014", today, today_more_days)
            for resultat in resultat_matchs_la_liga:
                resultat_matchs.append(resultat)

            # uefa_champions_league
            resultat_matchs_uefa_champions_league = footballPrediction.prediction_matchs("2001", today,
                                                                                         today_more_days)
            for resultat in resultat_matchs_uefa_champions_league:
                resultat_matchs.append(resultat)

            # primeira_liga
            resultat_matchs_primeira_liga = footballPrediction.prediction_matchs("2017", today, today_more_days)
            for resultat in resultat_matchs_primeira_liga:
                resultat_matchs.append(resultat)

            # eredivisie
            resultat_matchs_eredivisie = footballPrediction.prediction_matchs("2003", today, today_more_days)
            for resultat in resultat_matchs_eredivisie:
                resultat_matchs.append(resultat)

            # serie_a_brazil
            resultat_matchs_serie_a_brazil = footballPrediction.prediction_matchs("2013", today, today_more_days)
            for resultat in resultat_matchs_serie_a_brazil:
                resultat_matchs.append(resultat)

            # championship
            resultat_matchs_championship = footballPrediction.prediction_matchs("2016", today, today_more_days)
            for resultat in resultat_matchs_championship:
                resultat_matchs.append(resultat)

            # world_cup
            resultat_matchs_world_cup = footballPrediction.prediction_matchs("2000", today, today_more_days)
            for resultat in resultat_matchs_world_cup:
                resultat_matchs.append(resultat)

            # european_championship
            resultat_matchs_european_championship = footballPrediction.prediction_matchs("2018", today,
                                                                                         today_more_days)
            for resultat in resultat_matchs_european_championship:
                resultat_matchs.append(resultat)

            print(json.dumps(resultat_matchs))
        except Exception as e:
            print('error : ' + str(e))

    # ok
    def test_football_prediction_european_all_competitions_v2(self):
        print('test_football_prediction_european_all_competitions_v2')

        today = datetime.now().strftime('%Y-%m-%d')

        today_more_days = (datetime.now() + timedelta(days=10)).strftime('%Y-%m-%d')

        resultat_matchs = []

        try:
            # european_championship
            print('# european_championship')
            resultat_matchs_european_championship = footballPrediction.prediction_matchs("2018", today, today_more_days)
            for resultat in resultat_matchs_european_championship:
                resultat_matchs.append(resultat)
            time.sleep(10)
        except Exception as e:
            print('error # european_championship : ' + str(e))

        try:
            # uefa_champions_league
            print('# uefa_champions_league')
            resultat_matchs_uefa_champions_league = footballPrediction.prediction_matchs("2001", today, today_more_days)
            for resultat in resultat_matchs_uefa_champions_league:
                resultat_matchs.append(resultat)
            time.sleep(10)
        except Exception as e:
            print("error # uefa_champions_league : " + str(e))

        try:
            # england / premier_league
            print('# england / premier_league')
            resultat_matchs_premier_league = footballPrediction.prediction_matchs("2021", today, today_more_days)
            for resultat in resultat_matchs_premier_league:
                resultat_matchs.append(resultat)
            time.sleep(10)
        except Exception as e:
            print('error # england / premier_league : ' + str(e))

        try:
            # france / ligue_1
            print('# france / ligue_1')
            resultat_matchs_ligue_1 = footballPrediction.prediction_matchs("2015", today, today_more_days)
            for resultat in resultat_matchs_ligue_1:
                resultat_matchs.append(resultat)
            time.sleep(10)
        except Exception as e:
            print('error # france / ligue_1 : ' + str(e))

        try:
            # italy / serie_a
            print('# italy / serie_a')
            resultat_matchs_serie_a_italy = footballPrediction.prediction_matchs("2019", today, today_more_days)
            for resultat in resultat_matchs_serie_a_italy:
                resultat_matchs.append(resultat)
            time.sleep(10)
        except Exception as e:
            print('error # italy / serie_a : ' + str(e))

        try:
            # spain / primera_division
            print('# spain / primera_division')
            resultat_matchs_la_liga = footballPrediction.prediction_matchs("2014", today, today_more_days)
            for resultat in resultat_matchs_la_liga:
                resultat_matchs.append(resultat)
            time.sleep(10)
        except Exception as e:
            print('error # spain / primera_division : ' + str(e))

        try:
            # england / championship
            print('# england / championship')
            resultat_matchs_championship = footballPrediction.prediction_matchs("2016", today, today_more_days)
            for resultat in resultat_matchs_championship:
                resultat_matchs.append(resultat)
            time.sleep(10)
        except Exception as e:
            print('error # england / championship : ' + str(e))

        print(json.dumps(resultat_matchs))

    # ok
    def test_football_prediction_european_all_competitions_v3(self):
        print('test_football_prediction_european_all_competitions_v3')

        try:
            today = datetime.now().strftime('%Y-%m-%d')

            today_more_days = (datetime.now() + timedelta(days=10)).strftime('%Y-%m-%d')

            resultat_matchs = []

            # ligue_1
            print('# ligue_1')
            resultat_matchs_ligue_1 = footballPrediction.prediction_matchs("2015", today, today_more_days)
            for resultat in resultat_matchs_ligue_1:
                resultat_matchs.append(resultat)

            # premier_league
            print('# premier_league')
            resultat_matchs_premier_league = footballPrediction.prediction_matchs("2021", today, today_more_days)
            for resultat in resultat_matchs_premier_league:
                resultat_matchs.append(resultat)

            # bundesliga
            print("# bundesliga")
            resultat_matchs_bundesliga = footballPrediction.prediction_matchs("2002", today, today_more_days)
            for resultat in resultat_matchs_bundesliga:
                resultat_matchs.append(resultat)

            # serie_a_italy
            print('# serie_a_italy')
            resultat_matchs_serie_a_italy = footballPrediction.prediction_matchs("2019", today, today_more_days)
            for resultat in resultat_matchs_serie_a_italy:
                resultat_matchs.append(resultat)

            # la_liga
            print("# la_liga")
            resultat_matchs_la_liga = footballPrediction.prediction_matchs("2014", today, today_more_days)
            for resultat in resultat_matchs_la_liga:
                resultat_matchs.append(resultat)

            # primeira_liga
            print('# primeira_liga')
            resultat_matchs_primeira_liga = footballPrediction.prediction_matchs("2017", today, today_more_days)
            for resultat in resultat_matchs_primeira_liga:
                resultat_matchs.append(resultat)

            # eredivisie
            print("# eredivisie")
            resultat_matchs_eredivisie = footballPrediction.prediction_matchs("2003", today, today_more_days)
            for resultat in resultat_matchs_eredivisie:
                resultat_matchs.append(resultat)

            # championship
            print('# championship')
            resultat_matchs_championship = footballPrediction.prediction_matchs("2016", today, today_more_days)
            for resultat in resultat_matchs_championship:
                resultat_matchs.append(resultat)

            # european_championship
            print('# european_championship')
            resultat_matchs_european_championship = footballPrediction.prediction_matchs("2018", today, today_more_days)
            for resultat in resultat_matchs_european_championship:
                resultat_matchs.append(resultat)

            # uefa_champions_league
            print('# uefa_champions_league')
            resultat_matchs_uefa_champions_league = footballPrediction.prediction_matchs("2001", today, today_more_days)
            for resultat in resultat_matchs_uefa_champions_league:
                resultat_matchs.append(resultat)

            print(json.dumps(resultat_matchs))
        except Exception as e:
            print('error : ' + str(e))


if __name__ == '__main__':
    unittest.main()
