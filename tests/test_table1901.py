"""1901年の表の読みと対照を確かめるテスト。  python3 -m unittest discover -s tests"""
import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / 'src'))
import table1901 as T  # noqa: E402


class TestTable1901(unittest.TestCase):
    def test_table_shape(self):
        self.assertEqual(len(T.SEQ), 68)
        self.assertEqual(len(set(T.SEQ)), 68)
        self.assertEqual(T.SEQ[0], 'ア')
        self.assertEqual(T.SEQ[67], 'ン')

    def test_all_runs_have_even_length(self):
        for _, _, runs in T.TELEGRAMS:
            for run, exp in runs:
                self.assertEqual(len(run.replace(' ', '')) % 2, 0)
                self.assertEqual(len(T.pairs(run)), len(exp))

    def test_readings(self):
        for _, _, runs in T.TELEGRAMS:
            for run, exp in runs:
                self.assertEqual(T.decode(run), exp)

    def test_held_out_telegrams(self):
        self.assertEqual(T.agreement('test'), (16, 16))
        self.assertEqual(T.agreement('build'), (42, 42))

    def test_control(self):
        real, ge, best = T.control('test', n=1000)
        self.assertEqual(real, 16)
        self.assertEqual(ge, 0)
        self.assertLess(best, 8)


if __name__ == '__main__':
    unittest.main()
