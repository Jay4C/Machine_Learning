import unittest
from Machine_Learning.Supervised_Learning.Forex import tradingeconomics
from Machine_Learning.Supervised_Learning.Forex import worldometers
import statistics
from Machine_Learning.Supervised_Learning.Forex import forex


class UnitTestsSupervisedLearningForex(unittest.TestCase):
    def test_get_the_future_quote_eur_usd_m0(self):
        print('test_get_the_future_quote_eur_usd_m0')

        ratio_eur_usd_m0 = tradingeconomics.Indicator_Money_Supply_M0.get_money_supply_m0_for_eur_global() / \
                           tradingeconomics.Indicator_Money_Supply_M0.get_money_supply_m0_for_usd_global()

        print('ratio_eur_usd_m0 : ' + str(ratio_eur_usd_m0))

    def test_get_the_future_quote_eur_usd_m1(self):
        print('test_get_the_future_quote_eur_usd_m1')

        ratio_eur_usd_m1 = tradingeconomics.Indicator_Money_Supply_M1.get_money_supply_m1_for_eur_global() / \
                           tradingeconomics.Indicator_Money_Supply_M1.get_money_supply_m1_for_usd_global()

        print('ratio_eur_usd_m1 : ' + str(ratio_eur_usd_m1))

    def test_get_the_future_quote_eur_usd_m2(self):
        print('test_get_the_future_quote_eur_usd_m2')

        ratio_eur_usd_m2 = tradingeconomics.Indicator_Money_Supply_M2.get_money_supply_m2_for_eur_global() / \
                           tradingeconomics.Indicator_Money_Supply_M2.get_money_supply_m2_for_usd_global()

        print('ratio_eur_usd_m2 : ' + str(ratio_eur_usd_m2))

    def test_get_the_future_quote_eur_usd_m3(self):
        print('test_get_the_future_quote_eur_usd_m3')

        ratio_eur_usd_m3 = tradingeconomics.Indicator_Money_Supply_M3.get_money_supply_m3_for_eur_global() / \
                           tradingeconomics.Indicator_Money_Supply_M3.get_money_supply_m3_for_usd_global()

        print('ratio_eur_usd_m3 : ' + str(ratio_eur_usd_m3))


class UnitTestsSupervisedLearningForexGlobal(unittest.TestCase):
    def test_get_the_future_quote_eur_usd_global_1(self):
        print('test_get_the_future_quote_eur_usd_global')

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

        print('ratio_eur_usd_global_1 : ' + str(ratio_eur_usd_global_1))

    def test_get_the_future_quote_eur_usd_global_2(self):
        print('test_get_the_future_quote_eur_usd_global_2')

        ratio_eur_usd_global_2 = 0

        us_population = worldometers.Worldometers.get_us_population_live()

        eu_population = tradingeconomics.Population.get_population_for_eu_population()

        ratio_eur_usd_global_2 += float(eu_population/us_population)

        print('ratio_eur_usd_global_2 : ' + str(ratio_eur_usd_global_2))


class UnitTestsSupervisedLearningForexFinal(unittest.TestCase):
    def test_get_the_future_quote_eur_usd_global_final(self):
        print('test_get_the_future_quote_eur_usd_global_final')

        # ratio_eur_usd_global_final
        ratio_eur_usd_global_final = 0

        ratio_eur_usd_global_final += statistics.mean(
            [
                forex.ForexGlobal.get_the_future_quote_eur_usd_global_1(),
                forex.ForexGlobal.get_the_future_quote_eur_usd_global_2()
            ]
        )
        # ratio_eur_usd_global_final

        print("ratio_eur_usd_global_final : " + str(ratio_eur_usd_global_final))


if __name__ == '__main__':
    unittest.main()
