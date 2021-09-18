import unittest


class TestVariables(unittest.TestCase):

    def test_variable_names(self) -> None:
        self.assertEqual(cena_soku, 14)
        self.assertEqual(imie, "Piotr")
        self.assertEqual(procent_mleka_w_kawie, 0.05)
