import time
import warnings
from datetime import date
from selenium import webdriver
from requests_tor import RequestsTor
from selenium.webdriver.firefox.options import Options


class PMU:
    def __init__(self):
        pass

    # number of disqualified from musique from unibet : ok
    def number_of_disqualified_from_unibet(global_url):
        print('def number_of_disqualified_from_unibet(global_url):')

        reverse = False

        warnings.filterwarnings(action="ignore", message="unclosed", category=ResourceWarning)

        url = str(global_url)

        # with Firefox
        options = Options()
        options.headless = True
        browser = webdriver.Firefox(executable_path='geckodriver.exe', options=options)

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

        return scoring_runners

    # number of disqualified from musique from pmu : ok
    def number_of_disqualified(global_url):
        print('def number_of_disqualified(global_url):')

        reverse = False

        participant_key = 'musique'

        url_unibet_race = str(global_url)

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

        return scoring_runners

    # age : ok
    def age(global_url):
        print("def age(global_url):")

        reverse = False

        participant_key = 'age'

        url_unibet_race = str(global_url)

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

        return scoring_runners

    # placeCorde : ok
    def place_corde(global_url):
        print('def place_corde(global_url):')

        reverse = False

        participant_key = 'placeCorde'

        url_unibet_race = str(global_url)

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

        return scoring_runners

    # nombreCourses : ok
    def nombre_courses(global_url):
        print('def nombre_courses(global_url):')

        reverse = True

        participant_key = 'nombreCourses'

        url_unibet_race = str(global_url)

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

        return scoring_runners

    # nombreVictoires : ok
    def nombre_victoires(global_url):
        print('def nombre_victoires(global_url):')

        reverse = True

        participant_key = 'nombreVictoires'

        url_unibet_race = str(global_url)

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

        return scoring_runners

    # nombrePlaces : ok
    def nombre_places(global_url):
        print('def nombre_places(global_url):')

        reverse = True

        participant_key = 'nombrePlaces'

        url_unibet_race = str(global_url)

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

        return scoring_runners

    # nombrePlacesSecond : ok
    def nombre_places_second(global_url):
        print("def nombre_places_second(global_url):")

        reverse = True

        participant_key = 'nombrePlacesSecond'

        url_unibet_race = str(global_url)

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

        return scoring_runners

    # nombrePlacesTroisieme : ok
    def nombre_places_troisieme(global_url):
        print('def nombre_places_troisieme(global_url):')

        reverse = True

        participant_key = 'nombrePlacesTroisieme'

        url_unibet_race = str(global_url)

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

        return scoring_runners

    # gainsParticipant of gainsCarriere : ok
    def gains_participant_gains_carriere(global_url):
        print('def gains_participant_gains_carriere(global_url):')

        reverse = True

        participant_key = 'gainsCarriere'

        url_unibet_race = str(global_url)

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

        for participant in response.json()['participants']:
            num_pmu = str(participant['numPmu'])

            if 'gainsParticipant' in participant:
                criteria = int(participant['gainsParticipant'][participant_key])
                runners[num_pmu] = criteria
            else:
                runners[num_pmu] = 1

        runners_sorted = sorted(runners.items(), key=lambda x: x[1], reverse=reverse)

        scoring_runners = {}

        i = 1

        for runner in runners_sorted:
            scoring_runners[runner[0]] = i

            i += 1

        return scoring_runners

    # gainsParticipant of gainsVictoires : ok
    def gains_participant_gains_victoires(global_url):
        print('def gains_participant_gains_victoires(global_url):')

        reverse = True

        participant_key = 'gainsVictoires'

        url_unibet_race = str(global_url)

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

        for participant in response.json()['participants']:
            num_pmu = str(participant['numPmu'])

            if 'gainsParticipant' in participant:
                criteria = int(participant['gainsParticipant'][participant_key])
                runners[num_pmu] = criteria
            else:
                runners[num_pmu] = 1

        runners_sorted = sorted(runners.items(), key=lambda x: x[1], reverse=reverse)

        scoring_runners = {}

        i = 1

        for runner in runners_sorted:
            scoring_runners[runner[0]] = i

            i += 1

        return scoring_runners

    # gainsParticipant of gainsPlace : ok
    def gains_participant_gains_place(global_url):
        print('def gains_participant_gains_place(global_url):')

        reverse = True

        participant_key = 'gainsPlace'

        url_unibet_race = str(global_url)

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

        for participant in response.json()['participants']:
            num_pmu = str(participant['numPmu'])

            if 'gainsParticipant' in participant:
                criteria = int(participant['gainsParticipant'][participant_key])
                runners[num_pmu] = criteria
            else:
                runners[num_pmu] = 1

        runners_sorted = sorted(runners.items(), key=lambda x: x[1], reverse=reverse)

        scoring_runners = {}

        i = 1

        for runner in runners_sorted:
            scoring_runners[runner[0]] = i

            i += 1

        return scoring_runners

    # gainsParticipant of gainsAnneeEnCours : ok
    def gains_participant_gains_annee_en_cours(global_url):
        print('def gains_participant_gains_annee_en_cours(global_url):')

        reverse = True

        participant_key = 'gainsAnneeEnCours'

        url_unibet_race = str(global_url)

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

        for participant in response.json()['participants']:
            num_pmu = str(participant['numPmu'])

            if 'gainsParticipant' in participant:
                criteria = int(participant['gainsParticipant'][participant_key])
                runners[num_pmu] = criteria
            else:
                runners[num_pmu] = 1

        runners_sorted = sorted(runners.items(), key=lambda x: x[1], reverse=reverse)

        scoring_runners = {}

        i = 1

        for runner in runners_sorted:
            scoring_runners[runner[0]] = i

            i += 1

        return scoring_runners

    # gainsParticipant of gainsAnneePrecedente : ok
    def gains_participant_gains_annee_precedente(global_url):
        print('def gains_participant_gains_annee_precedente(global_url):')

        reverse = True

        participant_key = 'gainsAnneePrecedente'

        url_unibet_race = str(global_url)

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

        for participant in response.json()['participants']:
            num_pmu = str(participant['numPmu'])

            if 'gainsParticipant' in participant:
                criteria = int(participant['gainsParticipant'][participant_key])
                runners[num_pmu] = criteria
            else:
                runners[num_pmu] = 1

        runners_sorted = sorted(runners.items(), key=lambda x: x[1], reverse=reverse)

        scoring_runners = {}

        i = 1

        for runner in runners_sorted:
            scoring_runners[runner[0]] = i

            i += 1

        return scoring_runners

    # supplement : ok
    def supplement(global_url):
        print('def supplement(global_url):')

        reverse = True

        participant_key = 'supplement'

        url_unibet_race = str(global_url)

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

        return scoring_runners

    # handicapDistance : ok
    def handicap_distance(global_url):
        print('def handicap_distance(global_url):')

        reverse = False

        participant_key = 'handicapDistance'

        url_unibet_race = str(global_url)

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

        return scoring_runners

    # dernierRapportDirect of rapport : ok
    def dernier_rapport_direct_rapport(global_url):
        print('def dernier_rapport_direct_rapport(global_url):')

        reverse = False

        participant_key = 'rapport'

        url_unibet_race = str(global_url)

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

        for participant in response.json()['participants']:
            num_pmu = str(participant['numPmu'])

            if 'dernierRapportDirect' in participant:
                criteria = int(participant['dernierRapportDirect'][participant_key])
                runners[num_pmu] = criteria
            else:
                runners[num_pmu] = 1

        runners_sorted = sorted(runners.items(), key=lambda x: x[1], reverse=reverse)

        scoring_runners = {}

        i = 1

        for runner in runners_sorted:
            scoring_runners[runner[0]] = i

            i += 1

        return scoring_runners

    # dernierRapportDirect of nombreIndicateurTendance : ok
    def dernier_rapport_direct_nombre_indicateur_tendance(global_url):
        print("def dernier_rapport_direct_nombre_indicateur_tendance(global_url):")

        reverse = False

        participant_key = 'nombreIndicateurTendance'

        url_unibet_race = str(global_url)

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

        for participant in response.json()['participants']:
            num_pmu = str(participant['numPmu'])

            if 'dernierRapportDirect' in participant:
                criteria = int(participant['dernierRapportDirect'][participant_key])
                runners[num_pmu] = criteria
            else:
                runners[num_pmu] = 1

        runners_sorted = sorted(runners.items(), key=lambda x: x[1], reverse=reverse)

        scoring_runners = {}

        i = 1

        for runner in runners_sorted:
            scoring_runners[runner[0]] = i

            i += 1

        return scoring_runners

    # dernierRapportDirect of permutation : ok
    def dernier_rapport_direct_permutation(global_url):
        print("def dernier_rapport_direct_permutation(global_url):")

        reverse = False

        participant_key = 'permutation'

        url_unibet_race = str(global_url)

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

        for participant in response.json()['participants']:
            num_pmu = str(participant['numPmu'])

            if 'dernierRapportDirect' in participant:
                criteria = int(participant['dernierRapportDirect'][participant_key])
                runners[num_pmu] = criteria
            else:
                runners[num_pmu] = 1

        runners_sorted = sorted(runners.items(), key=lambda x: x[1], reverse=reverse)

        scoring_runners = {}

        i = 1

        for runner in runners_sorted:
            scoring_runners[runner[0]] = i

            i += 1

        return scoring_runners

    # dernierRapportDirect of numPmu1 : ok
    def dernier_rapport_direct_num_pmu1(global_url):
        print('def dernier_rapport_direct_num_pmu1(global_url):')

        reverse = False

        participant_key = 'numPmu1'

        url_unibet_race = str(global_url)

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

        for participant in response.json()['participants']:
            num_pmu = str(participant['numPmu'])

            if 'dernierRapportDirect' in participant:
                criteria = int(participant['dernierRapportDirect'][participant_key])
                runners[num_pmu] = criteria
            else:
                runners[num_pmu] = 1

        runners_sorted = sorted(runners.items(), key=lambda x: x[1], reverse=reverse)

        scoring_runners = {}

        i = 1

        for runner in runners_sorted:
            scoring_runners[runner[0]] = i

            i += 1

        return scoring_runners

    # dernierRapportReference of rapport : ok
    def dernier_rapport_reference_rapport(global_url):
        print('def dernier_rapport_reference_rapport(global_url):')

        reverse = False

        participant_key = 'rapport'

        url_unibet_race = str(global_url)

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

        return scoring_runners

    # dernierRapportReference of nombreIndicateurTendance
    def dernier_rapport_reference_nombre_indicateur_tendance(global_url):
        print('def dernier_rapport_reference_nombre_indicateur_tendance(global_url):')

        reverse = False

        participant_key = 'nombreIndicateurTendance'

        url_unibet_race = str(global_url)

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

        return scoring_runners

    # dernierRapportReference of permutation : ok
    def dernier_rapport_reference_permutation(global_url):
        print('def dernier_rapport_reference_permutation(global_url):')

        reverse = False

        participant_key = 'permutation'

        url_unibet_race = str(global_url)

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

        return scoring_runners

    # dernierRapportReference of numPmu1 : ok
    def dernier_rapport_reference_num_pmu1(global_url):
        print('def dernier_rapport_reference_num_pmu1(global_url):')

        reverse = False

        participant_key = 'numPmu1'

        url_unibet_race = str(global_url)

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

        return scoring_runners

    # musique : ok
    def musique(global_url):
        print('def musique(global_url):')

        reverse = False

        participant_key = 'musique'

        url_unibet_race = str(global_url)

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

        for participant in response.json()['participants']:
            num_pmu = str(participant['numPmu'])

            criteria = str(participant[participant_key]) \
                .replace('a', '') \
                .replace('D', '') \
                .replace('m', '') \
                .replace('Q', '') \
                .replace('R', '') \
                .replace('A', '') \
                .replace('p', '') \
                .replace('h', '') \
                .replace('s', '') \
                .replace('c', '') \
                .replace('T', '') \
                .replace('(22)', '') \
                .replace('(21)', '') \
                .replace('(20)', '') \
                .replace('(19)', '') \
                .replace('(18)', '') \
                .replace('(17)', '') \
                .replace('(16)', '')

            average = 0

            for i in range(0, len(criteria)):
                average += int(criteria[i])

            try:
                average_musique = average / len(criteria)

                runners[num_pmu] = average_musique
            except Exception as e:
                print('error average_musique : ' + str(e))

        runners_sorted = sorted(runners.items(), key=lambda x: x[1], reverse=reverse)

        scoring_runners = {}

        i = 1

        for runner in runners_sorted:
            scoring_runners[runner[0]] = i

            i += 1

        return scoring_runners

    # cote direct from unibet : ok
    def cotes_direct_from_unibet(global_url):
        print('def cotes_direct_from_unibet(global_url):')

        reverse = False

        warnings.filterwarnings(action="ignore", message="unclosed", category=ResourceWarning)

        url = str(global_url)

        # with Firefox
        options = Options()
        options.headless = True
        browser = webdriver.Firefox(executable_path='geckodriver.exe', options=options)

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

        return scoring_runners

    # cotes matin from unibet : ok
    def cotes_matin_from_unibet(global_url):
        print('def cotes_matin_from_unibet(global_url):')

        reverse = False

        warnings.filterwarnings(action="ignore", message="unclosed", category=ResourceWarning)

        url = str(global_url)

        # with Firefox
        options = Options()
        options.headless = True
        browser = webdriver.Firefox(executable_path='geckodriver.exe', options=options)

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

        return scoring_runners

    # musique from unibet : ok
    def musique_from_unibet(global_url):
        print('def musique_from_unibet(global_url):')

        reverse = False

        warnings.filterwarnings(action="ignore", message="unclosed", category=ResourceWarning)

        url = str(global_url)

        # with Firefox
        options = Options()
        options.headless = True
        browser = webdriver.Firefox(executable_path='geckodriver.exe', options=options)

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
                    .replace('h', '') \
                    .replace('s', '') \
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

                try:
                    average_musique = average / len(musique)

                    runners[num_pmu] = average_musique
                except Exception as e:
                    print('error average_musique : ' + str(e))
            except Exception as e:
                print('unable to locate the element : 1 _ ' + str(e))
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

        return scoring_runners

    # number of racers from pmu : ok
    def number_of_racers_from_unibet(global_url):
        print("def number_of_racers_from_unibet(global_url):")

        url_unibet_race = str(global_url)

        today = date.today()

        d1 = today.strftime("%d%m%Y")

        reunion = url_unibet_race \
                      .replace("https://www.unibet.fr/turf/race/", "") \
                      .replace(today.strftime("%d-%m-%Y") + "-", "") \
                      .replace("-", "")[:2]

        course = url_unibet_race \
                     .replace("https://www.unibet.fr/turf/race/", "") \
                     .replace(today.strftime("%d-%m-%Y") + "-", "") \
                     .replace("-", "")[2:4]

        url = "https://offline.turfinfo.api.pmu.fr/rest/client/1/programme/" + d1 + "/" + reunion + "/" + course + "/participants"

        headers = {
            "Accept": "application/json",
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103'
        }

        rt = RequestsTor()

        response = rt.get(url, headers=headers)

        number_of_runners = len(response.json()['participants'])

        return number_of_runners

    # musique from unibet x cote direct : ok
    def musique_from_unibet_x_cote_direct(global_url):
        print("def musique_from_unibet_x_cote_direct(global_url):")

        reverse = False

        url = str(global_url)

        warnings.filterwarnings(action="ignore", message="unclosed", category=ResourceWarning)

        # with Firefox
        options = Options()
        options.headless = True
        browser = webdriver.Firefox(executable_path='geckodriver.exe', options=options)

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

        return scoring_runners

    # musique from unibet x cote matin : ok
    def musique_from_unibet_x_cote_matin(global_url):
        print("def musique_from_unibet_x_cote_matin(global_url):")

        reverse = False

        url = str(global_url)

        warnings.filterwarnings(action="ignore", message="unclosed", category=ResourceWarning)

        # with Firefox
        options = Options()
        options.headless = True
        browser = webdriver.Firefox(executable_path='geckodriver.exe', options=options)

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

        return scoring_runners

    # musique from unibet x nombre courses : ok
    def musique_from_unibet_x_nombre_courses(global_url):
        print("def musique_from_unibet_x_nombre_courses(global_url):")

        reverse = False

        url = str(global_url)

        warnings.filterwarnings(action="ignore", message="unclosed", category=ResourceWarning)

        # with Firefox
        options = Options()
        options.headless = True
        browser = webdriver.Firefox(executable_path='geckodriver.exe', options=options)

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

            url_unibet_race = str(global_url)

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

            return scoring_runners
        except Exception as e:
            print('error 1 : ' + str(e))
            browser.quit()


class PMUFinal:
    def __init__(self):
        pass

    # global_scoring_runners
    def global_scoring_runners(global_url):
        global_scoring_runners = {}

        # Without learning code
        age = PMU.age(global_url)
        place_corde = PMU.place_corde(global_url)
        nombre_courses = PMU.nombre_courses(global_url)
        nombre_victoires = PMU.nombre_victoires(global_url)
        nombre_places = PMU.nombre_places(global_url)
        nombre_places_second = PMU.nombre_places_second(global_url)
        nombre_places_troisieme = PMU.nombre_places_troisieme(global_url)
        gains_participant_gains_carriere = PMU.gains_participant_gains_carriere(global_url)
        gains_participant_gains_victoires = PMU.gains_participant_gains_victoires(global_url)
        gains_participant_gains_place = PMU.gains_participant_gains_place(global_url)
        gains_participant_gains_annee_en_cours = PMU.gains_participant_gains_annee_en_cours(global_url)
        gains_participant_gains_annee_precedente = PMU.gains_participant_gains_annee_precedente(global_url)
        supplement = PMU.supplement(global_url)
        handicap_distance = PMU.handicap_distance(global_url)
        dernier_rapport_direct_rapport = PMU.dernier_rapport_direct_rapport(global_url)
        dernier_rapport_direct_nombre_indicateur_tendance = PMU.dernier_rapport_direct_nombre_indicateur_tendance(global_url)
        dernier_rapport_direct_permutation = PMU.dernier_rapport_direct_permutation(global_url)
        dernier_rapport_direct_num_pmu1 = PMU.dernier_rapport_direct_num_pmu1(global_url)
        dernier_rapport_reference_rapport = PMU.dernier_rapport_reference_rapport(global_url)
        dernier_rapport_reference_nombre_indicateur_tendance = PMU.dernier_rapport_reference_nombre_indicateur_tendance(global_url)
        dernier_rapport_reference_permutation = PMU.dernier_rapport_reference_permutation(global_url)
        dernier_rapport_reference_num_pmu1 = PMU.dernier_rapport_reference_num_pmu1(global_url)
        musique = PMU.musique(global_url)
        cotes_direct_from_unibet = PMU.cotes_direct_from_unibet(global_url)
        cotes_matin_from_unibet = PMU.cotes_matin_from_unibet(global_url)
        musique_from_unibet = PMU.musique_from_unibet(global_url)
        number_of_disqualified = PMU.number_of_disqualified(global_url)
        number_of_disqualified_from_unibet = PMU.number_of_disqualified_from_unibet(global_url)
        musique_from_unibet_x_cote_direct = PMU.musique_from_unibet_x_cote_direct(global_url)
        musique_from_unibet_x_cote_matin = PMU.musique_from_unibet_x_cote_matin(global_url)
        musique_from_unibet_x_nombre_courses = PMU.musique_from_unibet_x_nombre_courses(global_url)

        for i in range(1, int(PMU.number_of_racers_from_unibet(global_url)) + 1):
            global_scoring_runners[i] = age[str(i)]
            global_scoring_runners[i] += place_corde[str(i)]
            global_scoring_runners[i] += nombre_courses[str(i)]
            global_scoring_runners[i] += nombre_victoires[str(i)]
            global_scoring_runners[i] += nombre_places[str(i)]
            global_scoring_runners[i] += nombre_places_second[str(i)]
            global_scoring_runners[i] += nombre_places_troisieme[str(i)]
            global_scoring_runners[i] += gains_participant_gains_carriere[str(i)]
            global_scoring_runners[i] += gains_participant_gains_victoires[str(i)]
            global_scoring_runners[i] += gains_participant_gains_place[str(i)]
            global_scoring_runners[i] += gains_participant_gains_annee_en_cours[str(i)]
            global_scoring_runners[i] += gains_participant_gains_annee_precedente[str(i)]
            global_scoring_runners[i] += supplement[str(i)]
            global_scoring_runners[i] += handicap_distance[str(i)]
            global_scoring_runners[i] += dernier_rapport_direct_rapport[str(i)]
            global_scoring_runners[i] += dernier_rapport_direct_nombre_indicateur_tendance[str(i)]
            global_scoring_runners[i] += dernier_rapport_direct_permutation[str(i)]
            global_scoring_runners[i] += dernier_rapport_direct_num_pmu1[str(i)]
            global_scoring_runners[i] += dernier_rapport_reference_rapport[str(i)]
            global_scoring_runners[i] += dernier_rapport_reference_nombre_indicateur_tendance[str(i)]
            global_scoring_runners[i] += dernier_rapport_reference_permutation[str(i)]
            global_scoring_runners[i] += dernier_rapport_reference_num_pmu1[str(i)]
            global_scoring_runners[i] += musique[str(i)]
            global_scoring_runners[i] += cotes_direct_from_unibet[str(i)]
            global_scoring_runners[i] += cotes_matin_from_unibet[str(i)]
            global_scoring_runners[i] += musique_from_unibet[str(i)]
            global_scoring_runners[i] += number_of_disqualified[str(i)]
            global_scoring_runners[i] += number_of_disqualified_from_unibet[str(i)]
            global_scoring_runners[i] += musique_from_unibet_x_cote_direct[str(i)]
            global_scoring_runners[i] += musique_from_unibet_x_cote_matin[str(i)]
            global_scoring_runners[i] += musique_from_unibet_x_nombre_courses[str(i)]

        global_scoring_runners_sorted = sorted(global_scoring_runners.items(), key=lambda x: x[1])

        return global_scoring_runners_sorted