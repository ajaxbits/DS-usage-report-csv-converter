import unittest

import pandas as pd
import numpy as np

from csv_converter import (
    substring_row_eliminator,
    extrapolate_column,
    accounts_extrapolated,
    accounts_extrapolated_use_this_one,
)


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
            {
                "A": [1, 2, 3],
                "B": [
                    "Computers > 876596565555 - APPS - wowowowowo > US West (Oregon)",
                    "123",
                    "",
                ],
            }
        )
        desired_df = pd.DataFrame(
            {
                "A": [1, 2, 3],
                "B": [
                    "Computers > 876596565555 - APPS - wowowowowo > US West (Oregon)",
                    "123",
                    "",
                ],
                "C": ["876596565555", "", ""],
            }
        )
        result_df = df
        result_df["C"] = extrapolate_column(df, "B")
        pd.testing.assert_frame_equal(result_df, desired_df)

    def test_full_functionality(self):
        df = pd.DataFrame(
            {
                "A": [1, 2, 3],
                "Computer Group": ["123456789012345678901234567890123", "123", "as"],
                "Cloud Account": ["duhduhduh", "helloworld", "12345"],
            }
        )
        desired_df = pd.DataFrame(
            {
                "A": [1, 2, 3],
                "Computer Group": ["123456789012345678901234567890123", "123", "as"],
                "Cloud Account": ["duhduhduh", "helloworld", "12345"],
                "Cloud Account Extrapolated": ["345678901234", np.nan, np.nan],
            }
        )
        result = accounts_extrapolated(df)
        pd.testing.assert_frame_equal(result, desired_df)

    def test_full_functionality_use_this_one(self):
        df = pd.DataFrame(
            {
                "A": [1, 2, 3],
                "Computer Group": ["123456789012345678901234567890123", "123", "as"],
                "Cloud Account": ["duhduhduh", "helloworld", "12345"],
                "Cloud Account Extrapolated": ["345678901234", np.nan, np.nan],
            }
        )
        desired_df = pd.DataFrame(
            {
                "A": [1, 2, 3],
                "Computer Group": ["123456789012345678901234567890123", "123", "as"],
                "Cloud Account": ["duhduhduh", "helloworld", "12345"],
                "Cloud Account Extrapolated": ["345678901234", np.nan, np.nan],
                "Cloud Account Extrapolated (Use This Column)": [
                    "345678901234",
                    "345678901234",
                    "345678901234",
                ],
            }
        )
        result = accounts_extrapolated_use_this_one(df)
        pd.testing.assert_frame_equal(result, desired_df)


if __name__ == "__main__":
    unittest.main()
