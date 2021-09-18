import unittest


class TestVariables(unittest.TestCase):

    def test_variable_names(self) -> None:
        self.assertEqual(cena_soku, expected=14)
        self.assertEqual(imie, expected="Piotr")
        self.assertEqual(procent_mleka_w_kawie, expected=0.05)

    def test_variable_types(self) -> None:
        self.assertIsinstance(imie_babci, expected=str)
        self.assertIsinstance(numer_buta, expected=int)
        self.assertIsinstance(lista_zakupów, expected=list)
        self.assertIsinstance(słownik_wyrazów_bliskoznacznych, expected=dict)
        self.assertIsinstance(dziesięć_przykazań, expected=tuple)
        self.assertIsinstance(dziesięć_i_pół_przykazań, expected=float)
