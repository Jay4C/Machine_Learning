import math
from bs4 import BeautifulSoup
from requests_tor import RequestsTor


# Indicators
# Money
# Money Supply M0
class Indicator_Money_Supply_M0:
    def __init__(self):
        pass

    # Money Supply M0 for USD
    def get_money_supply_m0_for_usd_united_states(self=None):
        money_supply_m0 = 0

        headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103'
        }

        url = "https://tradingeconomics.com/united-states/money-supply-m0"

        rt = RequestsTor()

        html_with_tor = rt.get(url, headers=headers)

        # Parse the content of html_doc
        soup = BeautifulSoup(html_with_tor.content, 'html.parser')

        element = soup.find('div', id="ctl00_ContentPlaceHolder1_ctl00_ctl00_Panel1")

        if element is not None:
            value = float(element.find('table', {'class': 'table table-hover'})
                          .find_all('tr', {'class': 'datatable-row'})[1].find_all('td')[1].text)

            unit = element \
                .find('table', {'class': 'table table-hover'}) \
                .find_all('tr', {'class': 'datatable-row'})[1] \
                .find_all('td')[3] \
                .text \
                .split(' ')[1]

            if unit == "Million":
                money_supply_m0 += value * math.pow(10, 6)
            elif unit == "Billion":
                money_supply_m0 += value * math.pow(10, 9)
            elif unit == "Thousands":
                money_supply_m0 += value * math.pow(10, 3)

        return money_supply_m0

    def get_money_supply_m0_for_usd_belize(self=None):
        money_supply_m0 = 0

        headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103'
        }

        url = "https://tradingeconomics.com/belize/money-supply-m0"

        rt = RequestsTor()

        html_with_tor = rt.get(url, headers=headers)

        # Parse the content of html_doc
        soup = BeautifulSoup(html_with_tor.content, 'html.parser')

        element = soup.find('div', id="ctl00_ContentPlaceHolder1_ctl00_ctl00_Panel1")

        if element is not None:
            value = float(element.find('table', {'class': 'table table-hover'})
                          .find_all('tr', {'class': 'datatable-row'})[1].find_all('td')[1].text)

            unit = element \
                .find('table', {'class': 'table table-hover'}) \
                .find_all('tr', {'class': 'datatable-row'})[1] \
                .find_all('td')[3] \
                .text \
                .split(' ')[1]

            if unit == "Million":
                money_supply_m0 += value * math.pow(10, 6)
            elif unit == "Billion":
                money_supply_m0 += value * math.pow(10, 9)
            elif unit == "Thousands":
                money_supply_m0 += value * math.pow(10, 3)

        return money_supply_m0

    def get_money_supply_m0_for_usd_el_salvador(self=None):
        money_supply_m0 = 0

        headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103'
        }

        url = "https://tradingeconomics.com/el-salvador/money-supply-m0"

        rt = RequestsTor()

        html_with_tor = rt.get(url, headers=headers)

        # Parse the content of html_doc
        soup = BeautifulSoup(html_with_tor.content, 'html.parser')

        element = soup.find('div', id="ctl00_ContentPlaceHolder1_ctl00_ctl00_Panel1")

        if element is not None:
            value = float(element.find('table', {'class': 'table table-hover'})
                          .find_all('tr', {'class': 'datatable-row-alternating'})[0]
                          .find_all('td')[1]
                          .text)

            unit = element \
                .find('table', {'class': 'table table-hover'}) \
                .find_all('tr', {'class': 'datatable-row-alternating'})[0] \
                .find_all('td')[3] \
                .text \
                .split(' ')[1]

            if unit == "Million":
                money_supply_m0 += value * math.pow(10, 6)
            elif unit == "Billion":
                money_supply_m0 += value * math.pow(10, 9)
            elif unit == "Thousands":
                money_supply_m0 += value * math.pow(10, 3)

        return money_supply_m0

    def get_money_supply_m0_for_usd_global(self=None):
        money_supply_m0_for_usd_global = 0

        money_supply_m0_for_usd_global += Indicator_Money_Supply_M0.get_money_supply_m0_for_usd_united_states() \
                                          + Indicator_Money_Supply_M0.get_money_supply_m0_for_usd_belize() \
                                          + Indicator_Money_Supply_M0.get_money_supply_m0_for_usd_el_salvador()

        return money_supply_m0_for_usd_global

    # Money Supply M0 for EUR
    def get_money_supply_m0_for_eur_finland(self=None):
        money_supply_m0 = 0

        headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103'
        }

        url = "https://tradingeconomics.com/finland/money-supply-m0"

        rt = RequestsTor()

        html_with_tor = rt.get(url, headers=headers)

        # Parse the content of html_doc
        soup = BeautifulSoup(html_with_tor.content, 'html.parser')

        element = soup.find('div', id="ctl00_ContentPlaceHolder1_ctl00_ctl00_Panel1")

        if element is not None:
            value = float(element.find('table', {'class': 'table table-hover'})
                          .find_all('tr', {'class': 'datatable-row-alternating'})[0]
                          .find_all('td')[1]
                          .text)

            unit = element\
                .find('table', {'class': 'table table-hover'})\
                .find_all('tr', {'class': 'datatable-row-alternating'})[0]\
                .find_all('td')[3]\
                .text\
                .split(' ')[1]

            if unit == "Million":
                money_supply_m0 += value * math.pow(10, 6)
            elif unit == "Billion":
                money_supply_m0 += value * math.pow(10, 9)
            elif unit == "Thousands":
                money_supply_m0 += value * math.pow(10, 3)

        return money_supply_m0

    def get_money_supply_m0_for_eur_greece(self=None):
        money_supply_m0 = 0

        headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103'
        }

        url = "https://tradingeconomics.com/greece/money-supply-m0"

        rt = RequestsTor()

        html_with_tor = rt.get(url, headers=headers)

        # Parse the content of html_doc
        soup = BeautifulSoup(html_with_tor.content, 'html.parser')

        element = soup.find('div', id="ctl00_ContentPlaceHolder1_ctl00_ctl00_Panel1")

        if element is not None:
            value = float(element.find('table', {'class': 'table table-hover'})
                          .find_all('tr', {'class': 'datatable-row'})[1]
                          .find_all('td')[1]
                          .text)

            unit = element\
                .find('table', {'class': 'table table-hover'})\
                .find_all('tr', {'class': 'datatable-row'})[1]\
                .find_all('td')[3]\
                .text\
                .split(' ')[1]

            if unit == "Million":
                money_supply_m0 += value * math.pow(10, 6)
            elif unit == "Billion":
                money_supply_m0 += value * math.pow(10, 9)
            elif unit == "Thousands":
                money_supply_m0 += value * math.pow(10, 3)

        return money_supply_m0

    def get_money_supply_m0_for_eur_latvia(self=None):
        money_supply_m0 = 0

        headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103'
        }

        url = "https://tradingeconomics.com/latvia/money-supply-m0"

        rt = RequestsTor()

        html_with_tor = rt.get(url, headers=headers)

        # Parse the content of html_doc
        soup = BeautifulSoup(html_with_tor.content, 'html.parser')

        element = soup.find('div', id="ctl00_ContentPlaceHolder1_ctl00_ctl00_Panel1")

        if element is not None:
            value = float(element.find('table', {'class': 'table table-hover'})
                          .find_all('tr', {'class': 'datatable-row-alternating'})[0]
                          .find_all('td')[1]
                          .text)

            unit = element\
                .find('table', {'class': 'table table-hover'})\
                .find_all('tr', {'class': 'datatable-row-alternating'})[0]\
                .find_all('td')[3]\
                .text\
                .split(' ')[1]

            if unit == "Million":
                money_supply_m0 += value * math.pow(10, 6)
            elif unit == "Billion":
                money_supply_m0 += value * math.pow(10, 9)
            elif unit == "Thousands":
                money_supply_m0 += value * math.pow(10, 3)

        return money_supply_m0

    def get_money_supply_m0_for_eur_lithuania(self=None):
        money_supply_m0 = 0

        headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103'
        }

        url = "https://tradingeconomics.com/lithuania/money-supply-m0"

        rt = RequestsTor()

        html_with_tor = rt.get(url, headers=headers)

        # Parse the content of html_doc
        soup = BeautifulSoup(html_with_tor.content, 'html.parser')

        element = soup.find('div', id="ctl00_ContentPlaceHolder1_ctl00_ctl00_Panel1")

        if element is not None:
            value = float(element.find('table', {'class': 'table table-hover'})
                          .find_all('tr', {'class': 'datatable-row-alternating'})[1]
                          .find_all('td')[1]
                          .text)

            unit = element\
                .find('table', {'class': 'table table-hover'})\
                .find_all('tr', {'class': 'datatable-row-alternating'})[1]\
                .find_all('td')[3]\
                .text\
                .split(' ')[1]

            if unit == "Million":
                money_supply_m0 += value * math.pow(10, 6)
            elif unit == "Billion":
                money_supply_m0 += value * math.pow(10, 9)
            elif unit == "Thousands":
                money_supply_m0 += value * math.pow(10, 3)

        return money_supply_m0

    def get_money_supply_m0_for_eur_luxembourg(self=None):
        money_supply_m0 = 0

        headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103'
        }

        url = "https://tradingeconomics.com/luxembourg/money-supply-m0"

        rt = RequestsTor()

        html_with_tor = rt.get(url, headers=headers)

        # Parse the content of html_doc
        soup = BeautifulSoup(html_with_tor.content, 'html.parser')

        element = soup.find('div', id="ctl00_ContentPlaceHolder1_ctl00_ctl00_Panel1")

        if element is not None:
            value = float(element.find('table', {'class': 'table table-hover'})
                          .find_all('tr', {'class': 'datatable-row-alternating'})[0]
                          .find_all('td')[1]
                          .text)

            unit = element\
                .find('table', {'class': 'table table-hover'})\
                .find_all('tr', {'class': 'datatable-row-alternating'})[0]\
                .find_all('td')[3]\
                .text\
                .split(' ')[1]

            if unit == "Million":
                money_supply_m0 += value * math.pow(10, 6)
            elif unit == "Billion":
                money_supply_m0 += value * math.pow(10, 9)
            elif unit == "Thousands":
                money_supply_m0 += value * math.pow(10, 3)

        return money_supply_m0

    def get_money_supply_m0_for_eur_malta(self=None):
        money_supply_m0 = 0

        headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103'
        }

        url = "https://tradingeconomics.com/malta/money-supply-m0"

        rt = RequestsTor()

        html_with_tor = rt.get(url, headers=headers)

        # Parse the content of html_doc
        soup = BeautifulSoup(html_with_tor.content, 'html.parser')

        element = soup.find('div', id="ctl00_ContentPlaceHolder1_ctl00_ctl00_Panel1")

        if element is not None:
            value = float(element.find('table', {'class': 'table table-hover'})
                          .find_all('tr', {'class': 'datatable-row-alternating'})[0]
                          .find_all('td')[1]
                          .text)

            unit = element\
                .find('table', {'class': 'table table-hover'})\
                .find_all('tr', {'class': 'datatable-row-alternating'})[0]\
                .find_all('td')[3]\
                .text\
                .split(' ')[1]

            if unit == "Million":
                money_supply_m0 += value * math.pow(10, 6)
            elif unit == "Billion":
                money_supply_m0 += value * math.pow(10, 9)
            elif unit == "Thousands":
                money_supply_m0 += value * math.pow(10, 3)

        return money_supply_m0

    def get_money_supply_m0_for_eur_netherlands(self=None):
        money_supply_m0 = 0

        headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103'
        }

        url = "https://tradingeconomics.com/netherlands/money-supply-m0"

        rt = RequestsTor()

        html_with_tor = rt.get(url, headers=headers)

        # Parse the content of html_doc
        soup = BeautifulSoup(html_with_tor.content, 'html.parser')

        element = soup.find('div', id="ctl00_ContentPlaceHolder1_ctl00_ctl00_Panel1")

        if element is not None:
            value = float(element.find('table', {'class': 'table table-hover'})
                          .find_all('tr', {'class': 'datatable-row-alternating'})[0]
                          .find_all('td')[1]
                          .text)

            unit = element\
                .find('table', {'class': 'table table-hover'})\
                .find_all('tr', {'class': 'datatable-row-alternating'})[0]\
                .find_all('td')[3]\
                .text\
                .split(' ')[1]

            if unit == "Million":
                money_supply_m0 += value * math.pow(10, 6)
            elif unit == "Billion":
                money_supply_m0 += value * math.pow(10, 9)
            elif unit == "Thousands":
                money_supply_m0 += value * math.pow(10, 3)

        return money_supply_m0

    def get_money_supply_m0_for_eur_portugal(self=None):
        money_supply_m0 = 0

        headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103'
        }

        url = "https://tradingeconomics.com/portugal/money-supply-m0"

        rt = RequestsTor()

        html_with_tor = rt.get(url, headers=headers)

        # Parse the content of html_doc
        soup = BeautifulSoup(html_with_tor.content, 'html.parser')

        element = soup.find('div', id="ctl00_ContentPlaceHolder1_ctl00_ctl00_Panel1")

        if element is not None:
            value = float(element.find('table', {'class': 'table table-hover'})
                          .find_all('tr', {'class': 'datatable-row'})[0]
                          .find_all('td')[1]
                          .text)

            """
            unit = element\
                .find('table', {'class': 'table table-hover'})\
                .find_all('tr', {'class': 'datatable-row'})[0]\
                .find_all('td')[3]\
                .text\
                .split(' ')[1]
            
            if unit == "Million":
                money_supply_m0 += value * math.pow(10, 6)
            elif unit == "Billion":
                money_supply_m0 += value * math.pow(10, 9)
            elif unit == "Thousands":
                money_supply_m0 += value * math.pow(10, 3)
            """

            money_supply_m0 += value * math.pow(10, 6)

        return money_supply_m0

    def get_money_supply_m0_for_eur_slovakia(self=None):
        money_supply_m0 = 0

        headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103'
        }

        url = "https://tradingeconomics.com/slovakia/money-supply-m0"

        rt = RequestsTor()

        html_with_tor = rt.get(url, headers=headers)

        # Parse the content of html_doc
        soup = BeautifulSoup(html_with_tor.content, 'html.parser')

        element = soup.find('div', id="ctl00_ContentPlaceHolder1_ctl00_ctl00_Panel1")

        if element is not None:
            value = float(element.find('table', {'class': 'table table-hover'})
                          .find_all('tr', {'class': 'datatable-row-alternating'})[0]
                          .find_all('td')[1]
                          .text)

            unit = element\
                .find('table', {'class': 'table table-hover'})\
                .find_all('tr', {'class': 'datatable-row-alternating'})[0]\
                .find_all('td')[3]\
                .text\
                .split(' ')[1]

            if unit == "Million":
                money_supply_m0 += value * math.pow(10, 6)
            elif unit == "Billion":
                money_supply_m0 += value * math.pow(10, 9)
            elif unit == "Thousands":
                money_supply_m0 += value * math.pow(10, 3)

        return money_supply_m0

    def get_money_supply_m0_for_eur_slovenia(self=None):
        money_supply_m0 = 0

        headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103'
        }

        url = "https://tradingeconomics.com/slovenia/money-supply-m0"

        rt = RequestsTor()

        html_with_tor = rt.get(url, headers=headers)

        # Parse the content of html_doc
        soup = BeautifulSoup(html_with_tor.content, 'html.parser')

        element = soup.find('div', id="ctl00_ContentPlaceHolder1_ctl00_ctl00_Panel1")

        if element is not None:
            value = float(element.find('table', {'class': 'table table-hover'})
                          .find_all('tr', {'class': 'datatable-row-alternating'})[0]
                          .find_all('td')[1]
                          .text)

            unit = element\
                .find('table', {'class': 'table table-hover'})\
                .find_all('tr', {'class': 'datatable-row-alternating'})[0]\
                .find_all('td')[3]\
                .text\
                .split(' ')[1]

            if unit == "Million":
                money_supply_m0 += value * math.pow(10, 6)
            elif unit == "Billion":
                money_supply_m0 += value * math.pow(10, 9)
            elif unit == "Thousands":
                money_supply_m0 += value * math.pow(10, 3)

        return money_supply_m0

    def get_money_supply_m0_for_eur_belgium(self=None):
        money_supply_m0 = 0

        headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103'
        }

        url = "https://tradingeconomics.com/belgium/money-supply-m0"

        rt = RequestsTor()

        html_with_tor = rt.get(url, headers=headers)

        # Parse the content of html_doc
        soup = BeautifulSoup(html_with_tor.content, 'html.parser')

        element = soup.find('div', id="ctl00_ContentPlaceHolder1_ctl00_ctl00_Panel1")

        if element is not None:
            value = float(element.find('table', {'class': 'table table-hover'})
                          .find_all('tr', {'class': 'datatable-row'})[1]
                          .find_all('td')[1]
                          .text)

            unit = element\
                .find('table', {'class': 'table table-hover'})\
                .find_all('tr', {'class': 'datatable-row'})[1]\
                .find_all('td')[3]\
                .text\
                .split(' ')[1]

            if unit == "Million":
                money_supply_m0 += value * math.pow(10, 6)
            elif unit == "Billion":
                money_supply_m0 += value * math.pow(10, 9)
            elif unit == "Thousands":
                money_supply_m0 += value * math.pow(10, 3)

        return money_supply_m0

    def get_money_supply_m0_for_eur_global(self=None):
        money_supply_m0_for_eur_global = 0

        money_supply_m0_for_eur_global += Indicator_Money_Supply_M0.get_money_supply_m0_for_eur_belgium() \
                                          + Indicator_Money_Supply_M0.get_money_supply_m0_for_eur_finland() \
                                          + Indicator_Money_Supply_M0.get_money_supply_m0_for_eur_greece() \
                                          + Indicator_Money_Supply_M0.get_money_supply_m0_for_eur_latvia() \
                                          + Indicator_Money_Supply_M0.get_money_supply_m0_for_eur_slovakia() \
                                          + Indicator_Money_Supply_M0.get_money_supply_m0_for_eur_slovenia() \
                                          + Indicator_Money_Supply_M0.get_money_supply_m0_for_eur_netherlands() \
                                          + Indicator_Money_Supply_M0.get_money_supply_m0_for_eur_lithuania() \
                                          + Indicator_Money_Supply_M0.get_money_supply_m0_for_eur_luxembourg() \
                                          + Indicator_Money_Supply_M0.get_money_supply_m0_for_eur_malta() \
                                          + Indicator_Money_Supply_M0.get_money_supply_m0_for_eur_portugal()

        return money_supply_m0_for_eur_global
# Money Supply M0


# Money Supply M1
class Indicator_Money_Supply_M1:
    def __init__(self):
        pass

    # Money Supply M1 for USD
    def get_money_supply_m1_for_usd_united_states(self=None):
        money_supply_m1 = 0

        headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103'
        }

        url = "https://tradingeconomics.com/united-states/money-supply-m1"

        rt = RequestsTor()

        html_with_tor = rt.get(url, headers=headers)

        soup = BeautifulSoup(html_with_tor.content, 'html.parser')

        element = soup.find('div', id="ctl00_ContentPlaceHolder1_ctl00_ctl00_Panel1")

        if element is not None:
            value = float(element.find('table', {'class': 'table table-hover'})
                          .find_all('tr', {'class': 'datatable-row-alternating'})[0]
                          .find_all('td')[1]
                          .text)

            unit = element \
                .find('table', {'class': 'table table-hover'}) \
                .find_all('tr', {'class': 'datatable-row-alternating'})[0] \
                .find_all('td')[3] \
                .text \
                .split(' ')[1]

            if unit == "Million":
                money_supply_m1 += value * math.pow(10, 6)
            elif unit == "Billion":
                money_supply_m1 += value * math.pow(10, 9)
            elif unit == "Thousands":
                money_supply_m1 += value * math.pow(10, 3)

        return money_supply_m1

    def get_money_supply_m1_for_usd_belize(self=None):
        money_supply_m1 = 0

        headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103'
        }

        url = "https://tradingeconomics.com/belize/money-supply-m1"

        rt = RequestsTor()

        html_with_tor = rt.get(url, headers=headers)

        soup = BeautifulSoup(html_with_tor.content, 'html.parser')

        element = soup.find('div', id="ctl00_ContentPlaceHolder1_ctl00_ctl00_Panel1")

        if element is not None:
            value = float(element.find('table', {'class': 'table table-hover'})
                          .find_all('tr', {'class': 'datatable-row-alternating'})[0]
                          .find_all('td')[1]
                          .text)

            unit = element \
                .find('table', {'class': 'table table-hover'}) \
                .find_all('tr', {'class': 'datatable-row-alternating'})[0] \
                .find_all('td')[3] \
                .text \
                .split(' ')[1]

            if unit == "Million":
                money_supply_m1 += value * math.pow(10, 6)
            elif unit == "Billion":
                money_supply_m1 += value * math.pow(10, 9)
            elif unit == "Thousands":
                money_supply_m1 += value * math.pow(10, 3)

        return money_supply_m1

    def get_money_supply_m1_for_usd_ecuador(self=None):
        money_supply_m1 = 0

        headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103'
        }

        url = "https://tradingeconomics.com/ecuador/money-supply-m1"

        rt = RequestsTor()

        html_with_tor = rt.get(url, headers=headers)

        soup = BeautifulSoup(html_with_tor.content, 'html.parser')

        element = soup.find('div', id="ctl00_ContentPlaceHolder1_ctl00_ctl00_Panel1")

        if element is not None:
            value = float(element.find('table', {'class': 'table table-hover'})
                          .find_all('tr', {'class': 'datatable-row'})[1]
                          .find_all('td')[1]
                          .text)

            unit = element \
                .find('table', {'class': 'table table-hover'}) \
                .find_all('tr', {'class': 'datatable-row'})[1] \
                .find_all('td')[3] \
                .text \
                .split(' ')[1]

            if unit == "Million":
                money_supply_m1 += value * math.pow(10, 6)
            elif unit == "Billion":
                money_supply_m1 += value * math.pow(10, 9)
            elif unit == "Thousands":
                money_supply_m1 += value * math.pow(10, 3)

        return money_supply_m1

    def get_money_supply_m1_for_usd_el_salvador(self=None):
        money_supply_m1 = 0

        headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103'
        }

        url = "https://tradingeconomics.com/el-salvador/money-supply-m1"

        rt = RequestsTor()

        html_with_tor = rt.get(url, headers=headers)

        soup = BeautifulSoup(html_with_tor.content, 'html.parser')

        element = soup.find('div', id="ctl00_ContentPlaceHolder1_ctl00_ctl00_Panel1")

        if element is not None:
            value = float(element.find('table', {'class': 'table table-hover'})
                          .find_all('tr', {'class': 'datatable-row'})[1]
                          .find_all('td')[1]
                          .text)

            unit = element \
                .find('table', {'class': 'table table-hover'}) \
                .find_all('tr', {'class': 'datatable-row'})[1] \
                .find_all('td')[3] \
                .text \
                .split(' ')[1]

            if unit == "Million":
                money_supply_m1 += value * math.pow(10, 6)
            elif unit == "Billion":
                money_supply_m1 += value * math.pow(10, 9)
            elif unit == "Thousands":
                money_supply_m1 += value * math.pow(10, 3)

        return money_supply_m1

    def get_money_supply_m1_for_usd_zimbabwe(self=None):
        money_supply_m1 = 0

        headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103'
        }

        url = "https://tradingeconomics.com/zimbabwe/money-supply-m1"

        rt = RequestsTor()

        html_with_tor = rt.get(url, headers=headers)

        soup = BeautifulSoup(html_with_tor.content, 'html.parser')

        element = soup.find('div', id="ctl00_ContentPlaceHolder1_ctl00_ctl00_Panel1")

        if element is not None:
            value = float(element.find('table', {'class': 'table table-hover'})
                          .find_all('tr', {'class': 'datatable-row-alternating'})[0]
                          .find_all('td')[1]
                          .text)

            unit = element \
                .find('table', {'class': 'table table-hover'}) \
                .find_all('tr', {'class': 'datatable-row-alternating'})[0] \
                .find_all('td')[3] \
                .text \
                .split(' ')[1]

            if unit == "Million":
                money_supply_m1 += value * math.pow(10, 6)
            elif unit == "Billion":
                money_supply_m1 += value * math.pow(10, 9)
            elif unit == "Thousands":
                money_supply_m1 += value * math.pow(10, 3)

        return money_supply_m1

    def get_money_supply_m1_for_usd_global(self=None):
        money_supply_m1_for_usd_global = 0

        money_supply_m1_for_usd_global += Indicator_Money_Supply_M1.get_money_supply_m1_for_usd_united_states() \
                                          + Indicator_Money_Supply_M1.get_money_supply_m1_for_usd_belize() \
                                          + Indicator_Money_Supply_M1.get_money_supply_m1_for_usd_el_salvador() \
                                          + Indicator_Money_Supply_M1.get_money_supply_m1_for_usd_ecuador() \
                                          + Indicator_Money_Supply_M1.get_money_supply_m1_for_usd_zimbabwe()

        return money_supply_m1_for_usd_global

    # Money Supply M1 for EUR
    def get_money_supply_m1_for_eur_euro_area(self=None):
        money_supply_m1 = 0

        headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103'
        }

        url = "https://tradingeconomics.com/euro-area/money-supply-m1"

        rt = RequestsTor()

        html_with_tor = rt.get(url, headers=headers)

        soup = BeautifulSoup(html_with_tor.content, 'html.parser')

        element = soup.find('div', id="ctl00_ContentPlaceHolder1_ctl00_ctl00_Panel1")

        if element is not None:
            value = float(element.find('table', {'class': 'table table-hover'})
                          .find_all('tr', {'class': 'datatable-row-alternating'})[0]
                          .find_all('td')[1]
                          .text)

            unit = element \
                .find('table', {'class': 'table table-hover'}) \
                .find_all('tr', {'class': 'datatable-row-alternating'})[0] \
                .find_all('td')[3] \
                .text \
                .split(' ')[1]

            if unit == "Million":
                money_supply_m1 += value * math.pow(10, 6)
            elif unit == "Billion":
                money_supply_m1 += value * math.pow(10, 9)
            elif unit == "Thousands":
                money_supply_m1 += value * math.pow(10, 3)

        return money_supply_m1

    def get_money_supply_m1_for_eur_global(self=None):
        money_supply_m1_for_usd_global = 0

        money_supply_m1_for_usd_global += Indicator_Money_Supply_M1.get_money_supply_m1_for_eur_euro_area()

        return money_supply_m1_for_usd_global
# Money Supply M1


# Money Supply M2
class Indicator_Money_Supply_M2:
    def __init__(self):
        pass

    # Money Supply M2 for USD
    def get_money_supply_m2_for_usd_united_states(self=None):
        money_supply_m2 = 0

        headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103'
        }

        url = "https://tradingeconomics.com/united-states/money-supply-m2"

        rt = RequestsTor()

        html_with_tor = rt.get(url, headers=headers)

        soup = BeautifulSoup(html_with_tor.content, 'html.parser')

        element = soup.find('div', id="ctl00_ContentPlaceHolder1_ctl00_ctl00_Panel1")

        if element is not None:
            value = float(element.find('table', {'class': 'table table-hover'})
                          .find_all('tr', {'class': 'datatable-row-alternating'})[1]
                          .find_all('td')[1]
                          .text)

            unit = element \
                .find('table', {'class': 'table table-hover'}) \
                .find_all('tr', {'class': 'datatable-row-alternating'})[1] \
                .find_all('td')[3] \
                .text \
                .split(' ')[1]

            if unit == "Million":
                money_supply_m2 += value * math.pow(10, 6)
            elif unit == "Billion":
                money_supply_m2 += value * math.pow(10, 9)
            elif unit == "Thousands":
                money_supply_m2 += value * math.pow(10, 3)

        return money_supply_m2

    def get_money_supply_m2_for_usd_zimbabwe(self=None):
        money_supply_m2 = 0

        headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103'
        }

        url = "https://tradingeconomics.com/zimbabwe/money-supply-m2"

        rt = RequestsTor()

        html_with_tor = rt.get(url, headers=headers)

        soup = BeautifulSoup(html_with_tor.content, 'html.parser')

        element = soup.find('div', id="ctl00_ContentPlaceHolder1_ctl00_ctl00_Panel1")

        if element is not None:
            value = float(element.find('table', {'class': 'table table-hover'})
                          .find_all('tr', {'class': 'datatable-row'})[1]
                          .find_all('td')[1]
                          .text)

            unit = element \
                .find('table', {'class': 'table table-hover'}) \
                .find_all('tr', {'class': 'datatable-row'})[1] \
                .find_all('td')[3] \
                .text \
                .split(' ')[1]

            if unit == "Million":
                money_supply_m2 += value * math.pow(10, 6)
            elif unit == "Billion":
                money_supply_m2 += value * math.pow(10, 9)
            elif unit == "Thousands":
                money_supply_m2 += value * math.pow(10, 3)

        return money_supply_m2

    def get_money_supply_m2_for_usd_el_salvador(self=None):
        money_supply_m2 = 0

        headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103'
        }

        url = "https://tradingeconomics.com/el-salvador/money-supply-m2"

        rt = RequestsTor()

        html_with_tor = rt.get(url, headers=headers)

        soup = BeautifulSoup(html_with_tor.content, 'html.parser')

        element = soup.find('div', id="ctl00_ContentPlaceHolder1_ctl00_ctl00_Panel1")

        if element is not None:
            value = float(element.find('table', {'class': 'table table-hover'})
                          .find_all('tr', {'class': 'datatable-row-alternating'})[1]
                          .find_all('td')[1]
                          .text)

            unit = element \
                .find('table', {'class': 'table table-hover'}) \
                .find_all('tr', {'class': 'datatable-row-alternating'})[1] \
                .find_all('td')[3] \
                .text \
                .split(' ')[1]

            if unit == "Million":
                money_supply_m2 += value * math.pow(10, 6)
            elif unit == "Billion":
                money_supply_m2 += value * math.pow(10, 9)
            elif unit == "Thousands":
                money_supply_m2 += value * math.pow(10, 3)

        return money_supply_m2

    def get_money_supply_m2_for_usd_ecuador(self=None):
        money_supply_m2 = 0

        headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103'
        }

        url = "https://tradingeconomics.com/ecuador/money-supply-m2"

        rt = RequestsTor()

        html_with_tor = rt.get(url, headers=headers)

        soup = BeautifulSoup(html_with_tor.content, 'html.parser')

        element = soup.find('div', id="ctl00_ContentPlaceHolder1_ctl00_ctl00_Panel1")

        if element is not None:
            value = float(element.find('table', {'class': 'table table-hover'})
                          .find_all('tr', {'class': 'datatable-row-alternating'})[1]
                          .find_all('td')[1]
                          .text)

            unit = element \
                .find('table', {'class': 'table table-hover'}) \
                .find_all('tr', {'class': 'datatable-row-alternating'})[1] \
                .find_all('td')[3] \
                .text \
                .split(' ')[1]

            if unit == "Million":
                money_supply_m2 += value * math.pow(10, 6)
            elif unit == "Billion":
                money_supply_m2 += value * math.pow(10, 9)
            elif unit == "Thousands":
                money_supply_m2 += value * math.pow(10, 3)

        return money_supply_m2

    def get_money_supply_m2_for_usd_belize(self=None):
        money_supply_m2 = 0

        headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103'
        }

        url = "https://tradingeconomics.com/belize/money-supply-m2"

        rt = RequestsTor()

        html_with_tor = rt.get(url, headers=headers)

        soup = BeautifulSoup(html_with_tor.content, 'html.parser')

        element = soup.find('div', id="ctl00_ContentPlaceHolder1_ctl00_ctl00_Panel1")

        if element is not None:
            value = float(element.find('table', {'class': 'table table-hover'})
                          .find_all('tr', {'class': 'datatable-row-alternating'})[1]
                          .find_all('td')[1]
                          .text)

            unit = element \
                .find('table', {'class': 'table table-hover'}) \
                .find_all('tr', {'class': 'datatable-row-alternating'})[1] \
                .find_all('td')[3] \
                .text \
                .split(' ')[1]

            if unit == "Million":
                money_supply_m2 += value * math.pow(10, 6)
            elif unit == "Billion":
                money_supply_m2 += value * math.pow(10, 9)
            elif unit == "Thousands":
                money_supply_m2 += value * math.pow(10, 3)

        return money_supply_m2

    def get_money_supply_m2_for_usd_global(self=None):
        money_supply_m2_for_usd_global = 0

        money_supply_m2_for_usd_global += Indicator_Money_Supply_M2.get_money_supply_m2_for_usd_united_states() \
                                          + Indicator_Money_Supply_M2.get_money_supply_m2_for_usd_belize() \
                                          + Indicator_Money_Supply_M2.get_money_supply_m2_for_usd_el_salvador() \
                                          + Indicator_Money_Supply_M2.get_money_supply_m2_for_usd_ecuador() \
                                          + Indicator_Money_Supply_M2.get_money_supply_m2_for_usd_zimbabwe()

        return money_supply_m2_for_usd_global

    # Money Supply M2 for EUR
    def get_money_supply_m2_for_eur_euro_area(self=None):
        money_supply_m2 = 0

        headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103'
        }

        url = "https://tradingeconomics.com/euro-area/money-supply-m2"

        rt = RequestsTor()

        html_with_tor = rt.get(url, headers=headers)

        soup = BeautifulSoup(html_with_tor.content, 'html.parser')

        element = soup.find('div', id="ctl00_ContentPlaceHolder1_ctl00_ctl00_Panel1")

        if element is not None:
            value = float(element.find('table', {'class': 'table table-hover'})
                          .find_all('tr', {'class': 'datatable-row'})[1]
                          .find_all('td')[1]
                          .text)

            unit = element \
                .find('table', {'class': 'table table-hover'}) \
                .find_all('tr', {'class': 'datatable-row'})[1] \
                .find_all('td')[3] \
                .text \
                .split(' ')[1]

            if unit == "Million":
                money_supply_m2 += value * math.pow(10, 6)
            elif unit == "Billion":
                money_supply_m2 += value * math.pow(10, 9)
            elif unit == "Thousands":
                money_supply_m2 += value * math.pow(10, 3)

        return money_supply_m2

    def get_money_supply_m2_for_eur_global(self=None):
        money_supply_m2_for_usd_global = 0

        money_supply_m2_for_usd_global += Indicator_Money_Supply_M2.get_money_supply_m2_for_eur_euro_area()

        return money_supply_m2_for_usd_global
# Money Supply M2


# Money Supply M3
class Indicator_Money_Supply_M3:
    def __init__(self):
        pass

    # Money Supply M3 for USD
    def get_money_supply_m3_for_usd_zimbabwe(self=None):
        money_supply_m3 = 0

        headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103'
        }

        url = "https://tradingeconomics.com/zimbabwe/money-supply-m3"

        rt = RequestsTor()

        html_with_tor = rt.get(url, headers=headers)

        soup = BeautifulSoup(html_with_tor.content, 'html.parser')

        element = soup.find('div', id="ctl00_ContentPlaceHolder1_ctl00_ctl00_Panel1")

        if element is not None:
            value = float(element.find('table', {'class': 'table table-hover'})
                          .find_all('tr', {'class': 'datatable-row-alternating'})[1]
                          .find_all('td')[1]
                          .text)

            unit = element \
                .find('table', {'class': 'table table-hover'}) \
                .find_all('tr', {'class': 'datatable-row-alternating'})[1] \
                .find_all('td')[3] \
                .text \
                .split(' ')[1]

            if unit == "Million":
                money_supply_m3 += value * math.pow(10, 6)
            elif unit == "Billion":
                money_supply_m3 += value * math.pow(10, 9)
            elif unit == "Thousands":
                money_supply_m3 += value * math.pow(10, 3)

        return money_supply_m3

    def get_money_supply_m3_for_usd_el_salvador(self=None):
        money_supply_m3 = 0

        headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103'
        }

        url = "https://tradingeconomics.com/el-salvador/money-supply-m3"

        rt = RequestsTor()

        html_with_tor = rt.get(url, headers=headers)

        soup = BeautifulSoup(html_with_tor.content, 'html.parser')

        element = soup.find('div', id="ctl00_ContentPlaceHolder1_ctl00_ctl00_Panel1")

        if element is not None:
            value = float(element.find('table', {'class': 'table table-hover'})
                          .find_all('tr', {'class': 'datatable-row'})[2]
                          .find_all('td')[1]
                          .text)

            unit = element \
                .find('table', {'class': 'table table-hover'}) \
                .find_all('tr', {'class': 'datatable-row'})[2] \
                .find_all('td')[3] \
                .text \
                .split(' ')[1]

            if unit == "Million":
                money_supply_m3 += value * math.pow(10, 6)
            elif unit == "Billion":
                money_supply_m3 += value * math.pow(10, 9)
            elif unit == "Thousands":
                money_supply_m3 += value * math.pow(10, 3)

        return money_supply_m3

    def get_money_supply_m3_for_usd_global(self=None):
        money_supply_m3_for_usd_global = 0

        money_supply_m3_for_usd_global += Indicator_Money_Supply_M3.get_money_supply_m3_for_usd_zimbabwe() \
                                          + Indicator_Money_Supply_M3.get_money_supply_m3_for_usd_el_salvador() \
                                          + Indicator_Money_Supply_M2.get_money_supply_m2_for_usd_belize() \
                                          + Indicator_Money_Supply_M2.get_money_supply_m2_for_usd_ecuador() \
                                          + Indicator_Money_Supply_M2.get_money_supply_m2_for_usd_united_states()

        return money_supply_m3_for_usd_global

    # Money Supply M3 for EUR
    def get_money_supply_m3_for_eur_euro_area(self=None):
        money_supply_m3 = 0

        headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103'
        }

        url = "https://tradingeconomics.com/euro-area/money-supply-m2"

        rt = RequestsTor()

        html_with_tor = rt.get(url, headers=headers)

        soup = BeautifulSoup(html_with_tor.content, 'html.parser')

        element = soup.find('div', id="ctl00_ContentPlaceHolder1_ctl00_ctl00_Panel1")

        if element is not None:
            value = float(element.find('table', {'class': 'table table-hover'})
                          .find_all('tr', {'class': 'datatable-row-alternating'})[1]
                          .find_all('td')[1]
                          .text)

            unit = element \
                .find('table', {'class': 'table table-hover'}) \
                .find_all('tr', {'class': 'datatable-row-alternating'})[1] \
                .find_all('td')[3] \
                .text \
                .split(' ')[1]

            if unit == "Million":
                money_supply_m3 += value * math.pow(10, 6)
            elif unit == "Billion":
                money_supply_m3 += value * math.pow(10, 9)
            elif unit == "Thousands":
                money_supply_m3 += value * math.pow(10, 3)

        return money_supply_m3

    def get_money_supply_m3_for_eur_global(self=None):
        money_supply_m3_for_usd_global = 0

        money_supply_m3_for_usd_global += Indicator_Money_Supply_M3.get_money_supply_m3_for_eur_euro_area()

        return money_supply_m3_for_usd_global
# Money Supply M3

# Money


# Population
class Population:
    def __init__(self):
        pass

    def get_population_for_eu_population(self=None):
        eu_population = 0

        headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103'
        }

        url = "https://tradingeconomics.com/euro-area/population"

        rt = RequestsTor()

        html_with_tor = rt.get(url, headers=headers)

        soup = BeautifulSoup(html_with_tor.content, 'html.parser')

        element = soup.find('div', id="ctl00_ContentPlaceHolder1_ctl00_ctl00_Panel1")

        if element is not None:
            value = float(element
                          .find_all('tr', {'class': 'datatable-row'})[4]
                          .find_all('td')[1]
                          .text)

            eu_population += value * math.pow(10, 6)

        return eu_population


# Population
# Indicators
