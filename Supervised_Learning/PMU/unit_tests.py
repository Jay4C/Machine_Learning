import time
import unittest
import warnings
from datetime import date
from requests_tor import RequestsTor
from selenium import webdriver
from Machine_Learning.Supervised_Learning.PMU.pmu import PMUFinal
from selenium.webdriver.firefox.options import Options
import pymysql.cursors

# unibet race url
global_url = "https://www.unibet.fr/turf/race/14-01-2022-R3-C8-nantes-prix-narcisse.html"


class UnitTestsSupervisedLearningPMU(unittest.TestCase):
    # number of disqualified from musique from pmu : ok
    def test_scoring_the_runners_by_number_of_disqualified_with_dark_web(self):
        print("test_scoring_the_runners_by_number_of_disqualified_with_dark_web")

        reverse = False

        participant_key = 'musique'

        url_unibet_race = global_url

        today = date.today()

        d1 = today.strftime("%d%m%Y")

        reunion = url_unibet_race.replace("https://www.unibet.fr/turf/race/", "").replace(today.strftime("%d-%m-%Y") + "-", "").replace("-", "")[:2]

        course = url_unibet_race.replace("https://www.unibet.fr/turf/race/", "").replace(today.strftime("%d-%m-%Y") + "-", "").replace("-", "")[2:4]

        url = "https://offline.turfinfo.api.pmu.fr/rest/client/1/programme/" \
              + d1 + "/" \
              + reunion + "/" \
              + course + "/participants"

        headers = {
            "Accept": "application/json",
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103'
        }

        rt = RequestsTor()

        response = rt.get(url, headers=headers)

        runners = {}

        for participant in response.json()['participants']:
            num_pmu = str(participant['numPmu'])

            if participant_key in participant:
                criteria = str(participant[participant_key])

                number_of_disqualified = criteria.count("D")

                runners[num_pmu] = number_of_disqualified
            else:
                runners[num_pmu] = 1

        runners_sorted = sorted(runners.items(), key=lambda x: x[1], reverse=reverse)

        scoring_runners = {}

        i = 1

        for runner in runners_sorted:
            scoring_runners[runner[0]] = i

            i += 1

        print(scoring_runners)

    # age : ok
    def test_scoring_the_runners_by_age_with_dark_web(self):
        print("test_scoring_the_runners_by_age_with_dark_web")

        reverse = False

        participant_key = 'age'

        url_unibet_race = global_url

        today = date.today()

        d1 = today.strftime("%d%m%Y")

        reunion = url_unibet_race.replace("https://www.unibet.fr/turf/race/", "").replace(today.strftime("%d-%m-%Y") + "-", "").replace("-", "")[:2]

        course = url_unibet_race.replace("https://www.unibet.fr/turf/race/", "").replace(today.strftime("%d-%m-%Y") + "-", "").replace("-", "")[2:4]

        url = "https://offline.turfinfo.api.pmu.fr/rest/client/1/programme/" \
              + d1 + "/" \
              + reunion + "/" \
              + course + "/participants"

        headers = {
            "Accept": "application/json",
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103'
        }

        rt = RequestsTor()

        response = rt.get(url, headers=headers)

        runners = {}

        for participant in response.json()['participants']:
            num_pmu = str(participant['numPmu'])

            if participant_key in participant:
                criteria = int(participant[participant_key])
                runners[num_pmu] = criteria
            else:
                runners[num_pmu] = 1

        runners_sorted = sorted(runners.items(), key=lambda x: x[1], reverse=reverse)

        scoring_runners = {}

        i = 1

        for runner in runners_sorted:
            scoring_runners[runner[0]] = i

            i += 1

        print(scoring_runners)

    # placeCorde : ok
    def test_scoring_the_runners_by_place_corde_with_dark_web(self):
        print("test_scoring_the_runners_by_place_corde_with_dark_web")

        reverse = False

        participant_key = 'placeCorde'

        url_unibet_race = global_url

        today = date.today()

        d1 = today.strftime("%d%m%Y")

        reunion = url_unibet_race.replace("https://www.unibet.fr/turf/race/", "").replace(today.strftime("%d-%m-%Y") + "-", "").replace("-", "")[:2]

        course = url_unibet_race.replace("https://www.unibet.fr/turf/race/", "").replace(today.strftime("%d-%m-%Y") + "-", "").replace("-", "")[2:4]

        url = "https://offline.turfinfo.api.pmu.fr/rest/client/1/programme/" \
              + d1 + "/" \
              + reunion + "/" \
              + course + "/participants"

        headers = {
            "Accept": "application/json",
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103'
        }

        rt = RequestsTor()

        response = rt.get(url, headers=headers)

        runners = {}

        for participant in response.json()['participants']:
            num_pmu = str(participant['numPmu'])

            if participant_key in participant:
                criteria = int(participant[participant_key])
                runners[num_pmu] = criteria
            else:
                runners[num_pmu] = 1

        runners_sorted = sorted(runners.items(), key=lambda x: x[1], reverse=reverse)

        scoring_runners = {}

        i = 1

        for runner in runners_sorted:
            scoring_runners[runner[0]] = i

            i += 1

        print(scoring_runners)

    # nombreCourses : ok
    def test_scoring_the_runners_by_nombre_courses_with_dark_web(self):
        print("test_scoring_the_runners_by_nombre_courses_with_dark_web")

        reverse = True

        participant_key = 'nombreCourses'

        url_unibet_race = global_url

        today = date.today()

        d1 = today.strftime("%d%m%Y")

        reunion = url_unibet_race.replace("https://www.unibet.fr/turf/race/", "").replace(today.strftime("%d-%m-%Y") + "-", "").replace("-", "")[:2]

        course = url_unibet_race.replace("https://www.unibet.fr/turf/race/", "").replace(today.strftime("%d-%m-%Y") + "-", "").replace("-", "")[2:4]

        url = "https://offline.turfinfo.api.pmu.fr/rest/client/1/programme/" \
              + d1 + "/" \
              + reunion + "/" \
              + course + "/participants"

        headers = {
            "Accept": "application/json",
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103'
        }

        rt = RequestsTor()

        response = rt.get(url, headers=headers)

        runners = {}

        for participant in response.json()['participants']:
            num_pmu = str(participant['numPmu'])

            if participant_key in participant:
                criteria = int(participant[participant_key])

                runners[num_pmu] = criteria
            else:
                runners[num_pmu] = 1

        runners_sorted = sorted(runners.items(), key=lambda x: x[1], reverse=reverse)

        scoring_runners = {}

        i = 1

        for runner in runners_sorted:
            scoring_runners[runner[0]] = i

            i += 1

        print(scoring_runners)

    # nombreVictoires : ok
    def test_scoring_the_runners_by_nombre_victoires_with_dark_web(self):
        print("test_scoring_the_runners_by_nombre_victoires_with_dark_web")

        reverse = True

        participant_key = 'nombreVictoires'

        url_unibet_race = global_url

        today = date.today()

        d1 = today.strftime("%d%m%Y")

        reunion = url_unibet_race.replace("https://www.unibet.fr/turf/race/", "").replace(today.strftime("%d-%m-%Y") + "-", "").replace("-", "")[:2]

        course = url_unibet_race.replace("https://www.unibet.fr/turf/race/", "").replace(today.strftime("%d-%m-%Y") + "-", "").replace("-", "")[2:4]

        url = "https://offline.turfinfo.api.pmu.fr/rest/client/1/programme/" \
              + d1 + "/" \
              + reunion + "/" \
              + course + "/participants"

        headers = {
            "Accept": "application/json",
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103'
        }

        rt = RequestsTor()

        response = rt.get(url, headers=headers)

        runners = {}

        for participant in response.json()['participants']:
            num_pmu = str(participant['numPmu'])

            if participant_key in participant:
                criteria = int(participant[participant_key])
                runners[num_pmu] = criteria
            else:
                runners[num_pmu] = 1

        runners_sorted = sorted(runners.items(), key=lambda x: x[1], reverse=reverse)

        scoring_runners = {}

        i = 1

        for runner in runners_sorted:
            scoring_runners[runner[0]] = i

            i += 1

        print(scoring_runners)

    # nombrePlaces : ok
    def test_scoring_the_runners_by_nombre_places_with_dark_web(self):
        print("test_scoring_the_runners_by_nombre_places_with_dark_web")

        reverse = True

        participant_key = 'nombrePlaces'

        url_unibet_race = global_url

        today = date.today()

        d1 = today.strftime("%d%m%Y")

        reunion = url_unibet_race.replace("https://www.unibet.fr/turf/race/", "").replace(today.strftime("%d-%m-%Y") + "-", "").replace("-", "")[:2]

        course = url_unibet_race.replace("https://www.unibet.fr/turf/race/", "").replace(today.strftime("%d-%m-%Y") + "-", "").replace("-", "")[2:4]

        url = "https://offline.turfinfo.api.pmu.fr/rest/client/1/programme/" \
              + d1 + "/" \
              + reunion + "/" \
              + course + "/participants"

        headers = {
            "Accept": "application/json",
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103'
        }

        rt = RequestsTor()

        response = rt.get(url, headers=headers)

        runners = {}

        for participant in response.json()['participants']:
            num_pmu = str(participant['numPmu'])

            if participant_key in participant:
                criteria = int(participant[participant_key])
                runners[num_pmu] = criteria
            else:
                runners[num_pmu] = 1

        runners_sorted = sorted(runners.items(), key=lambda x: x[1], reverse=reverse)

        scoring_runners = {}

        i = 1

        for runner in runners_sorted:
            scoring_runners[runner[0]] = i

            i += 1

        print(scoring_runners)

    # nombrePlacesSecond : ok
    def test_scoring_the_runners_by_nombre_places_second_with_dark_web(self):
        print("test_scoring_the_runners_by_nombre_places_second_with_dark_web")

        reverse = True

        participant_key = 'nombrePlacesSecond'

        url_unibet_race = global_url

        today = date.today()

        d1 = today.strftime("%d%m%Y")

        reunion = url_unibet_race.replace("https://www.unibet.fr/turf/race/", "").replace(today.strftime("%d-%m-%Y") + "-", "").replace("-", "")[:2]

        course = url_unibet_race.replace("https://www.unibet.fr/turf/race/", "").replace(today.strftime("%d-%m-%Y") + "-", "").replace("-", "")[2:4]

        url = "https://offline.turfinfo.api.pmu.fr/rest/client/1/programme/" \
              + d1 + "/" \
              + reunion + "/" \
              + course + "/participants"

        headers = {
            "Accept": "application/json",
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103'
        }

        rt = RequestsTor()

        response = rt.get(url, headers=headers)

        runners = {}

        for participant in response.json()['participants']:
            num_pmu = str(participant['numPmu'])

            if participant_key in participant:
                criteria = int(participant[participant_key])
                runners[num_pmu] = criteria
            else:
                runners[num_pmu] = 1

        runners_sorted = sorted(runners.items(), key=lambda x: x[1], reverse=reverse)

        scoring_runners = {}

        i = 1

        for runner in runners_sorted:
            scoring_runners[runner[0]] = i

            i += 1

        print(scoring_runners)

    # nombrePlacesTroisieme : ok
    def test_scoring_the_runners_by_nombre_places_troisieme_with_dark_web(self):
        print("test_scoring_the_runners_by_nombre_places_troisieme_with_dark_web")

        reverse = True

        participant_key = 'nombrePlacesTroisieme'

        url_unibet_race = global_url

        today = date.today()

        d1 = today.strftime("%d%m%Y")

        reunion = url_unibet_race.replace("https://www.unibet.fr/turf/race/", "").replace(today.strftime("%d-%m-%Y") + "-", "").replace("-", "")[:2]

        course = url_unibet_race.replace("https://www.unibet.fr/turf/race/", "").replace(today.strftime("%d-%m-%Y") + "-", "").replace("-", "")[2:4]

        url = "https://offline.turfinfo.api.pmu.fr/rest/client/1/programme/" \
              + d1 + "/" \
              + reunion + "/" \
              + course + "/participants"

        headers = {
            "Accept": "application/json",
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103'
        }

        rt = RequestsTor()

        response = rt.get(url, headers=headers)

        runners = {}

        for participant in response.json()['participants']:
            num_pmu = str(participant['numPmu'])

            if participant_key in participant:
                criteria = int(participant[participant_key])
                runners[num_pmu] = criteria
            else:
                runners[num_pmu] = 1

        runners_sorted = sorted(runners.items(), key=lambda x: x[1], reverse=reverse)

        scoring_runners = {}

        i = 1

        for runner in runners_sorted:
            scoring_runners[runner[0]] = i

            i += 1

        print(scoring_runners)

    # gainsParticipant of gainsCarriere : ok
    def test_scoring_the_runners_by_gains_participant_of_gains_carriere_with_dark_web(self):
        print("test_scoring_the_runners_by_gains_participant_of_gains_carriere_with_dark_web")

        reverse = True

        participant_key = 'gainsCarriere'

        url_unibet_race = global_url

        today = date.today()

        d1 = today.strftime("%d%m%Y")

        reunion = url_unibet_race.replace("https://www.unibet.fr/turf/race/", "").replace(today.strftime("%d-%m-%Y") + "-", "").replace("-", "")[:2]

        course = url_unibet_race.replace("https://www.unibet.fr/turf/race/", "").replace(today.strftime("%d-%m-%Y") + "-", "").replace("-", "")[2:4]

        url = "https://offline.turfinfo.api.pmu.fr/rest/client/1/programme/" \
              + d1 + "/" \
              + reunion + "/" \
              + course + "/participants"

        headers = {
            "Accept": "application/json",
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103'
        }

        rt = RequestsTor()

        response = rt.get(url, headers=headers)

        runners = {}

        for participant in response.json()['participants']:
            num_pmu = str(participant['numPmu'])

            if participant_key in participant:
                criteria = int(participant[participant_key])
                runners[num_pmu] = criteria
            else:
                runners[num_pmu] = 1

        runners_sorted = sorted(runners.items(), key=lambda x: x[1], reverse=reverse)

        scoring_runners = {}

        i = 1

        for runner in runners_sorted:
            scoring_runners[runner[0]] = i

            i += 1

        print(scoring_runners)

    # gainsParticipant of gainsVictoires : ok
    def test_scoring_the_runners_by_gains_participant_of_gains_victoires_with_dark_web(self):
        print("test_scoring_the_runners_by_gains_participant_of_gains_victoires_with_dark_web")

        reverse = True

        participant_key = 'gainsVictoires'

        url_unibet_race = global_url

        today = date.today()

        d1 = today.strftime("%d%m%Y")

        reunion = url_unibet_race.replace("https://www.unibet.fr/turf/race/", "").replace(today.strftime("%d-%m-%Y") + "-", "").replace("-", "")[:2]

        course = url_unibet_race.replace("https://www.unibet.fr/turf/race/", "").replace(today.strftime("%d-%m-%Y") + "-", "").replace("-", "")[2:4]

        url = "https://offline.turfinfo.api.pmu.fr/rest/client/1/programme/" \
              + d1 + "/" \
              + reunion + "/" \
              + course + "/participants"

        headers = {
            "Accept": "application/json",
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103'
        }

        rt = RequestsTor()

        response = rt.get(url, headers=headers)

        runners = {}

        for participant in response.json()['participants']:
            num_pmu = str(participant['numPmu'])

            if participant_key in participant:
                criteria = int(participant[participant_key])
                runners[num_pmu] = criteria
            else:
                runners[num_pmu] = 1

        runners_sorted = sorted(runners.items(), key=lambda x: x[1], reverse=reverse)

        scoring_runners = {}

        i = 1

        for runner in runners_sorted:
            scoring_runners[runner[0]] = i

            i += 1

        print(scoring_runners)

    # gainsParticipant of gainsPlace : ok
    def test_scoring_the_runners_by_gains_participant_of_gains_place_with_dark_web(self):
        print("test_scoring_the_runners_by_gains_participant_of_gains_place_with_dark_web")

        reverse = True

        participant_key = 'gainsPlace'

        url_unibet_race = global_url

        today = date.today()

        d1 = today.strftime("%d%m%Y")

        reunion = url_unibet_race.replace("https://www.unibet.fr/turf/race/", "").replace(today.strftime("%d-%m-%Y") + "-", "").replace("-", "")[:2]

        course = url_unibet_race.replace("https://www.unibet.fr/turf/race/", "").replace(today.strftime("%d-%m-%Y") + "-", "").replace("-", "")[2:4]

        url = "https://offline.turfinfo.api.pmu.fr/rest/client/1/programme/" \
              + d1 + "/" \
              + reunion + "/" \
              + course + "/participants"

        headers = {
            "Accept": "application/json",
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103'
        }

        rt = RequestsTor()

        response = rt.get(url, headers=headers)

        runners = {}

        for participant in response.json()['participants']:
            num_pmu = str(participant['numPmu'])

            if participant_key in participant:
                criteria = int(participant[participant_key])
                runners[num_pmu] = criteria
            else:
                runners[num_pmu] = 1

        runners_sorted = sorted(runners.items(), key=lambda x: x[1], reverse=reverse)

        scoring_runners = {}

        i = 1

        for runner in runners_sorted:
            scoring_runners[runner[0]] = i

            i += 1

        print(scoring_runners)

    # gainsParticipant of gainsAnneeEnCours : ok
    def test_scoring_the_runners_by_gains_participant_of_gains_annee_en_cours_with_dark_web(self):
        print("test_scoring_the_runners_by_gains_participant_of_gains_annee_en_cours_with_dark_web")

        reverse = True

        participant_key = 'gainsAnneeEnCours'

        url_unibet_race = global_url

        today = date.today()

        d1 = today.strftime("%d%m%Y")

        reunion = url_unibet_race.replace("https://www.unibet.fr/turf/race/", "").replace(today.strftime("%d-%m-%Y") + "-", "").replace("-", "")[:2]

        course = url_unibet_race.replace("https://www.unibet.fr/turf/race/", "").replace(today.strftime("%d-%m-%Y") + "-", "").replace("-", "")[2:4]

        url = "https://offline.turfinfo.api.pmu.fr/rest/client/1/programme/" \
              + d1 + "/" \
              + reunion + "/" \
              + course + "/participants"

        headers = {
            "Accept": "application/json",
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103'
        }

        rt = RequestsTor()

        response = rt.get(url, headers=headers)

        runners = {}

        for participant in response.json()['participants']:
            num_pmu = str(participant['numPmu'])

            if participant_key in participant:
                criteria = int(participant[participant_key])
                runners[num_pmu] = criteria
            else:
                runners[num_pmu] = 1

        runners_sorted = sorted(runners.items(), key=lambda x: x[1], reverse=reverse)

        scoring_runners = {}

        i = 1

        for runner in runners_sorted:
            scoring_runners[runner[0]] = i

            i += 1

        print(scoring_runners)

    # gainsParticipant of gainsAnneePrecedente : ok
    def test_scoring_the_runners_by_gains_participant_of_gains_annee_precedente_with_dark_web(self):
        print("test_scoring_the_runners_by_gains_participant_of_gains_annee_precedente_with_dark_web")

        reverse = True

        participant_key = 'gainsAnneePrecedente'

        url_unibet_race = global_url

        today = date.today()

        d1 = today.strftime("%d%m%Y")

        reunion = url_unibet_race.replace("https://www.unibet.fr/turf/race/", "").replace(today.strftime("%d-%m-%Y") + "-", "").replace("-", "")[:2]

        course = url_unibet_race.replace("https://www.unibet.fr/turf/race/", "").replace(today.strftime("%d-%m-%Y") + "-", "").replace("-", "")[2:4]

        url = "https://offline.turfinfo.api.pmu.fr/rest/client/1/programme/" \
              + d1 + "/" \
              + reunion + "/" \
              + course + "/participants"

        headers = {
            "Accept": "application/json",
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103'
        }

        rt = RequestsTor()

        response = rt.get(url, headers=headers)

        runners = {}

        for participant in response.json()['participants']:
            num_pmu = str(participant['numPmu'])

            if participant_key in participant:
                criteria = int(participant[participant_key])
                runners[num_pmu] = criteria
            else:
                runners[num_pmu] = 1

        runners_sorted = sorted(runners.items(), key=lambda x: x[1], reverse=reverse)

        scoring_runners = {}

        i = 1

        for runner in runners_sorted:
            scoring_runners[runner[0]] = i

            i += 1

        print(scoring_runners)

    # supplement : ok
    def test_scoring_the_runners_by_supplement_with_dark_web(self):
        print("test_scoring_the_runners_by_supplement_with_dark_web")

        reverse = True

        participant_key = 'supplement'

        url_unibet_race = global_url

        today = date.today()

        d1 = today.strftime("%d%m%Y")

        reunion = url_unibet_race.replace("https://www.unibet.fr/turf/race/", "").replace(today.strftime("%d-%m-%Y") + "-", "").replace("-", "")[:2]

        course = url_unibet_race.replace("https://www.unibet.fr/turf/race/", "").replace(today.strftime("%d-%m-%Y") + "-", "").replace("-", "")[2:4]

        url = "https://offline.turfinfo.api.pmu.fr/rest/client/1/programme/" \
              + d1 + "/" \
              + reunion + "/" \
              + course + "/participants"

        headers = {
            "Accept": "application/json",
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103'
        }

        rt = RequestsTor()

        response = rt.get(url, headers=headers)

        runners = {}

        for participant in response.json()['participants']:
            num_pmu = str(participant['numPmu'])

            if participant_key in participant:
                criteria = int(participant[participant_key])
                runners[num_pmu] = criteria
            else:
                runners[num_pmu] = 1

        runners_sorted = sorted(runners.items(), key=lambda x: x[1], reverse=reverse)

        scoring_runners = {}

        i = 1

        for runner in runners_sorted:
            scoring_runners[runner[0]] = i

            i += 1

        print(scoring_runners)

    # handicapDistance : ok
    def test_scoring_the_runners_by_handicap_distance_with_dark_web(self):
        print("test_scoring_the_runners_by_handicap_distance_with_dark_web")

        reverse = False

        participant_key = 'handicapDistance'

        url_unibet_race = global_url

        today = date.today()

        d1 = today.strftime("%d%m%Y")

        reunion = url_unibet_race.replace("https://www.unibet.fr/turf/race/", "").replace(today.strftime("%d-%m-%Y") + "-", "").replace("-", "")[:2]

        course = url_unibet_race.replace("https://www.unibet.fr/turf/race/", "").replace(today.strftime("%d-%m-%Y") + "-", "").replace("-", "")[2:4]

        url = "https://offline.turfinfo.api.pmu.fr/rest/client/1/programme/" \
              + d1 + "/" \
              + reunion + "/" \
              + course + "/participants"

        headers = {
            "Accept": "application/json",
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103'
        }

        rt = RequestsTor()

        response = rt.get(url, headers=headers)

        runners = {}

        for participant in response.json()['participants']:
            num_pmu = str(participant['numPmu'])

            if participant_key in participant:
                criteria = int(participant[participant_key])
                runners[num_pmu] = criteria
            else:
                runners[num_pmu] = 1

        runners_sorted = sorted(runners.items(), key=lambda x: x[1], reverse=reverse)

        scoring_runners = {}

        i = 1

        for runner in runners_sorted:
            scoring_runners[runner[0]] = i

            i += 1

        print(scoring_runners)

    # dernierRapportDirect of rapport : ok
    def test_scoring_the_runners_by_dernier_rapport_direct_of_rapport_with_dark_web(self):
        print("test_scoring_the_runners_by_dernier_rapport_direct_of_rapport_with_dark_web")

        reverse = False

        participant_key = 'rapport'

        url_unibet_race = global_url

        today = date.today()

        d1 = today.strftime("%d%m%Y")

        reunion = url_unibet_race.replace("https://www.unibet.fr/turf/race/", "").replace(today.strftime("%d-%m-%Y") + "-", "").replace("-", "")[:2]

        course = url_unibet_race.replace("https://www.unibet.fr/turf/race/", "").replace(today.strftime("%d-%m-%Y") + "-", "").replace("-", "")[2:4]

        url = "https://offline.turfinfo.api.pmu.fr/rest/client/1/programme/" \
              + d1 + "/" \
              + reunion + "/" \
              + course + "/participants"

        headers = {
            "Accept": "application/json",
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103'
        }

        rt = RequestsTor()

        response = rt.get(url, headers=headers)

        runners = {}

        for participant in response.json()['participants']:
            num_pmu = str(participant['numPmu'])

            if participant_key in participant:
                criteria = int(participant[participant_key])
                runners[num_pmu] = criteria
            else:
                runners[num_pmu] = 1

        runners_sorted = sorted(runners.items(), key=lambda x: x[1], reverse=reverse)

        scoring_runners = {}

        i = 1

        for runner in runners_sorted:
            scoring_runners[runner[0]] = i

            i += 1

        print(scoring_runners)

    # dernierRapportDirect of nombreIndicateurTendance : ok
    def test_scoring_the_runners_by_dernier_rapport_direct_of_nombre_indicateur_tendance_with_dark_web(self):
        print("test_scoring_the_runners_by_dernier_rapport_direct_of_nombre_indicateur_tendance_with_dark_web")

        reverse = False

        participant_key = 'nombreIndicateurTendance'

        url_unibet_race = global_url

        today = date.today()

        d1 = today.strftime("%d%m%Y")

        reunion = url_unibet_race.replace("https://www.unibet.fr/turf/race/", "").replace(today.strftime("%d-%m-%Y") + "-", "").replace("-", "")[:2]

        course = url_unibet_race.replace("https://www.unibet.fr/turf/race/", "").replace(today.strftime("%d-%m-%Y") + "-", "").replace("-", "")[2:4]

        url = "https://offline.turfinfo.api.pmu.fr/rest/client/1/programme/" \
              + d1 + "/" \
              + reunion + "/" \
              + course + "/participants"

        headers = {
            "Accept": "application/json",
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103'
        }

        rt = RequestsTor()

        response = rt.get(url, headers=headers)

        runners = {}

        for participant in response.json()['participants']:
            num_pmu = str(participant['numPmu'])

            if participant_key in participant:
                criteria = int(participant[participant_key])
                runners[num_pmu] = criteria
            else:
                runners[num_pmu] = 1

        runners_sorted = sorted(runners.items(), key=lambda x: x[1], reverse=reverse)

        scoring_runners = {}

        i = 1

        for runner in runners_sorted:
            scoring_runners[runner[0]] = i

            i += 1

        print(scoring_runners)

    # dernierRapportDirect of permutation : ok
    def test_scoring_the_runners_by_dernier_rapport_direct_of_permutation_with_dark_web(self):
        print("test_scoring_the_runners_by_dernier_rapport_direct_of_permutation_with_dark_web")

        reverse = False

        participant_key = 'permutation'

        url_unibet_race = global_url

        today = date.today()

        d1 = today.strftime("%d%m%Y")

        reunion = url_unibet_race.replace("https://www.unibet.fr/turf/race/", "").replace(today.strftime("%d-%m-%Y") + "-", "").replace("-", "")[:2]

        course = url_unibet_race.replace("https://www.unibet.fr/turf/race/", "").replace(today.strftime("%d-%m-%Y") + "-", "").replace("-", "")[2:4]

        url = "https://offline.turfinfo.api.pmu.fr/rest/client/1/programme/" \
              + d1 + "/" \
              + reunion + "/" \
              + course + "/participants"

        headers = {
            "Accept": "application/json",
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103'
        }

        rt = RequestsTor()

        response = rt.get(url, headers=headers)

        runners = {}

        for participant in response.json()['participants']:
            num_pmu = str(participant['numPmu'])

            if participant_key in participant:
                criteria = int(participant[participant_key])
                runners[num_pmu] = criteria
            else:
                runners[num_pmu] = 1

        runners_sorted = sorted(runners.items(), key=lambda x: x[1], reverse=reverse)

        scoring_runners = {}

        i = 1

        for runner in runners_sorted:
            scoring_runners[runner[0]] = i

            i += 1

        print(scoring_runners)

    # dernierRapportDirect of numPmu1 : ok
    def test_scoring_the_runners_by_dernier_rapport_direct_of_num_pmu_1_with_dark_web(self):
        print("test_scoring_the_runners_by_dernier_rapport_direct_of_num_pmu_1_with_dark_web")

        reverse = False

        participant_key = 'numPmu1'

        url_unibet_race = global_url

        today = date.today()

        d1 = today.strftime("%d%m%Y")

        reunion = url_unibet_race.replace("https://www.unibet.fr/turf/race/", "").replace(today.strftime("%d-%m-%Y") + "-", "").replace("-", "")[:2]

        course = url_unibet_race.replace("https://www.unibet.fr/turf/race/", "").replace(today.strftime("%d-%m-%Y") + "-", "").replace("-", "")[2:4]

        url = "https://offline.turfinfo.api.pmu.fr/rest/client/1/programme/" \
              + d1 + "/" \
              + reunion + "/" \
              + course + "/participants"

        headers = {
            "Accept": "application/json",
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103'
        }

        rt = RequestsTor()

        response = rt.get(url, headers=headers)

        runners = {}

        for participant in response.json()['participants']:
            num_pmu = str(participant['numPmu'])

            if participant_key in participant:
                criteria = int(participant[participant_key])
                runners[num_pmu] = criteria
            else:
                runners[num_pmu] = 1

        runners_sorted = sorted(runners.items(), key=lambda x: x[1], reverse=reverse)

        scoring_runners = {}

        i = 1

        for runner in runners_sorted:
            scoring_runners[runner[0]] = i

            i += 1

        print(scoring_runners)

    # dernierRapportReference of rapport : ok
    def test_scoring_the_runners_by_dernier_rapport_reference_of_rapport_with_dark_web(self):
        print("test_scoring_the_runners_by_dernier_rapport_reference_of_rapport_with_dark_web")

        reverse = False

        participant_key = 'rapport'

        url_unibet_race = global_url

        today = date.today()

        d1 = today.strftime("%d%m%Y")

        reunion = url_unibet_race.replace("https://www.unibet.fr/turf/race/", "").replace(today.strftime("%d-%m-%Y") + "-", "").replace("-", "")[:2]

        course = url_unibet_race.replace("https://www.unibet.fr/turf/race/", "").replace(today.strftime("%d-%m-%Y") + "-", "").replace("-", "")[2:4]

        url = "https://offline.turfinfo.api.pmu.fr/rest/client/1/programme/" \
              + d1 + "/" \
              + reunion + "/" \
              + course + "/participants"

        headers = {
            "Accept": "application/json",
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103'
        }

        rt = RequestsTor()

        response = rt.get(url, headers=headers)

        runners = {}

        for participant in response.json()['participants']:
            num_pmu = str(participant['numPmu'])

            if "dernierRapportReference" in participant:
                criteria = int(participant['dernierRapportReference'][participant_key])
                runners[num_pmu] = criteria
            else:
                runners[num_pmu] = 1

        runners_sorted = sorted(runners.items(), key=lambda x: x[1], reverse=reverse)

        scoring_runners = {}

        i = 1

        for runner in runners_sorted:
            scoring_runners[runner[0]] = i

            i += 1

        print(scoring_runners)

    # dernierRapportReference of nombreIndicateurTendance : ok
    def test_scoring_the_runners_by_dernier_rapport_reference_of_nombre_indicateur_tendance_with_dark_web(self):
        print("test_scoring_the_runners_by_dernier_rapport_reference_of_nombre_indicateur_tendance_with_dark_web")

        reverse = False

        participant_key = 'nombreIndicateurTendance'

        url_unibet_race = global_url

        today = date.today()

        d1 = today.strftime("%d%m%Y")

        reunion = url_unibet_race.replace("https://www.unibet.fr/turf/race/", "").replace(today.strftime("%d-%m-%Y") + "-", "").replace("-", "")[:2]

        course = url_unibet_race.replace("https://www.unibet.fr/turf/race/", "").replace(today.strftime("%d-%m-%Y") + "-", "").replace("-", "")[2:4]

        url = "https://offline.turfinfo.api.pmu.fr/rest/client/1/programme/" \
              + d1 + "/" \
              + reunion + "/" \
              + course + "/participants"

        headers = {
            "Accept": "application/json",
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103'
        }

        rt = RequestsTor()

        response = rt.get(url, headers=headers)

        runners = {}

        for participant in response.json()['participants']:
            num_pmu = str(participant['numPmu'])

            if "dernierRapportReference" in participant:
                criteria = int(participant['dernierRapportReference'][participant_key])
                runners[num_pmu] = criteria
            else:
                runners[num_pmu] = 1

        runners_sorted = sorted(runners.items(), key=lambda x: x[1], reverse=reverse)

        scoring_runners = {}

        i = 1

        for runner in runners_sorted:
            scoring_runners[runner[0]] = i

            i += 1

        print(scoring_runners)

    # dernierRapportReference of permutation : ok
    def test_scoring_the_runners_by_dernier_rapport_reference_of_permutation_with_dark_web(self):
        print("test_scoring_the_runners_by_dernier_rapport_reference_of_nombre_indicateur_tendance_with_dark_web")

        reverse = False

        participant_key = 'permutation'

        url_unibet_race = global_url

        today = date.today()

        d1 = today.strftime("%d%m%Y")

        reunion = url_unibet_race.replace("https://www.unibet.fr/turf/race/", "").replace(today.strftime("%d-%m-%Y") + "-", "").replace("-", "")[:2]

        course = url_unibet_race.replace("https://www.unibet.fr/turf/race/", "").replace(today.strftime("%d-%m-%Y") + "-", "").replace("-", "")[2:4]

        url = "https://offline.turfinfo.api.pmu.fr/rest/client/1/programme/" \
              + d1 + "/" \
              + reunion + "/" \
              + course + "/participants"

        headers = {
            "Accept": "application/json",
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103'
        }

        rt = RequestsTor()

        response = rt.get(url, headers=headers)

        runners = {}

        for participant in response.json()['participants']:
            num_pmu = str(participant['numPmu'])

            if "dernierRapportReference" in participant:
                criteria = int(participant['dernierRapportReference'][participant_key])
                runners[num_pmu] = criteria
            else:
                runners[num_pmu] = 1

        runners_sorted = sorted(runners.items(), key=lambda x: x[1], reverse=reverse)

        scoring_runners = {}

        i = 1

        for runner in runners_sorted:
            scoring_runners[runner[0]] = i

            i += 1

        print(scoring_runners)

    # dernierRapportReference of numPmu1 : ok
    def test_scoring_the_runners_by_dernier_rapport_reference_of_num_pmu_1_with_dark_web(self):
        print("test_scoring_the_runners_by_dernier_rapport_reference_of_num_pmu_1_with_dark_web")

        reverse = False

        participant_key = 'numPmu1'

        url_unibet_race = global_url

        today = date.today()

        d1 = today.strftime("%d%m%Y")

        reunion = url_unibet_race.replace("https://www.unibet.fr/turf/race/", "").replace(today.strftime("%d-%m-%Y") + "-", "").replace("-", "")[:2]

        course = url_unibet_race.replace("https://www.unibet.fr/turf/race/", "").replace(today.strftime("%d-%m-%Y") + "-", "").replace("-", "")[2:4]

        url = "https://offline.turfinfo.api.pmu.fr/rest/client/1/programme/" \
              + d1 + "/" \
              + reunion + "/" \
              + course + "/participants"

        headers = {
            "Accept": "application/json",
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103'
        }

        rt = RequestsTor()

        response = rt.get(url, headers=headers)

        runners = {}

        for participant in response.json()['participants']:
            num_pmu = str(participant['numPmu'])

            if "dernierRapportReference" in participant:
                criteria = int(participant['dernierRapportReference'][participant_key])
                runners[num_pmu] = criteria
            else:
                runners[num_pmu] = 1

        runners_sorted = sorted(runners.items(), key=lambda x: x[1], reverse=reverse)

        scoring_runners = {}

        i = 1

        for runner in runners_sorted:
            scoring_runners[runner[0]] = i

            i += 1

        print(scoring_runners)

    # musique : ok
    def test_scoring_the_runners_by_musique_with_dark_web(self):
        print("test_scoring_the_runners_by_musique_with_dark_web")

        reverse = False

        participant_key = 'musique'

        url_unibet_race = global_url

        today = date.today()

        d1 = today.strftime("%d%m%Y")

        reunion = url_unibet_race.replace("https://www.unibet.fr/turf/race/", "").replace(today.strftime("%d-%m-%Y") + "-", "").replace("-", "")[:2]

        course = url_unibet_race.replace("https://www.unibet.fr/turf/race/", "").replace(today.strftime("%d-%m-%Y") + "-", "").replace("-", "")[2:4]

        url = "https://offline.turfinfo.api.pmu.fr/rest/client/1/programme/" \
              + d1 + "/" \
              + reunion + "/" \
              + course + "/participants"

        headers = {
            "Accept": "application/json",
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103'
        }

        rt = RequestsTor()

        response = rt.get(url, headers=headers)

        runners = {}

        for participant in response.json()['participants']:
            num_pmu = str(participant['numPmu'])

            if participant_key in participant:
                criteria = str(participant[participant_key]) \
                    .replace('D', '0')\
                    .replace('Q', '0') \
                    .replace('R', '0') \
                    .replace('A', '0') \
                    .replace('T', '0') \
                    .replace('(22)', '') \
                    .replace('(21)', '')\
                    .replace('(20)', '')\
                    .replace('(19)', '')\
                    .replace('(18)', '')\
                    .replace('(17)', '') \
                    .replace('a', '') \
                    .replace('m', '') \
                    .replace('s', '') \
                    .replace('c', '') \
                    .replace('p', '') \
                    .replace('h', '')

                average = 0

                print(str(criteria))

                for i in range(0, len(criteria)):
                    average += int(criteria[i])

                average_musique = average/len(criteria)

                runners[num_pmu] = average_musique
            else:
                runners[num_pmu] = 1

        runners_sorted = sorted(runners.items(), key=lambda x: x[1], reverse=reverse)

        scoring_runners = {}

        i = 1

        for runner in runners_sorted:
            scoring_runners[runner[0]] = i

            i += 1

        print(scoring_runners)

    # musique from unibet : ok
    def test_scoring_the_runners_by_musique_from_unibet(self):
        print("test_scoring_the_runners_by_musique_from_unibet")

        reverse = False

        url = global_url

        warnings.filterwarnings(action="ignore", message="unclosed", category=ResourceWarning)

        # with Firefox
        options = Options()
        options.headless = True
        browser = webdriver.Firefox(executable_path='..\\geckodriver.exe', options=options)

        time.sleep(10)

        # maximize window
        browser.maximize_window()

        time.sleep(5)

        # open
        browser.get(url)

        time.sleep(20)

        number_of_racers = int(
            browser.find_element_by_xpath(
                "//p[@class='race-meta ui-mainview-block']"
            ).text.lower().split(" - ")[3].replace(' partants', '')
        )

        runners = {}

        for i in range(1, number_of_racers + 1):
            num_pmu = browser.find_element_by_xpath(
                "/html/body/div/div[2]/div[5]/div/div/section/div/div/div/div/div/div/div/div[2]/div/div[3]/"
                "ul[2]/li/div/div[2]/ul/li[" + str(i + 1) + "]/div/div[1]/span"
            ).text

            try:
                musique = browser.find_element_by_xpath(
                    "/html/body/div[1]/div[2]/div[5]/div/div/section/div/div/div/div/div/div/div/div[2]/div/div[3]"
                    "/ul[2]/li/div/div[2]/ul/li[" + str(i + 1) + "]/div"
                ).find_element_by_class_name("musique")\
                    .text \
                    .replace('a', '') \
                    .replace('m', '') \
                    .replace('D', '') \
                    .replace('Q', '') \
                    .replace('R', '') \
                    .replace('A', '') \
                    .replace('p', '') \
                    .replace('s', '') \
                    .replace('h', '') \
                    .replace('c', '') \
                    .replace('T', '') \
                    .replace(' ', '') \
                    .replace('(21)', '') \
                    .replace('(20)', '') \
                    .replace('(19)', '') \
                    .replace('(18)', '') \
                    .replace('(17)', '')

                print("num_pmu : " + str(num_pmu) + " , musique : " + str(musique))

                average = 0

                for i1 in range(0, len(musique)):
                    average += int(musique[i1])

                average_musique = average / len(musique)

                runners[num_pmu] = average_musique
            except Exception as e:
                print('unable to locate the element : 1 _ ' + str(e))

        time.sleep(5)

        runners_sorted = sorted(runners.items(), key=lambda x: x[1], reverse=reverse)

        scoring_runners = {}

        i = 1

        for runner in runners_sorted:
            scoring_runners[runner[0]] = i

            i += 1

        time.sleep(5)

        browser.quit()

        print(scoring_runners)

    # cote direct from unibet : ok
    def test_scoring_the_runners_by_cote_direct_from_unibet(self):
        print("test_scoring_the_runners_by_cote_direct_from_unibet_with_dark_web")

        reverse = False

        url = global_url

        warnings.filterwarnings(action="ignore", message="unclosed", category=ResourceWarning)

        # with Firefox
        options = Options()
        options.headless = True
        browser = webdriver.Firefox(executable_path='..\\geckodriver.exe', options=options)

        time.sleep(10)

        # maximize window
        browser.maximize_window()

        time.sleep(5)

        # open
        browser.get(url)

        time.sleep(20)

        number_of_racers = int(
            browser.find_element_by_xpath("//p[@class='race-meta ui-mainview-block']").text
                .lower().split(" - ")[3].replace(' partants', '')
        )

        runners = {}

        for i in range(1, number_of_racers + 1):
            num_pmu = browser.find_element_by_xpath(
                "/html/body/div/div[2]/div[5]/div/div/section/div/div/div/div/div/div/div/div[2]/div/div[3]/"
                "ul[2]/li/div/div[2]/ul/li[" + str(i + 1) + "]/div/div[1]/span"
            ).text

            try:
                cote_direct = browser.find_element_by_xpath(
                    "/html/body/div[1]/div[2]/div[5]/div/div/section/div/div/div/div/div/div/div/div[2]/div/div[3]"
                    "/ul[2]/li/div/div[2]/ul/li[" + str(i + 1) + "]/div"
                ).find_element_by_class_name("price-live").text

                print("num_pmu : " + str(num_pmu) + " , cote_direct : " + str(cote_direct))

                if cote_direct != "NP":
                    runners[num_pmu] = float(cote_direct)
                else:
                    runners[num_pmu] = 200
            except Exception as e:
                print('unable to locate element : 1 _ ' + str(e))

        time.sleep(5)

        runners_sorted = sorted(runners.items(), key=lambda x: x[1], reverse=reverse)

        scoring_runners = {}

        i = 1

        for runner in runners_sorted:
            scoring_runners[runner[0]] = i

            i += 1

        time.sleep(5)

        browser.quit()

        print(scoring_runners)

    # cotes matin from unibet : ok
    def test_scoring_the_runners_by_cote_matin_from_unibet(self):
        print('test_scoring_the_runners_by_cote_matin_from_unibet')

        reverse = False

        url = global_url

        warnings.filterwarnings(action="ignore", message="unclosed", category=ResourceWarning)

        # with Firefox
        options = Options()
        options.headless = True
        browser = webdriver.Firefox(executable_path='..\\geckodriver.exe', options=options)

        time.sleep(10)

        # maximize window
        browser.maximize_window()

        time.sleep(5)

        # open
        browser.get(url)

        time.sleep(20)

        number_of_racers = int(
            browser.find_element_by_xpath("//p[@class='race-meta ui-mainview-block']").text.lower().split(" - ")[
                3].replace(' partants', '')
        )

        runners = {}

        for i in range(1, number_of_racers + 1):
            num_pmu = browser.find_element_by_xpath(
                "/html/body/div/div[2]/div[5]/div/div/section/div/div/div/div/div/div/div/div[2]/div/div[3]/"
                "ul[2]/li/div/div[2]/ul/li[" + str(i + 1) + "]/div/div[1]/span"
            ).text

            try:
                cote_matin = browser.find_element_by_xpath(
                    "/html/body/div[1]/div[2]/div[5]/div/div/section/div/div/div/div/div/div/div/div[2]/div/div[3]"
                    "/ul[2]/li/div/div[2]/ul/li[" + str(i + 1) + "]/div"
                ).find_element_by_class_name("price-morning").text

                print("num_pmu : " + str(num_pmu) + " , cote_matin : " + str(cote_matin))

                if cote_matin != "NP":
                    runners[num_pmu] = float(cote_matin)
                else:
                    runners[num_pmu] = 200
            except Exception as e:
                print('unable to locate element : 1 _ ' + str(e))

        time.sleep(5)

        runners_sorted = sorted(runners.items(), key=lambda x: x[1], reverse=reverse)

        scoring_runners = {}

        i = 1

        for runner in runners_sorted:
            scoring_runners[runner[0]] = i

            i += 1

        time.sleep(5)

        browser.quit()

        print(scoring_runners)

    # poids from unibet : ok
    def test_scoring_the_runners_by_poids_from_unibet(self):
        print("test_scoring_the_runners_by_poids_from_unibet")

        reverse = False

        url = global_url

        warnings.filterwarnings(action="ignore", message="unclosed", category=ResourceWarning)

        # with Firefox
        options = Options()
        options.headless = True
        browser = webdriver.Firefox(executable_path='..\\geckodriver.exe', options=options)

        time.sleep(10)

        # maximize window
        browser.maximize_window()

        time.sleep(5)

        # open
        browser.get(url)

        time.sleep(20)

        number_of_racers = int(
            browser.find_element_by_xpath(
                "//p[@class='race-meta ui-mainview-block']"
            ).text.lower().split(" - ")[3].replace(' partants', '')
        )

        runners = {}

        for i in range(1, number_of_racers + 1):
            num_pmu = browser.find_element_by_xpath(
                "/html/body/div/div[2]/div[5]/div/div/section/div/div/div/div/div/div/div/div[2]/div/div[3]/"
                "ul[2]/li/div/div[2]/ul/li[" + str(i + 1) + "]/div/div[1]/span"
            ).text

            try:
                poids = browser.find_element_by_xpath(
                    "/html/body/div[1]/div[2]/div[5]/div/div/section/div/div/div/div/div/div/div/div[2]/div/div[3]"
                    "/ul[2]/li/div/div[2]/ul/li[" + str(i + 1) + "]/div"
                ).find_element_by_class_name("weight").text.lower().replace(' ', '').replace('kg', '')

                runners[num_pmu] = poids
            except Exception as e:
                print('error poids : ' + str(e))
                runners[num_pmu] = 1

        time.sleep(5)

        runners_sorted = sorted(runners.items(), key=lambda x: x[1], reverse=reverse)

        scoring_runners = {}

        i = 1

        for runner in runners_sorted:
            scoring_runners[runner[0]] = i

            i += 1

        time.sleep(5)

        browser.quit()

        print(scoring_runners)

    # number of disqualified from musique from unibet : ok
    def test_scoring_the_runners_by_number_of_disqualified_from_unibet(self):
        print("test_scoring_the_runners_by_number_of_disqualified_from_unibet")

        reverse = False

        url = global_url

        warnings.filterwarnings(action="ignore", message="unclosed", category=ResourceWarning)

        # with Firefox
        options = Options()
        options.headless = True
        browser = webdriver.Firefox(executable_path='..\\geckodriver.exe', options=options)

        time.sleep(10)

        # maximize window
        browser.maximize_window()

        time.sleep(5)

        # open
        browser.get(url)

        time.sleep(20)

        number_of_racers = int(
            browser.find_element_by_xpath(
                "//p[@class='race-meta ui-mainview-block']"
            ).text.lower().split(" - ")[3].replace(' partants', '')
        )

        runners = {}

        for i in range(1, number_of_racers + 1):
            num_pmu = browser.find_element_by_xpath(
                "/html/body/div/div[2]/div[5]/div/div/section/div/div/div/div/div/div/div/div[2]/div/div[3]/"
                "ul[2]/li/div/div[2]/ul/li[" + str(i + 1) + "]/div/div[1]/span"
            ).text

            try:
                musique = browser.find_element_by_xpath(
                    "/html/body/div[1]/div[2]/div[5]/div/div/section/div/div/div/div/div/div/div/div[2]/div/div[3]"
                    "/ul[2]/li/div/div[2]/ul/li[" + str(i + 1) + "]/div"
                ).find_element_by_class_name("musique").text

                number_of_disqualified = musique.count("D")

                runners[num_pmu] = number_of_disqualified
            except Exception as e:
                print('unable to locate the element : 1 _ ' + str(e))

        time.sleep(5)

        runners_sorted = sorted(runners.items(), key=lambda x: x[1], reverse=reverse)

        scoring_runners = {}

        i = 1

        for runner in runners_sorted:
            scoring_runners[runner[0]] = i

            i += 1

        time.sleep(5)

        browser.quit()

        print(scoring_runners)

    # musique from unibet x cote direct : ok
    def test_scoring_the_runners_by_musique_from_unibet_x_cote_direct(self):
        print("test_scoring_the_runners_by_musique_from_unibet_x_cote_direct")

        reverse = False

        url = global_url

        warnings.filterwarnings(action="ignore", message="unclosed", category=ResourceWarning)

        # with Firefox
        options = Options()
        options.headless = True
        browser = webdriver.Firefox(executable_path='..\\geckodriver.exe', options=options)

        time.sleep(10)

        # maximize window
        browser.maximize_window()

        time.sleep(5)

        # open
        browser.get(url)

        time.sleep(20)

        number_of_racers = int(
            browser.find_element_by_xpath(
                "//p[@class='race-meta ui-mainview-block']"
            ).text.lower().split(" - ")[3].replace(' partants', '')
        )

        runners = {}

        for i in range(1, number_of_racers + 1):
            num_pmu = browser.find_element_by_xpath(
                "/html/body/div/div[2]/div[5]/div/div/section/div/div/div/div/div/div/div/div[2]/div/div[3]/"
                "ul[2]/li/div/div[2]/ul/li[" + str(i + 1) + "]/div/div[1]/span"
            ).text

            try:
                musique = browser.find_element_by_xpath(
                    "/html/body/div[1]/div[2]/div[5]/div/div/section/div/div/div/div/div/div/div/div[2]/div/div[3]"
                    "/ul[2]/li/div/div[2]/ul/li[" + str(i + 1) + "]/div"
                ).find_element_by_class_name("musique")\
                    .text \
                    .replace('a', '') \
                    .replace('m', '') \
                    .replace('D', '') \
                    .replace('Q', '') \
                    .replace('R', '') \
                    .replace('A', '') \
                    .replace('p', '') \
                    .replace('s', '') \
                    .replace('h', '') \
                    .replace('c', '') \
                    .replace('T', '') \
                    .replace(' ', '') \
                    .replace('(21)', '') \
                    .replace('(20)', '') \
                    .replace('(19)', '') \
                    .replace('(18)', '') \
                    .replace('(17)', '')

                print("num_pmu : " + str(num_pmu) + " , musique : " + str(musique))

                average = 0

                for i1 in range(0, len(musique)):
                    average += int(musique[i1])

                average_musique = average / len(musique)

                cote_direct = browser.find_element_by_xpath(
                    "/html/body/div[1]/div[2]/div[5]/div/div/section/div/div/div/div/div/div/div/div[2]/div/div[3]"
                    "/ul[2]/li/div/div[2]/ul/li[" + str(i + 1) + "]/div"
                ).find_element_by_class_name("price-live").text

                print("num_pmu : " + str(num_pmu) + " , cote_direct : " + str(cote_direct))

                if cote_direct != "NP":
                    runners[num_pmu] = float(cote_direct) * average_musique
                else:
                    runners[num_pmu] = average_musique
            except Exception as e:
                print('unable to locate the element : 1 _ ' + str(e))

        time.sleep(5)

        runners_sorted = sorted(runners.items(), key=lambda x: x[1], reverse=reverse)

        scoring_runners = {}

        i = 1

        for runner in runners_sorted:
            scoring_runners[runner[0]] = i

            i += 1

        time.sleep(5)

        browser.quit()

        print(scoring_runners)

    # musique from unibet x cote matin : ok
    def test_scoring_the_runners_by_musique_from_unibet_x_cote_matin(self):
        print("test_scoring_the_runners_by_musique_from_unibet_x_cote_matin")

        reverse = False

        url = global_url

        warnings.filterwarnings(action="ignore", message="unclosed", category=ResourceWarning)

        # with Firefox
        options = Options()
        options.headless = True
        browser = webdriver.Firefox(executable_path='..\\geckodriver.exe', options=options)

        time.sleep(10)

        # maximize window
        browser.maximize_window()

        time.sleep(5)

        # open
        browser.get(url)

        time.sleep(20)

        number_of_racers = int(
            browser.find_element_by_xpath(
                "//p[@class='race-meta ui-mainview-block']"
            ).text.lower().split(" - ")[3].replace(' partants', '')
        )

        runners = {}

        for i in range(1, number_of_racers + 1):
            num_pmu = browser.find_element_by_xpath(
                "/html/body/div/div[2]/div[5]/div/div/section/div/div/div/div/div/div/div/div[2]/div/div[3]/"
                "ul[2]/li/div/div[2]/ul/li[" + str(i + 1) + "]/div/div[1]/span"
            ).text

            try:
                musique = browser.find_element_by_xpath(
                    "/html/body/div[1]/div[2]/div[5]/div/div/section/div/div/div/div/div/div/div/div[2]/div/div[3]"
                    "/ul[2]/li/div/div[2]/ul/li[" + str(i + 1) + "]/div"
                ).find_element_by_class_name("musique")\
                    .text \
                    .replace('a', '') \
                    .replace('m', '') \
                    .replace('D', '') \
                    .replace('Q', '') \
                    .replace('R', '') \
                    .replace('A', '') \
                    .replace('p', '') \
                    .replace('s', '') \
                    .replace('h', '') \
                    .replace('c', '') \
                    .replace('T', '') \
                    .replace(' ', '') \
                    .replace('(21)', '') \
                    .replace('(20)', '') \
                    .replace('(19)', '') \
                    .replace('(18)', '') \
                    .replace('(17)', '')

                print("num_pmu : " + str(num_pmu) + " , musique : " + str(musique))

                average = 0

                for i1 in range(0, len(musique)):
                    average += int(musique[i1])

                average_musique = average / len(musique)

                cote_matin = browser.find_element_by_xpath(
                    "/html/body/div[1]/div[2]/div[5]/div/div/section/div/div/div/div/div/div/div/div[2]/div/div[3]"
                    "/ul[2]/li/div/div[2]/ul/li[" + str(i + 1) + "]/div"
                ).find_element_by_class_name("price-morning").text

                print("num_pmu : " + str(num_pmu) + " , cote_matin : " + str(cote_matin))

                if cote_matin != "NP":
                    runners[num_pmu] = float(cote_matin) * average_musique
                else:
                    runners[num_pmu] = average_musique
            except Exception as e:
                print('unable to locate the element : 1 _ ' + str(e))

        time.sleep(5)

        runners_sorted = sorted(runners.items(), key=lambda x: x[1], reverse=reverse)

        scoring_runners = {}

        i = 1

        for runner in runners_sorted:
            scoring_runners[runner[0]] = i

            i += 1

        time.sleep(5)

        browser.quit()

        print(scoring_runners)

    # musique from unibet x nombre_courses : ok
    def test_scoring_the_runners_by_musique_from_unibet_x_nombre_courses(self):
        print("test_scoring_the_runners_by_musique_from_unibet_x_nombre_courses")

        reverse = False

        url = global_url

        warnings.filterwarnings(action="ignore", message="unclosed", category=ResourceWarning)

        # with Firefox
        options = Options()
        options.headless = True
        browser = webdriver.Firefox(executable_path='..\\geckodriver.exe', options=options)

        time.sleep(10)

        try:
            # maximize window
            browser.maximize_window()

            time.sleep(5)

            # open
            browser.get(url)

            time.sleep(20)

            number_of_racers = int(
                browser.find_element_by_xpath(
                    "//p[@class='race-meta ui-mainview-block']"
                ).text.lower().split(" - ")[3].replace(' partants', '')
            )

            participant_key = 'nombreCourses'

            url_unibet_race = global_url

            today = date.today()

            d1 = today.strftime("%d%m%Y")

            reunion = url_unibet_race.replace("https://www.unibet.fr/turf/race/", "").replace(
                today.strftime("%d-%m-%Y") + "-", "").replace("-", "")[:2]

            course = url_unibet_race.replace("https://www.unibet.fr/turf/race/", "").replace(
                today.strftime("%d-%m-%Y") + "-", "").replace("-", "")[2:4]

            url = "https://offline.turfinfo.api.pmu.fr/rest/client/1/programme/" \
                  + d1 + "/" \
                  + reunion + "/" \
                  + course + "/participants"

            headers = {
                "Accept": "application/json",
                'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103'
            }

            rt = RequestsTor()

            response = rt.get(url, headers=headers)

            runners = {}

            chevaux = []

            for participant in response.json()['participants']:
                if participant_key in participant:
                    criteria = int(participant[participant_key])

                    chevaux.append(criteria)

            musiques = []

            for i in range(1, number_of_racers + 1):
                num_pmu = browser.find_element_by_xpath(
                    "/html/body/div/div[2]/div[5]/div/div/section/div/div/div/div/div/div/div/div[2]/div/div[3]/"
                    "ul[2]/li/div/div[2]/ul/li[" + str(i + 1) + "]/div/div[1]/span"
                ).text

                try:
                    musique = browser.find_element_by_xpath(
                        "/html/body/div[1]/div[2]/div[5]/div/div/section/div/div/div/div/div/div/div/div[2]/div/div[3]"
                        "/ul[2]/li/div/div[2]/ul/li[" + str(i + 1) + "]/div"
                    ).find_element_by_class_name("musique") \
                        .text \
                        .replace('a', '') \
                        .replace('m', '') \
                        .replace('D', '') \
                        .replace('Q', '') \
                        .replace('R', '') \
                        .replace('A', '') \
                        .replace('p', '') \
                        .replace('s', '') \
                        .replace('h', '') \
                        .replace('c', '') \
                        .replace('T', '') \
                        .replace(' ', '') \
                        .replace('(21)', '') \
                        .replace('(20)', '') \
                        .replace('(19)', '') \
                        .replace('(18)', '') \
                        .replace('(17)', '')

                    print("num_pmu : " + str(num_pmu) + " , musique : " + str(musique))

                    average = 0

                    for i1 in range(0, len(musique)):
                        average += int(musique[i1])

                    average_musique = average / len(musique)

                    musiques.append(average_musique)
                except Exception as e:
                    print('unable to locate the element : 1 _ ' + str(e))

            time.sleep(5)

            for i in range(1, number_of_racers + 1):
                try:
                    num_pmu = browser.find_element_by_xpath(
                        "/html/body/div/div[2]/div[5]/div/div/section/div/div/div/div/div/div/div/div[2]/div/div[3]/"
                        "ul[2]/li/div/div[2]/ul/li[" + str(i + 1) + "]/div/div[1]/span"
                    ).text

                    runners[num_pmu] = chevaux[i - 1] * musiques[i - 1]
                except Exception as e:
                    print('error : ' + str(e))

            runners_sorted = sorted(runners.items(), key=lambda x: x[1], reverse=reverse)

            scoring_runners = {}

            i = 1

            for runner in runners_sorted:
                scoring_runners[runner[0]] = i

                i += 1

            time.sleep(5)

            browser.quit()

            print(scoring_runners)
        except Exception as e:
            print('error 1 : ' + str(e))

            browser.quit()


class UnitTestsSupervisedLearningPMUV1(unittest.TestCase):
    # number of characters from clean musique from pmu : ok
    def test_scoring_the_runners_by_number_of_characters_from_clean_musique_from_pmu_with_dark_web(self):
        print("test_scoring_the_runners_by_number_of_characters_from_clean_musique_from_pmu_with_dark_web")

        reverse = True

        participant_key = 'musique'

        url_unibet_race = global_url

        today = date.today()

        d1 = today.strftime("%d%m%Y")

        reunion = url_unibet_race.replace("https://www.unibet.fr/turf/race/", "").replace(today.strftime("%d-%m-%Y") + "-", "").replace("-", "")[:2]

        course = url_unibet_race.replace("https://www.unibet.fr/turf/race/", "").replace(today.strftime("%d-%m-%Y") + "-", "").replace("-", "")[2:4]

        url = "https://offline.turfinfo.api.pmu.fr/rest/client/1/programme/" \
              + d1 + "/" \
              + reunion + "/" \
              + course + "/participants"

        headers = {
            "Accept": "application/json",
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103'
        }

        rt = RequestsTor()

        response = rt.get(url, headers=headers)

        response_pmu = response.json()['participants']

        runners = {}

        for participant in response_pmu:
            num_pmu = str(participant['numPmu'])

            if participant_key in participant:
                criteria = str(participant[participant_key]) \
                    .replace('D', '0')\
                    .replace('Q', '0') \
                    .replace('R', '0') \
                    .replace('A', '0') \
                    .replace('T', '0') \
                    .replace('(21)', '')\
                    .replace('(20)', '')\
                    .replace('(19)', '')\
                    .replace('(18)', '')\
                    .replace('(17)', '') \
                    .replace('a', '') \
                    .replace('m', '') \
                    .replace('s', '') \
                    .replace('c', '') \
                    .replace('p', '') \
                    .replace('h', '')

                number_of_characters_in_musique = len(criteria)

                runners[num_pmu] = number_of_characters_in_musique
            else:
                runners[num_pmu] = 1

        runners_sorted = sorted(runners.items(), key=lambda x: x[1], reverse=reverse)

        scoring_runners = {}

        i = 1

        for runner in runners_sorted:
            scoring_runners[runner[0]] = i

            i += 1

        print(scoring_runners)

    # number of characters from clean musique from unibet : ok
    def test_scoring_the_runners_by_number_of_characters_from_clean_musique_from_unibet_with_dark_web(self):
        print("test_scoring_the_runners_by_number_of_characters_from_clean_musique_from_unibet_with_dark_web")

        reverse = True

        url = global_url

        warnings.filterwarnings(action="ignore", message="unclosed", category=ResourceWarning)

        # with Firefox
        browser = webdriver.Firefox(executable_path='..\\geckodriver.exe')

        time.sleep(10)

        # maximize window
        browser.maximize_window()

        time.sleep(5)

        # open
        browser.get(url)

        time.sleep(20)

        number_of_racers = int(
            browser.find_element_by_xpath(
                "//p[@class='race-meta ui-mainview-block']"
            ).text.lower().split(" - ")[3].replace(' partants', '')
        )

        runners = {}

        for i in range(1, number_of_racers + 1):
            num_pmu = browser.find_element_by_xpath(
                "/html/body/div/div[2]/div[5]/div/div/section/div/div/div/div/div/div/div/div[2]/div/div[3]/"
                "ul[2]/li/div/div[2]/ul/li[" + str(i + 1) + "]/div/div[1]/span"
            ).text

            try:
                musique = browser.find_element_by_xpath(
                    "/html/body/div[1]/div[2]/div[5]/div/div/section/div/div/div/div/div/div/div/div[2]/div/div[3]"
                    "/ul[2]/li/div/div[2]/ul/li[" + str(i + 1) + "]/div"
                ).find_element_by_class_name("musique")\
                    .text \
                    .replace('a', '') \
                    .replace('m', '') \
                    .replace('D', '') \
                    .replace('Q', '') \
                    .replace('R', '') \
                    .replace('A', '') \
                    .replace('p', '') \
                    .replace('s', '') \
                    .replace('h', '') \
                    .replace('c', '') \
                    .replace('T', '') \
                    .replace(' ', '') \
                    .replace('(21)', '') \
                    .replace('(20)', '') \
                    .replace('(19)', '') \
                    .replace('(18)', '') \
                    .replace('(17)', '')

                number_of_characters_in_musique = len(musique)

                runners[num_pmu] = number_of_characters_in_musique
            except Exception as e:
                print('unable to locate the element : 1 _ ' + str(e))

        time.sleep(5)

        runners_sorted = sorted(runners.items(), key=lambda x: x[1], reverse=reverse)

        scoring_runners = {}

        i = 1

        for runner in runners_sorted:
            scoring_runners[runner[0]] = i

            i += 1

        time.sleep(5)

        browser.close()

        print(scoring_runners)

    # number of Q from musique from unibet
    def test_scoring_the_runners_by_number_of_capital_q_from_musique_from_unibet(self):
        print("test_scoring_the_runners_by_number_of_capital_r_from_musique_from_unibet")

        this_character = "Q"

        reverse = False

        url = global_url

        warnings.filterwarnings(action="ignore", message="unclosed", category=ResourceWarning)

        # with Firefox
        browser = webdriver.Firefox(executable_path='..\\geckodriver.exe')

        time.sleep(10)

        # maximize window
        browser.maximize_window()

        time.sleep(5)

        # open
        browser.get(url)

        time.sleep(20)

        number_of_racers = int(
            browser.find_element_by_xpath(
                "//p[@class='race-meta ui-mainview-block']"
            ).text.lower().split(" - ")[3].replace(' partants', '')
        )

        runners = {}

        for i in range(1, number_of_racers + 1):
            num_pmu = browser.find_element_by_xpath(
                "/html/body/div/div[2]/div[5]/div/div/section/div/div/div/div/div/div/div/div[2]/div/div[3]/"
                "ul[2]/li/div/div[2]/ul/li[" + str(i + 1) + "]/div/div[1]/span"
            ).text

            try:
                musique = browser.find_element_by_xpath(
                    "/html/body/div[1]/div[2]/div[5]/div/div/section/div/div/div/div/div/div/div/div[2]/div/div[3]"
                    "/ul[2]/li/div/div[2]/ul/li[" + str(i + 1) + "]/div"
                ).find_element_by_class_name("musique").text

                number_of_disqualified = musique.count(this_character)

                runners[num_pmu] = number_of_disqualified
            except Exception as e:
                print('unable to locate the element : 1 _ ' + str(e))

        time.sleep(5)

        runners_sorted = sorted(runners.items(), key=lambda x: x[1], reverse=reverse)

        scoring_runners = {}

        i = 1

        for runner in runners_sorted:
            scoring_runners[runner[0]] = i

            i += 1

        time.sleep(5)

        browser.close()

        print(scoring_runners)

    # number of Q from musique from pmu
    def test_scoring_the_runners_by_number_of_capital_q_from_musique_from_pmu_with_dark_web(self):
        print("test_scoring_the_runners_by_number_of_capital_r_from_musique_from_pmu_with_dark_web")

        this_character = "Q"

        reverse = False

        participant_key = 'musique'

        url_unibet_race = global_url

        today = date.today()

        d1 = today.strftime("%d%m%Y")

        reunion = url_unibet_race.replace("https://www.unibet.fr/turf/race/", "").replace(today.strftime("%d-%m-%Y") + "-", "").replace("-", "")[:2]

        course = url_unibet_race.replace("https://www.unibet.fr/turf/race/", "").replace(today.strftime("%d-%m-%Y") + "-", "").replace("-", "")[2:4]

        url = "https://offline.turfinfo.api.pmu.fr/rest/client/1/programme/" \
              + d1 + "/" \
              + reunion + "/" \
              + course + "/participants"

        headers = {
            "Accept": "application/json",
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103'
        }

        rt = RequestsTor()

        response = rt.get(url, headers=headers)

        runners = {}

        for participant in response.json()['participants']:
            num_pmu = str(participant['numPmu'])

            if participant_key in participant:
                criteria = str(participant[participant_key])

                number_of_disqualified = criteria.count(this_character)

                runners[num_pmu] = number_of_disqualified
            else:
                runners[num_pmu] = 1

        runners_sorted = sorted(runners.items(), key=lambda x: x[1], reverse=reverse)

        scoring_runners = {}

        i = 1

        for runner in runners_sorted:
            scoring_runners[runner[0]] = i

            i += 1

        print(scoring_runners)

    # number of R from musique from unibet
    def test_scoring_the_runners_by_number_of_capital_r_from_musique_from_unibet(self):
        print("test_scoring_the_runners_by_number_of_capital_r_from_musique_from_unibet")

        this_character = "R"

        reverse = False

        url = global_url

        warnings.filterwarnings(action="ignore", message="unclosed", category=ResourceWarning)

        # with Firefox
        browser = webdriver.Firefox(executable_path='..\\geckodriver.exe')

        time.sleep(10)

        # maximize window
        browser.maximize_window()

        time.sleep(5)

        # open
        browser.get(url)

        time.sleep(20)

        number_of_racers = int(
            browser.find_element_by_xpath(
                "//p[@class='race-meta ui-mainview-block']"
            ).text.lower().split(" - ")[3].replace(' partants', '')
        )

        runners = {}

        for i in range(1, number_of_racers + 1):
            num_pmu = browser.find_element_by_xpath(
                "/html/body/div/div[2]/div[5]/div/div/section/div/div/div/div/div/div/div/div[2]/div/div[3]/"
                "ul[2]/li/div/div[2]/ul/li[" + str(i + 1) + "]/div/div[1]/span"
            ).text

            try:
                musique = browser.find_element_by_xpath(
                    "/html/body/div[1]/div[2]/div[5]/div/div/section/div/div/div/div/div/div/div/div[2]/div/div[3]"
                    "/ul[2]/li/div/div[2]/ul/li[" + str(i + 1) + "]/div"
                ).find_element_by_class_name("musique").text

                number_of_disqualified = musique.count(this_character)

                runners[num_pmu] = number_of_disqualified
            except Exception as e:
                print('unable to locate the element : 1 _ ' + str(e))

        time.sleep(5)

        runners_sorted = sorted(runners.items(), key=lambda x: x[1], reverse=reverse)

        scoring_runners = {}

        i = 1

        for runner in runners_sorted:
            scoring_runners[runner[0]] = i

            i += 1

        time.sleep(5)

        browser.close()

        print(scoring_runners)

    # number of R from musique from pmu
    def test_scoring_the_runners_by_number_of_capital_r_from_musique_from_pmu_with_dark_web(self):
        print("test_scoring_the_runners_by_number_of_capital_r_from_musique_from_pmu_with_dark_web")

        this_character = "R"

        reverse = False

        participant_key = 'musique'

        url_unibet_race = global_url

        today = date.today()

        d1 = today.strftime("%d%m%Y")

        reunion = url_unibet_race.replace("https://www.unibet.fr/turf/race/", "").replace(today.strftime("%d-%m-%Y") + "-", "").replace("-", "")[:2]

        course = url_unibet_race.replace("https://www.unibet.fr/turf/race/", "").replace(today.strftime("%d-%m-%Y") + "-", "").replace("-", "")[2:4]

        url = "https://offline.turfinfo.api.pmu.fr/rest/client/1/programme/" \
              + d1 + "/" \
              + reunion + "/" \
              + course + "/participants"

        headers = {
            "Accept": "application/json",
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103'
        }

        rt = RequestsTor()

        response = rt.get(url, headers=headers)

        runners = {}

        for participant in response.json()['participants']:
            num_pmu = str(participant['numPmu'])

            if participant_key in participant:
                criteria = str(participant[participant_key])

                number_of_disqualified = criteria.count(this_character)

                runners[num_pmu] = number_of_disqualified
            else:
                runners[num_pmu] = 1

        runners_sorted = sorted(runners.items(), key=lambda x: x[1], reverse=reverse)

        scoring_runners = {}

        i = 1

        for runner in runners_sorted:
            scoring_runners[runner[0]] = i

            i += 1

        print(scoring_runners)

    # number of A from musique from unibet
    def test_scoring_the_runners_by_number_of_capital_a_from_musique_from_unibet(self):
        print("test_scoring_the_runners_by_number_of_capital_a_from_musique_from_unibet")

        this_character = "A"

        reverse = False

        url = global_url

        warnings.filterwarnings(action="ignore", message="unclosed", category=ResourceWarning)

        # with Firefox
        browser = webdriver.Firefox(executable_path='..\\geckodriver.exe')

        time.sleep(10)

        # maximize window
        browser.maximize_window()

        time.sleep(5)

        # open
        browser.get(url)

        time.sleep(20)

        number_of_racers = int(
            browser.find_element_by_xpath(
                "//p[@class='race-meta ui-mainview-block']"
            ).text.lower().split(" - ")[3].replace(' partants', '')
        )

        runners = {}

        for i in range(1, number_of_racers + 1):
            num_pmu = browser.find_element_by_xpath(
                "/html/body/div/div[2]/div[5]/div/div/section/div/div/div/div/div/div/div/div[2]/div/div[3]/"
                "ul[2]/li/div/div[2]/ul/li[" + str(i + 1) + "]/div/div[1]/span"
            ).text

            try:
                musique = browser.find_element_by_xpath(
                    "/html/body/div[1]/div[2]/div[5]/div/div/section/div/div/div/div/div/div/div/div[2]/div/div[3]"
                    "/ul[2]/li/div/div[2]/ul/li[" + str(i + 1) + "]/div"
                ).find_element_by_class_name("musique").text

                number_of_disqualified = musique.count(this_character)

                runners[num_pmu] = number_of_disqualified
            except Exception as e:
                print('unable to locate the element : 1 _ ' + str(e))

        time.sleep(5)

        runners_sorted = sorted(runners.items(), key=lambda x: x[1], reverse=reverse)

        scoring_runners = {}

        i = 1

        for runner in runners_sorted:
            scoring_runners[runner[0]] = i

            i += 1

        time.sleep(5)

        browser.close()

        print(scoring_runners)

    # number of A from musique from pmu
    def test_scoring_the_runners_by_number_of_capital_a_from_musique_from_pmu_with_dark_web(self):
        print("test_scoring_the_runners_by_number_of_capital_a_from_musique_from_pmu_with_dark_web")

        this_character = "A"

        reverse = False

        participant_key = 'musique'

        url_unibet_race = global_url

        today = date.today()

        d1 = today.strftime("%d%m%Y")

        reunion = url_unibet_race.replace("https://www.unibet.fr/turf/race/", "").replace(today.strftime("%d-%m-%Y") + "-", "").replace("-", "")[:2]

        course = url_unibet_race.replace("https://www.unibet.fr/turf/race/", "").replace(today.strftime("%d-%m-%Y") + "-", "").replace("-", "")[2:4]

        url = "https://offline.turfinfo.api.pmu.fr/rest/client/1/programme/" \
              + d1 + "/" \
              + reunion + "/" \
              + course + "/participants"

        headers = {
            "Accept": "application/json",
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103'
        }

        rt = RequestsTor()

        response = rt.get(url, headers=headers)

        runners = {}

        for participant in response.json()['participants']:
            num_pmu = str(participant['numPmu'])

            if participant_key in participant:
                criteria = str(participant[participant_key])

                number_of_disqualified = criteria.count(this_character)

                runners[num_pmu] = number_of_disqualified
            else:
                runners[num_pmu] = 1

        runners_sorted = sorted(runners.items(), key=lambda x: x[1], reverse=reverse)

        scoring_runners = {}

        i = 1

        for runner in runners_sorted:
            scoring_runners[runner[0]] = i

            i += 1

        print(scoring_runners)

    # number of T from musique from unibet
    def test_scoring_the_runners_by_number_of_capital_t_from_musique_from_unibet(self):
        print("test_scoring_the_runners_by_number_of_capital_t_from_musique_from_unibet")

        this_character = "T"

        reverse = False

        url = global_url

        warnings.filterwarnings(action="ignore", message="unclosed", category=ResourceWarning)

        # with Firefox
        browser = webdriver.Firefox(executable_path='..\\geckodriver.exe')

        time.sleep(10)

        # maximize window
        browser.maximize_window()

        time.sleep(5)

        # open
        browser.get(url)

        time.sleep(20)

        number_of_racers = int(
            browser.find_element_by_xpath(
                "//p[@class='race-meta ui-mainview-block']"
            ).text.lower().split(" - ")[3].replace(' partants', '')
        )

        runners = {}

        for i in range(1, number_of_racers + 1):
            num_pmu = browser.find_element_by_xpath(
                "/html/body/div/div[2]/div[5]/div/div/section/div/div/div/div/div/div/div/div[2]/div/div[3]/"
                "ul[2]/li/div/div[2]/ul/li[" + str(i + 1) + "]/div/div[1]/span"
            ).text

            try:
                musique = browser.find_element_by_xpath(
                    "/html/body/div[1]/div[2]/div[5]/div/div/section/div/div/div/div/div/div/div/div[2]/div/div[3]"
                    "/ul[2]/li/div/div[2]/ul/li[" + str(i + 1) + "]/div"
                ).find_element_by_class_name("musique").text

                number_of_disqualified = musique.count(this_character)

                runners[num_pmu] = number_of_disqualified
            except Exception as e:
                print('unable to locate the element : 1 _ ' + str(e))

        time.sleep(5)

        runners_sorted = sorted(runners.items(), key=lambda x: x[1], reverse=reverse)

        scoring_runners = {}

        i = 1

        for runner in runners_sorted:
            scoring_runners[runner[0]] = i

            i += 1

        time.sleep(5)

        browser.close()

        print(scoring_runners)

    # number of T from musique from pmu
    def test_scoring_the_runners_by_number_of_capital_t_from_musique_from_pmu_with_dark_web(self):
        print("test_scoring_the_runners_by_number_of_capital_t_from_musique_from_pmu_with_dark_web")

        this_character = "T"

        reverse = False

        participant_key = 'musique'

        url_unibet_race = global_url

        today = date.today()

        d1 = today.strftime("%d%m%Y")

        reunion = url_unibet_race.replace("https://www.unibet.fr/turf/race/", "").replace(today.strftime("%d-%m-%Y") + "-", "").replace("-", "")[:2]

        course = url_unibet_race.replace("https://www.unibet.fr/turf/race/", "").replace(today.strftime("%d-%m-%Y") + "-", "").replace("-", "")[2:4]

        url = "https://offline.turfinfo.api.pmu.fr/rest/client/1/programme/" \
              + d1 + "/" \
              + reunion + "/" \
              + course + "/participants"

        headers = {
            "Accept": "application/json",
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103'
        }

        rt = RequestsTor()

        response = rt.get(url, headers=headers)

        runners = {}

        for participant in response.json()['participants']:
            num_pmu = str(participant['numPmu'])

            if participant_key in participant:
                criteria = str(participant[participant_key])

                number_of_disqualified = criteria.count(this_character)

                runners[num_pmu] = number_of_disqualified
            else:
                runners[num_pmu] = 1

        runners_sorted = sorted(runners.items(), key=lambda x: x[1], reverse=reverse)

        scoring_runners = {}

        i = 1

        for runner in runners_sorted:
            scoring_runners[runner[0]] = i

            i += 1

        print(scoring_runners)

    # number of s from musique from unibet
    def test_scoring_the_runners_by_number_of_s_from_musique_from_unibet(self):
        print("test_scoring_the_runners_by_number_of_s_from_musique_from_unibet")

        this_character = "s"

        reverse = True

        url = global_url

        warnings.filterwarnings(action="ignore", message="unclosed", category=ResourceWarning)

        # with Firefox
        browser = webdriver.Firefox(executable_path='..\\geckodriver.exe')

        time.sleep(10)

        # maximize window
        browser.maximize_window()

        time.sleep(5)

        # open
        browser.get(url)

        time.sleep(20)

        number_of_racers = int(
            browser.find_element_by_xpath(
                "//p[@class='race-meta ui-mainview-block']"
            ).text.lower().split(" - ")[3].replace(' partants', '')
        )

        runners = {}

        for i in range(1, number_of_racers + 1):
            num_pmu = browser.find_element_by_xpath(
                "/html/body/div/div[2]/div[5]/div/div/section/div/div/div/div/div/div/div/div[2]/div/div[3]/"
                "ul[2]/li/div/div[2]/ul/li[" + str(i + 1) + "]/div/div[1]/span"
            ).text

            try:
                musique = browser.find_element_by_xpath(
                    "/html/body/div[1]/div[2]/div[5]/div/div/section/div/div/div/div/div/div/div/div[2]/div/div[3]"
                    "/ul[2]/li/div/div[2]/ul/li[" + str(i + 1) + "]/div"
                ).find_element_by_class_name("musique").text

                number_of_disqualified = musique.count(this_character)

                runners[num_pmu] = number_of_disqualified
            except Exception as e:
                print('unable to locate the element : 1 _ ' + str(e))

        time.sleep(5)

        runners_sorted = sorted(runners.items(), key=lambda x: x[1], reverse=reverse)

        scoring_runners = {}

        i = 1

        for runner in runners_sorted:
            scoring_runners[runner[0]] = i

            i += 1

        time.sleep(5)

        browser.close()

        print(scoring_runners)

    # number of s from musique from pmu
    def test_scoring_the_runners_by_number_of_s_from_musique_from_pmu_with_dark_web(self):
        print("test_scoring_the_runners_by_number_of_s_from_musique_from_pmu_with_dark_web")

        this_character = "s"

        reverse = True

        participant_key = 'musique'

        url_unibet_race = global_url

        today = date.today()

        d1 = today.strftime("%d%m%Y")

        reunion = url_unibet_race.replace("https://www.unibet.fr/turf/race/", "").replace(today.strftime("%d-%m-%Y") + "-", "").replace("-", "")[:2]

        course = url_unibet_race.replace("https://www.unibet.fr/turf/race/", "").replace(today.strftime("%d-%m-%Y") + "-", "").replace("-", "")[2:4]

        url = "https://offline.turfinfo.api.pmu.fr/rest/client/1/programme/" \
              + d1 + "/" \
              + reunion + "/" \
              + course + "/participants"

        headers = {
            "Accept": "application/json",
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103'
        }

        rt = RequestsTor()

        response = rt.get(url, headers=headers)

        runners = {}

        for participant in response.json()['participants']:
            num_pmu = str(participant['numPmu'])

            if participant_key in participant:
                criteria = str(participant[participant_key])

                number_of_disqualified = criteria.count(this_character)

                runners[num_pmu] = number_of_disqualified
            else:
                runners[num_pmu] = 1

        runners_sorted = sorted(runners.items(), key=lambda x: x[1], reverse=reverse)

        scoring_runners = {}

        i = 1

        for runner in runners_sorted:
            scoring_runners[runner[0]] = i

            i += 1

        print(scoring_runners)

    # number of c from musique from unibet
    def test_scoring_the_runners_by_number_of_c_from_musique_from_unibet(self):
        print("test_scoring_the_runners_by_number_of_c_from_musique_from_unibet")

        this_character = "c"

        reverse = True

        url = global_url

        warnings.filterwarnings(action="ignore", message="unclosed", category=ResourceWarning)

        # with Firefox
        browser = webdriver.Firefox(executable_path='..\\geckodriver.exe')

        time.sleep(10)

        # maximize window
        browser.maximize_window()

        time.sleep(5)

        # open
        browser.get(url)

        time.sleep(20)

        number_of_racers = int(
            browser.find_element_by_xpath(
                "//p[@class='race-meta ui-mainview-block']"
            ).text.lower().split(" - ")[3].replace(' partants', '')
        )

        runners = {}

        for i in range(1, number_of_racers + 1):
            num_pmu = browser.find_element_by_xpath(
                "/html/body/div/div[2]/div[5]/div/div/section/div/div/div/div/div/div/div/div[2]/div/div[3]/"
                "ul[2]/li/div/div[2]/ul/li[" + str(i + 1) + "]/div/div[1]/span"
            ).text

            try:
                musique = browser.find_element_by_xpath(
                    "/html/body/div[1]/div[2]/div[5]/div/div/section/div/div/div/div/div/div/div/div[2]/div/div[3]"
                    "/ul[2]/li/div/div[2]/ul/li[" + str(i + 1) + "]/div"
                ).find_element_by_class_name("musique").text

                number_of_disqualified = musique.count(this_character)

                runners[num_pmu] = number_of_disqualified
            except Exception as e:
                print('unable to locate the element : 1 _ ' + str(e))

        time.sleep(5)

        runners_sorted = sorted(runners.items(), key=lambda x: x[1], reverse=reverse)

        scoring_runners = {}

        i = 1

        for runner in runners_sorted:
            scoring_runners[runner[0]] = i

            i += 1

        time.sleep(5)

        browser.close()

        print(scoring_runners)

    # number of c from musique from pmu
    def test_scoring_the_runners_by_number_of_c_from_musique_from_pmu_with_dark_web(self):
        print("test_scoring_the_runners_by_number_of_c_from_musique_from_pmu_with_dark_web")

        this_character = "c"

        reverse = True

        participant_key = 'musique'

        url_unibet_race = global_url

        today = date.today()

        d1 = today.strftime("%d%m%Y")

        reunion = url_unibet_race.replace("https://www.unibet.fr/turf/race/", "").replace(today.strftime("%d-%m-%Y") + "-", "").replace("-", "")[:2]

        course = url_unibet_race.replace("https://www.unibet.fr/turf/race/", "").replace(today.strftime("%d-%m-%Y") + "-", "").replace("-", "")[2:4]

        url = "https://offline.turfinfo.api.pmu.fr/rest/client/1/programme/" \
              + d1 + "/" \
              + reunion + "/" \
              + course + "/participants"

        headers = {
            "Accept": "application/json",
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103'
        }

        rt = RequestsTor()

        response = rt.get(url, headers=headers)

        runners = {}

        for participant in response.json()['participants']:
            num_pmu = str(participant['numPmu'])

            if participant_key in participant:
                criteria = str(participant[participant_key])

                number_of_disqualified = criteria.count(this_character)

                runners[num_pmu] = number_of_disqualified
            else:
                runners[num_pmu] = 1

        runners_sorted = sorted(runners.items(), key=lambda x: x[1], reverse=reverse)

        scoring_runners = {}

        i = 1

        for runner in runners_sorted:
            scoring_runners[runner[0]] = i

            i += 1

        print(scoring_runners)

    # number of h from musique from unibet
    def test_scoring_the_runners_by_number_of_h_from_musique_from_unibet(self):
        print("test_scoring_the_runners_by_number_of_h_from_musique_from_unibet")

        this_character = "h"

        reverse = True

        url = global_url

        warnings.filterwarnings(action="ignore", message="unclosed", category=ResourceWarning)

        # with Firefox
        browser = webdriver.Firefox(executable_path='..\\geckodriver.exe')

        time.sleep(10)

        # maximize window
        browser.maximize_window()

        time.sleep(5)

        # open
        browser.get(url)

        time.sleep(20)

        number_of_racers = int(
            browser.find_element_by_xpath(
                "//p[@class='race-meta ui-mainview-block']"
            ).text.lower().split(" - ")[3].replace(' partants', '')
        )

        runners = {}

        for i in range(1, number_of_racers + 1):
            num_pmu = browser.find_element_by_xpath(
                "/html/body/div/div[2]/div[5]/div/div/section/div/div/div/div/div/div/div/div[2]/div/div[3]/"
                "ul[2]/li/div/div[2]/ul/li[" + str(i + 1) + "]/div/div[1]/span"
            ).text

            try:
                musique = browser.find_element_by_xpath(
                    "/html/body/div[1]/div[2]/div[5]/div/div/section/div/div/div/div/div/div/div/div[2]/div/div[3]"
                    "/ul[2]/li/div/div[2]/ul/li[" + str(i + 1) + "]/div"
                ).find_element_by_class_name("musique").text

                number_of_disqualified = musique.count(this_character)

                runners[num_pmu] = number_of_disqualified
            except Exception as e:
                print('unable to locate the element : 1 _ ' + str(e))

        time.sleep(5)

        runners_sorted = sorted(runners.items(), key=lambda x: x[1], reverse=reverse)

        scoring_runners = {}

        i = 1

        for runner in runners_sorted:
            scoring_runners[runner[0]] = i

            i += 1

        time.sleep(5)

        browser.close()

        print(scoring_runners)

    # number of h from musique from pmu
    def test_scoring_the_runners_by_number_of_h_from_musique_from_pmu_with_dark_web(self):
        print("test_scoring_the_runners_by_number_of_h_from_musique_from_pmu_with_dark_web")

        this_character = "h"

        reverse = True

        participant_key = 'musique'

        url_unibet_race = global_url

        today = date.today()

        d1 = today.strftime("%d%m%Y")

        reunion = url_unibet_race.replace("https://www.unibet.fr/turf/race/", "").replace(today.strftime("%d-%m-%Y") + "-", "").replace("-", "")[:2]

        course = url_unibet_race.replace("https://www.unibet.fr/turf/race/", "").replace(today.strftime("%d-%m-%Y") + "-", "").replace("-", "")[2:4]

        url = "https://offline.turfinfo.api.pmu.fr/rest/client/1/programme/" \
              + d1 + "/" \
              + reunion + "/" \
              + course + "/participants"

        headers = {
            "Accept": "application/json",
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103'
        }

        rt = RequestsTor()

        response = rt.get(url, headers=headers)

        runners = {}

        for participant in response.json()['participants']:
            num_pmu = str(participant['numPmu'])

            if participant_key in participant:
                criteria = str(participant[participant_key])

                number_of_disqualified = criteria.count(this_character)

                runners[num_pmu] = number_of_disqualified
            else:
                runners[num_pmu] = 1

        runners_sorted = sorted(runners.items(), key=lambda x: x[1], reverse=reverse)

        scoring_runners = {}

        i = 1

        for runner in runners_sorted:
            scoring_runners[runner[0]] = i

            i += 1

        print(scoring_runners)

    # number of m from musique from unibet
    def test_scoring_the_runners_by_number_of_m_from_musique_from_unibet(self):
        print("test_scoring_the_runners_by_number_of_a_from_musique_from_unibet")

        this_character = "m"

        reverse = True

        url = global_url

        warnings.filterwarnings(action="ignore", message="unclosed", category=ResourceWarning)

        # with Firefox
        browser = webdriver.Firefox(executable_path='..\\geckodriver.exe')

        time.sleep(10)

        # maximize window
        browser.maximize_window()

        time.sleep(5)

        # open
        browser.get(url)

        time.sleep(20)

        number_of_racers = int(
            browser.find_element_by_xpath(
                "//p[@class='race-meta ui-mainview-block']"
            ).text.lower().split(" - ")[3].replace(' partants', '')
        )

        runners = {}

        for i in range(1, number_of_racers + 1):
            num_pmu = browser.find_element_by_xpath(
                "/html/body/div/div[2]/div[5]/div/div/section/div/div/div/div/div/div/div/div[2]/div/div[3]/"
                "ul[2]/li/div/div[2]/ul/li[" + str(i + 1) + "]/div/div[1]/span"
            ).text

            try:
                musique = browser.find_element_by_xpath(
                    "/html/body/div[1]/div[2]/div[5]/div/div/section/div/div/div/div/div/div/div/div[2]/div/div[3]"
                    "/ul[2]/li/div/div[2]/ul/li[" + str(i + 1) + "]/div"
                ).find_element_by_class_name("musique").text

                number_of_disqualified = musique.count(this_character)

                runners[num_pmu] = number_of_disqualified
            except Exception as e:
                print('unable to locate the element : 1 _ ' + str(e))

        time.sleep(5)

        runners_sorted = sorted(runners.items(), key=lambda x: x[1], reverse=reverse)

        scoring_runners = {}

        i = 1

        for runner in runners_sorted:
            scoring_runners[runner[0]] = i

            i += 1

        time.sleep(5)

        browser.close()

        print(scoring_runners)

    # number of m from musique from pmu
    def test_scoring_the_runners_by_number_of_m_from_musique_from_pmu_with_dark_web(self):
        print("test_scoring_the_runners_by_number_of_a_from_musique_from_pmu_with_dark_web")

        this_character = "m"

        reverse = True

        participant_key = 'musique'

        url_unibet_race = global_url

        today = date.today()

        d1 = today.strftime("%d%m%Y")

        reunion = url_unibet_race.replace("https://www.unibet.fr/turf/race/", "").replace(today.strftime("%d-%m-%Y") + "-", "").replace("-", "")[:2]

        course = url_unibet_race.replace("https://www.unibet.fr/turf/race/", "").replace(today.strftime("%d-%m-%Y") + "-", "").replace("-", "")[2:4]

        url = "https://offline.turfinfo.api.pmu.fr/rest/client/1/programme/" \
              + d1 + "/" \
              + reunion + "/" \
              + course + "/participants"

        headers = {
            "Accept": "application/json",
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103'
        }

        rt = RequestsTor()

        response = rt.get(url, headers=headers)

        runners = {}

        for participant in response.json()['participants']:
            num_pmu = str(participant['numPmu'])

            if participant_key in participant:
                criteria = str(participant[participant_key])

                number_of_disqualified = criteria.count(this_character)

                runners[num_pmu] = number_of_disqualified
            else:
                runners[num_pmu] = 1

        runners_sorted = sorted(runners.items(), key=lambda x: x[1], reverse=reverse)

        scoring_runners = {}

        i = 1

        for runner in runners_sorted:
            scoring_runners[runner[0]] = i

            i += 1

        print(scoring_runners)

    # number of a from musique from unibet
    def test_scoring_the_runners_by_number_of_a_from_musique_from_unibet(self):
        print("test_scoring_the_runners_by_number_of_a_from_musique_from_unibet")

        this_character = "a"

        reverse = True

        url = global_url

        warnings.filterwarnings(action="ignore", message="unclosed", category=ResourceWarning)

        # with Firefox
        browser = webdriver.Firefox(executable_path='..\\geckodriver.exe')

        time.sleep(10)

        # maximize window
        browser.maximize_window()

        time.sleep(5)

        # open
        browser.get(url)

        time.sleep(20)

        number_of_racers = int(
            browser.find_element_by_xpath(
                "//p[@class='race-meta ui-mainview-block']"
            ).text.lower().split(" - ")[3].replace(' partants', '')
        )

        runners = {}

        for i in range(1, number_of_racers + 1):
            num_pmu = browser.find_element_by_xpath(
                "/html/body/div/div[2]/div[5]/div/div/section/div/div/div/div/div/div/div/div[2]/div/div[3]/"
                "ul[2]/li/div/div[2]/ul/li[" + str(i + 1) + "]/div/div[1]/span"
            ).text

            try:
                musique = browser.find_element_by_xpath(
                    "/html/body/div[1]/div[2]/div[5]/div/div/section/div/div/div/div/div/div/div/div[2]/div/div[3]"
                    "/ul[2]/li/div/div[2]/ul/li[" + str(i + 1) + "]/div"
                ).find_element_by_class_name("musique").text

                number_of_disqualified = musique.count(this_character)

                runners[num_pmu] = number_of_disqualified
            except Exception as e:
                print('unable to locate the element : 1 _ ' + str(e))

        time.sleep(5)

        runners_sorted = sorted(runners.items(), key=lambda x: x[1], reverse=reverse)

        scoring_runners = {}

        i = 1

        for runner in runners_sorted:
            scoring_runners[runner[0]] = i

            i += 1

        time.sleep(5)

        browser.close()

        print(scoring_runners)

    # number of a from musique from pmu
    def test_scoring_the_runners_by_number_of_a_from_musique_from_pmu_with_dark_web(self):
        print("test_scoring_the_runners_by_number_of_a_from_musique_from_pmu_with_dark_web")

        this_character = "a"

        reverse = True

        participant_key = 'musique'

        url_unibet_race = global_url

        today = date.today()

        d1 = today.strftime("%d%m%Y")

        reunion = url_unibet_race.replace("https://www.unibet.fr/turf/race/", "").replace(today.strftime("%d-%m-%Y") + "-", "").replace("-", "")[:2]

        course = url_unibet_race.replace("https://www.unibet.fr/turf/race/", "").replace(today.strftime("%d-%m-%Y") + "-", "").replace("-", "")[2:4]

        url = "https://offline.turfinfo.api.pmu.fr/rest/client/1/programme/" \
              + d1 + "/" \
              + reunion + "/" \
              + course + "/participants"

        headers = {
            "Accept": "application/json",
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103'
        }

        rt = RequestsTor()

        response = rt.get(url, headers=headers)

        runners = {}

        for participant in response.json()['participants']:
            num_pmu = str(participant['numPmu'])

            if participant_key in participant:
                criteria = str(participant[participant_key])

                number_of_disqualified = criteria.count(this_character)

                runners[num_pmu] = number_of_disqualified
            else:
                runners[num_pmu] = 1

        runners_sorted = sorted(runners.items(), key=lambda x: x[1], reverse=reverse)

        scoring_runners = {}

        i = 1

        for runner in runners_sorted:
            scoring_runners[runner[0]] = i

            i += 1

        print(scoring_runners)

    # number of p from musique from unibet
    def test_scoring_the_runners_by_number_of_p_from_musique_from_unibet(self):
        print("test_scoring_the_runners_by_number_of_p_from_musique_from_unibet")

        reverse = True

        url = global_url

        warnings.filterwarnings(action="ignore", message="unclosed", category=ResourceWarning)

        # with Firefox
        browser = webdriver.Firefox(executable_path='..\\geckodriver.exe')

        time.sleep(10)

        # maximize window
        browser.maximize_window()

        time.sleep(5)

        # open
        browser.get(url)

        time.sleep(20)

        number_of_racers = int(
            browser.find_element_by_xpath(
                "//p[@class='race-meta ui-mainview-block']"
            ).text.lower().split(" - ")[3].replace(' partants', '')
        )

        runners = {}

        for i in range(1, number_of_racers + 1):
            num_pmu = browser.find_element_by_xpath(
                "/html/body/div/div[2]/div[5]/div/div/section/div/div/div/div/div/div/div/div[2]/div/div[3]/"
                "ul[2]/li/div/div[2]/ul/li[" + str(i + 1) + "]/div/div[1]/span"
            ).text

            try:
                musique = browser.find_element_by_xpath(
                    "/html/body/div[1]/div[2]/div[5]/div/div/section/div/div/div/div/div/div/div/div[2]/div/div[3]"
                    "/ul[2]/li/div/div[2]/ul/li[" + str(i + 1) + "]/div"
                ).find_element_by_class_name("musique").text

                number_of_disqualified = musique.count("p")

                runners[num_pmu] = number_of_disqualified
            except Exception as e:
                print('unable to locate the element : 1 _ ' + str(e))

        time.sleep(5)

        runners_sorted = sorted(runners.items(), key=lambda x: x[1], reverse=reverse)

        scoring_runners = {}

        i = 1

        for runner in runners_sorted:
            scoring_runners[runner[0]] = i

            i += 1

        time.sleep(5)

        browser.close()

        print(scoring_runners)

    # number of p from musique from pmu
    def test_scoring_the_runners_by_number_of_p_from_musique_from_pmu_with_dark_web(self):
        print("test_scoring_the_runners_by_number_of_p_from_musique_from_pmu_with_dark_web")

        reverse = True

        participant_key = 'musique'

        url_unibet_race = global_url

        today = date.today()

        d1 = today.strftime("%d%m%Y")

        reunion = url_unibet_race.replace("https://www.unibet.fr/turf/race/", "").replace(today.strftime("%d-%m-%Y") + "-", "").replace("-", "")[:2]

        course = url_unibet_race.replace("https://www.unibet.fr/turf/race/", "").replace(today.strftime("%d-%m-%Y") + "-", "").replace("-", "")[2:4]

        url = "https://offline.turfinfo.api.pmu.fr/rest/client/1/programme/" \
              + d1 + "/" \
              + reunion + "/" \
              + course + "/participants"

        headers = {
            "Accept": "application/json",
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103'
        }

        rt = RequestsTor()

        response = rt.get(url, headers=headers)

        runners = {}

        for participant in response.json()['participants']:
            num_pmu = str(participant['numPmu'])

            if participant_key in participant:
                criteria = str(participant[participant_key])

                number_of_disqualified = criteria.count("p")

                runners[num_pmu] = number_of_disqualified
            else:
                runners[num_pmu] = 1

        runners_sorted = sorted(runners.items(), key=lambda x: x[1], reverse=reverse)

        scoring_runners = {}

        i = 1

        for runner in runners_sorted:
            scoring_runners[runner[0]] = i

            i += 1

        print(scoring_runners)


class UnitTestsSupervisedLearningPMUFinal(unittest.TestCase):
    # global_scoring_runners : ok
    def test_global_scoring_runners(self=None):
        print('starting')

        global_scoring_runners_sorted = PMUFinal.global_scoring_runners(global_url)

        runner_1 = global_scoring_runners_sorted[0][0]

        runner_2 = global_scoring_runners_sorted[1][0]

        runner_3 = global_scoring_runners_sorted[2][0]

        runner_4 = global_scoring_runners_sorted[3][0]

        runner_5 = global_scoring_runners_sorted[4][0]

        print("runner_1 : " + str(runner_1))

        print("runner_2 : " + str(runner_2))

        print("runner_3 : " + str(runner_3))

        print("runner_4 : " + str(runner_4))

        print("runner_5 : " + str(runner_5))

    # global_scoring_runners_for_prediction_pmu :
    def test_global_scoring_runners_for_prediction_pmu(self=None):
        print('test_global_scoring_runners_for_prediction_pmu')

        courses = []

        for course in courses:
            print('course : ' + str(course) + ' starting prediction pmu')

            global_scoring_runners_sorted = PMUFinal.global_scoring_runners(course)

            today = date.today()

            d1 = today.strftime("%d-%m-%Y")

            reunion_1 = course \
                          .replace("https://www.unibet.fr/turf/race/", "") \
                          .replace(today.strftime("%d-%m-%Y") + "-", "") \
                          .replace("-", "")[:2]

            course_1 = course \
                         .replace("https://www.unibet.fr/turf/race/", "") \
                         .replace(today.strftime("%d-%m-%Y") + "-", "") \
                         .replace("-", "")[2:4]

            runner_1 = global_scoring_runners_sorted[0][0]

            runner_2 = global_scoring_runners_sorted[1][0]

            runner_3 = global_scoring_runners_sorted[2][0]

            runner_4 = global_scoring_runners_sorted[3][0]

            runner_5 = global_scoring_runners_sorted[4][0]

            print("runner_1 : " + str(runner_1))

            print("runner_2 : " + str(runner_2))

            print("runner_3 : " + str(runner_3))

            print("runner_4 : " + str(runner_4))

            print("runner_5 : " + str(runner_5))

            try:
                connection = pymysql.connect(
                    host='localhost',
                    port=3306,
                    user='root',
                    password='',
                    db='pmu',
                    charset='utf8mb4',
                    cursorclass=pymysql.cursors.DictCursor
                )

                with connection.cursor() as cursor:
                    try:
                        sql = "INSERT INTO `prediction_pmu` (" \
                              "`date`, " \
                              "`reunion`, " \
                              "`course`, " \
                              "`cheval_1`, " \
                              "`cheval_2`, "\
                              "`cheval_3`, " \
                              "`cheval_4`, " \
                              "`cheval_5`) VALUE (%s, %s, %s, %s, %s, %s, %s, %s)"
                        cursor.execute(sql, (
                            d1,
                            reunion_1,
                            course_1,
                            runner_1,
                            runner_2,
                            runner_3,
                            runner_4,
                            runner_5
                        )
                                       )
                        connection.commit()
                        print("The record is stored for : " + str(course))
                        connection.close()
                    except Exception as e:
                        print("The record already exists for : " + str(course) + " _ " + str(e))
                        connection.close()
            except Exception as e:
                print(str(e) + " An error with the email for : " + str(course))


if __name__ == '__main__':
    unittest.main()
