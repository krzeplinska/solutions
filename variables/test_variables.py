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

    def test_changing_variables(self) -> None:
        wiek = 117
        wiek = odmłodź(wiek)
        def odmłódź(wiek):
            #tu napisz rozwiązanie
        self.assertEqual(wiek, expected=17)
        lista_numerów = list(112, 5, 80, 115, 45, 49)
        #tu napisz rozwiązanie
        self.assertEqual([5, 45, 49, 80, 112, 115], lista_numerów)
