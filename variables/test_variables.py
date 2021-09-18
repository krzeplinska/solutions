import unittest


class TestVariables(unittest.TestCase):

    def test_variable_names(self) -> None:
        self.assertEqual(cena_soku, expected=14)
        self.assertEqual(imie, expected="Piotr")
        self.assertEqual(procent_mleka_w_kawie, expected=0.05)

    def test_variable_types(self) -> None:
        self.assertIsInstance(imie_babci, cls=str)
        self.assertIsInstance(numer_buta, cls=int)
        self.assertIsInstance(lista_zakupów, cls=list)
        self.assertIsInstance(słownik_wyrazów_bliskoznacznych, cls=dict)
        self.assertIsInstance(dziesięć_przykazań, cls=tuple)
        self.assertIsInstance(dziesięć_i_pół_przykazań, cls=float)
