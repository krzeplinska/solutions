import unittest

cena_soku = 14
imie = "Piotr"
procent_mleka_w_kawie = 0.05
imie_babci= ""
numer_buta = 41
lista_zakupów= []
słownik_wyrazów_bliskoznacznych={}
dziesięć_przykazań=()
dziesięć_i_pół_przykazań=float()

class TestVariables(unittest.TestCase):

    def test_variable_names(self) -> None:
        self.assertEqual(cena_soku, 14)
        self.assertEqual(imie, "Piotr")
        self.assertEqual(procent_mleka_w_kawie, 0.05)

    def test_variable_types(self) -> None:
        self.assertIsInstance(imie_babci, cls=str)
        self.assertIsInstance(numer_buta, cls=int)
        self.assertIsInstance(lista_zakupów, cls=list)
        self.assertIsInstance(słownik_wyrazów_bliskoznacznych, cls=dict)
        self.assertIsInstance(dziesięć_przykazań, cls=tuple)
        self.assertIsInstance(dziesięć_i_pół_przykazań, cls=float)

    def test_changing_variables(self) -> None:
        wiek = 117
        def odmłodź(wiek):
            wiek = wiek -100
            return wiek
        wiek = odmłodź(wiek)
        self.assertEqual(wiek, 17)
        lista_numerów = (112, 5, 80, 115, 45, 49)
        lista_numerów = sorted(lista_numerów)
        self.assertEqual([5, 45, 49, 80, 112, 115], lista_numerów)
