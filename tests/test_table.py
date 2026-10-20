"""表の読みと対照を確かめるテスト。  python3 -m unittest discover -s tests"""
import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / 'src'))
import table1902 as T  # noqa: E402


class TestTable(unittest.TestCase):
    def test_table_is_one_to_one(self):
        t = T.table()
        vals = [v for k, v in t.items() if k not in 'ヰ']
        self.assertEqual(len(vals), len(set(vals)))

    def test_C09122911500_full(self):
        g, p = T.TELEGRAMS['C09122911500']
        self.assertEqual(T.decode(g), p)
        self.assertEqual(T.agreement(g, p), 35)

    def test_C09123116600_reading(self):
        g, _ = T.TELEGRAMS['C09123116600']
        self.assertEqual(T.decode(g), 'ヨヨウノカンコクチズダイヨ')

    def test_partial_readings(self):
        g, p = T.TELEGRAMS['C09122909900']
        self.assertEqual(T.agreement(g, p), 11)
        g, p = T.TELEGRAMS['C03020059400']
        self.assertEqual(T.agreement(g, p), 10)

    def test_shuffle_control(self):
        for rc, seed in T.SEEDS.items():
            g, p = T.TELEGRAMS[rc]
            real, ge, mx = T.shuffle_control(g, p, seed=seed)
            self.assertEqual(ge, 0, rc)
            self.assertLess(mx, real, rc)


if __name__ == '__main__':
    unittest.main()
