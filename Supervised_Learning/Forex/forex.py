import statistics

from Machine_Learning.Supervised_Learning.Forex import tradingeconomics
from Machine_Learning.Supervised_Learning.Forex import worldometers


class ForexGlobal:
    def __init__(self):
        pass

    def get_the_future_quote_eur_usd_global_1(self=None):
        ratio_eur_usd_global_1 = 0

        ratio_eur_usd_m0 = tradingeconomics.Indicator_Money_Supply_M0.get_money_supply_m0_for_eur_global() / \
                           tradingeconomics.Indicator_Money_Supply_M0.get_money_supply_m0_for_usd_global()

        ratio_eur_usd_m1 = tradingeconomics.Indicator_Money_Supply_M1.get_money_supply_m1_for_eur_global() / \
                           tradingeconomics.Indicator_Money_Supply_M1.get_money_supply_m1_for_usd_global()

        ratio_eur_usd_m2 = tradingeconomics.Indicator_Money_Supply_M2.get_money_supply_m2_for_eur_global() / \
                           tradingeconomics.Indicator_Money_Supply_M2.get_money_supply_m2_for_usd_global()

        ratio_eur_usd_m3 = tradingeconomics.Indicator_Money_Supply_M3.get_money_supply_m3_for_eur_global() / \
                           tradingeconomics.Indicator_Money_Supply_M3.get_money_supply_m3_for_usd_global()

        ratio_eur_usd_global_1 += ratio_eur_usd_m0 + ratio_eur_usd_m1 + ratio_eur_usd_m2 + ratio_eur_usd_m3

        return ratio_eur_usd_global_1

    def get_the_future_quote_eur_usd_global_2(self=None):
        ratio_eur_usd_global_2 = 0

        us_population = worldometers.Worldometers.get_us_population_live()

        eu_population = tradingeconomics.Population.get_population_for_eu_population()

        ratio_eur_usd_global_2 += float(eu_population/us_population)

        return ratio_eur_usd_global_2


class ForexFinal:
    def __init__(self):
        pass

    def get_the_future_quote_eur_usd_global_final(self=None):
        # ratio_eur_usd_global_final
        ratio_eur_usd_global_final = 0

        ratio_eur_usd_global_final += statistics.mean(
            [
                ForexGlobal.get_the_future_quote_eur_usd_global_1(),
                ForexGlobal.get_the_future_quote_eur_usd_global_2()
            ]
        )
        # ratio_eur_usd_global_final

        return ratio_eur_usd_global_final