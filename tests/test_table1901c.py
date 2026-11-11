"""1901年6月の起案の表（表C）のテスト。  python3 -m unittest discover -s tests"""
import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / 'src'))
import table1901c as C  # noqa: E402


class TestTable1901c(unittest.TestCase):
    def test_values_unique(self):
        self.assertEqual(len(set(C.TABLE.values())), len(C.TABLE))

    def test_attested(self):
        for ref, v, kana, _ in C.ATTESTED:
            got = C.decode(v)
            for a, b in zip(got, kana):
                if b != '?':
                    self.assertEqual(a, b, (ref, v))

    def test_some_cells(self):
        for code, kana in ((49, 'オ'), (47, 'ソ'), (28, 'ク'), (43, 'モ'), (99, 'ゴ'), (41, 'ロ'),
                           (6, 'タ'), (19, 'イ'), (85, 'ペ'), (58, 'ザ'), (10, 'ン'), (17, 'シ')):
            self.assertEqual(C.TABLE[code], kana)


if __name__ == '__main__':
    unittest.main()
