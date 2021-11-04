import unittest
from varasto import Varasto


class TestVarasto(unittest.TestCase):
    def setUp(self):
        self.varasto = Varasto(10)

    def test_konstruktori_luo_tyhjan_varaston(self):
        # https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertAlmostEqual
        self.assertAlmostEqual(self.varasto.saldo, 0)

    def test_uudella_varastolla_oikea_tilavuus(self):
        self.assertAlmostEqual(self.varasto.tilavuus, 10)

    def test_lisays_lisaa_saldoa(self):
        self.varasto.lisaa_varastoon(8)

        self.assertAlmostEqual(self.varasto.saldo, 8)

    def test_lisays_lisaa_pienentaa_vapaata_tilaa(self):
        self.varasto.lisaa_varastoon(8)

        # vapaata tilaa pitäisi vielä olla tilavuus-lisättävä määrä eli 2
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 2)

    def test_ottaminen_palauttaa_oikean_maaran(self):
        self.varasto.lisaa_varastoon(8)

        saatu_maara = self.varasto.ota_varastosta(2)

        self.assertAlmostEqual(saatu_maara, 2)

    def test_ottaminen_lisaa_tilaa(self):
        self.varasto.lisaa_varastoon(8)

        self.varasto.ota_varastosta(2)

        # varastossa pitäisi olla tilaa 10 - 8 + 2 eli 4
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 4)

    def test_negatiivinen_varasto(self):
        self.varasto = Varasto(-2)
        self.assertEqual(self.varasto.tilavuus, 0)

    def test_alkusaldo_negatiivinen(self):
        self.varasto = Varasto(0, -1)
        self.assertEqual(self.varasto.saldo, 0)

    def test_negatiivinen_maara(self):
        self.assertIsNone(self.varasto.lisaa_varastoon(-1))

    def test_yli_tilavuuden(self):
        self.varasto.lisaa_varastoon(self.varasto.paljonko_mahtuu()+1)
        self.assertEqual(self.varasto.saldo, self.varasto.tilavuus)

    def test_ottaminen_ei_ole_negatiivinen(self): 
        self.assertEqual(self.varasto.ota_varastosta(-1), 0)

    def test_ota_varastostosta_liikaa(self):
        saldo = self.varasto.saldo
        self.assertEqual(saldo, self.varasto.ota_varastosta(self.varasto.saldo+1) )

    def test_str(self):
        self.assertEqual(f"saldo = {self.varasto.saldo}, vielä tilaa {self.paljonko_mahtuu()}" , str(self.varasto))