from konto import Konto
import unittest


class NamesTestCase(unittest.TestCase):
    def test_saldo(self):
        konto = Konto(10000)
        saldo = konto.saldo
        self.assertEqual(saldo, 10000)

    def test_wyplata_fail(self):
        konto = Konto(10000)
        saldo = konto.wyplata(100000)
        self.assertEqual(saldo, "no money")
        self.assertEqual(konto.saldo, 10000)

    def test_wyplata(self):
        konto = Konto(9000)
        saldo = konto.wyplata(1000)
        self.assertEqual(saldo, 8000)

    def test_wplata(self):
        konto = Konto(159000)
        saldo = konto.wplata(1000)
        self.assertEqual(saldo, 160000)


unittest.main()

