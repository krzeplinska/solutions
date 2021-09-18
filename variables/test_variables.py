import unittest


class TestVariables(unittest.TestCase):

    def test_variable_names(self) -> None:
        self.assertEqual(cena_soku, expected=14)
        self.assertEqual(imie, expected="Piotr")
        self.assertEqual(procent_mleka_w_kawie, expected=0.05)
