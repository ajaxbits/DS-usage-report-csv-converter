import unittest

import pandas as pd
import numpy as np

from csv_converter import substring_row_eliminator, extrapolate_column


class TestEliminator(unittest.TestCase):
    def test_tame_elimination(self):
        df = pd.DataFrame(dict(A=[5, 3, 5, 6], C=["foo", "bar", "fooXYZbar", "bat"]))
        desired_df = pd.DataFrame(dict(A=[5, 3, 6], C=["foo", "bar", "bat"]))
        no_fly_list = ["XYZ"]
        sanitized_df = substring_row_eliminator("C", no_fly_list, df)
        self.assertEqual(sanitized_df.values.all(), desired_df.values.all())


class TestExtrapolate(unittest.TestCase):
    def test_extrapolation(self):
        df = pd.DataFrame(
            {"A": [1, 2, 3], "B": ["123456789012345678901234567890123", "123", ""]}
        )
        desired_df = pd.DataFrame(
            {
                "A": [1, 2, 3],
                "B": ["123456789012345678901234567890123", "123", ""],
                "C": ["23", np.nan, np.nan],
            }
        )
        result_df = df
        result_df["C"] = extrapolate_column(df, "B")
        self.assertEqual(
            extrapolate_column(df, "B").values.all(), desired_df.values.all()
        )


if __name__ == "__main__":
    unittest.main()
