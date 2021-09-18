import unittest


class TestVariables(unittest.TestCase):

    def test_variable_names(self) -> None:
        self.assertEqual(cena_soku, expected=14)
        self.assertEqual(imie, expected="Piotr")
        self.assertEqual(procent_mleka_w_kawie, expected=0.05)

    def test_variable_types(self) -> None:
        self.assertIsinstance(imie_babci, str)
        self.assertIsinstance(numer_buta, int)
        self.assertIsinstance(lista_zakupów, list)
        self.assertIsinstance(słownik_wyrazów_bliskoznacznych, dict)
        self.assertIsinstance(dziesięć_przykazań, tuple)
        self.assertIsinstance(dziesięć_i_pół_przykazań, float)
