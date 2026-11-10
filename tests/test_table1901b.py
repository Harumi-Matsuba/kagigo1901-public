"""1901年の発信側の表の読みを確かめるテスト。  python3 -m unittest discover -s tests"""
import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / 'src'))
import table1901b as B  # noqa: E402


class TestTable1901b(unittest.TestCase):
    def test_table_shape(self):
        self.assertEqual(len(B.TABLE), 70)
        self.assertEqual(len(set(B.TABLE.values())), 70)
        for code, kana in ((1, 'ア'), (10, 'バ'), (14, 'シ'), (21, 'ウ'), (41, 'オ'), (48, 'ノ'),
                           (50, 'ボ'), (51, 'パ'), (52, 'マ'), (55, 'ワ'), (64, 'リ'), (65, 'ン'), (93, 'ヨ')):
            self.assertEqual(B.TABLE[code], kana)

    def test_all_runs_have_even_length(self):
        for _, _, runs in B.TELEGRAMS:
            for first, second in runs:
                for r in (first, second):
                    if r:
                        self.assertEqual(len(r.replace(' ', '')) % 2, 0)

    def test_readings_first_transcription(self):
        got = {(ref, i): text for ref, i, _, text in B.readings(reread=False)}
        self.assertEqual(got[('C09122808300', 1)], 'ヒメジニ')
        self.assertEqual(got[('C09122808400', 0)], 'オオシマノ')
        self.assertEqual(got[('C09122808400', 1)], 'クスノセハ')
        self.assertEqual(got[('C09122808400', 2)], 'シバハトニ')
        self.assertEqual(got[('C09122809400', 1)], 'ワガ')
        self.assertEqual(got[('C09122809400', 2)], 'リコウシヨウハ[60][80]')
        self.assertEqual(got[('C09122809400', 6)], '[59]ニテウシドウ')
        self.assertEqual(got[('C09122809400', 7)], 'ゼウヤクノ')
        self.assertEqual(got[('C09122809400', 9)], 'デンポウキ')
        self.assertEqual(got[('C09122810100', 2)], 'カレオヒキ')
        self.assertEqual(got[('C09122812300', 0)], 'キテウスル')
        self.assertEqual(got[('C09122812300', 1)], 'コウタイヘイノスウハ[80]ガ')
        self.assertEqual(got[('C09122812300', 2)], 'ノゾミオ')

    def test_readings_reread(self):
        got = {(ref, i): text for ref, i, _, text in B.readings(reread=True)}
        self.assertEqual(got[('C09122810100', 0)], 'ゲンスイハコウシウワンヨリニホンニ')
        self.assertEqual(got[('C09122810100', 3)], 'ワレハソウ')
        self.assertEqual(got[('C09122809400', 5)], 'ゴチウコクハイレガタ')
        self.assertEqual(got[('C09122809400', 8)], 'セイアンヨリモ')

    def test_word_codes(self):
        self.assertEqual(B.decode_words('64422 11493 2109 6080'), 'リコウシヨウハ[清][公使]')
        self.assertEqual(B.decode_words('99603 52109'), '[露][清]ゼウハ')
        self.assertEqual(B.decode_words('92168 98048'), 'モチ[独?][公使]ノ')
        self.assertEqual(B.decode_words('5918'), '[政府?]ニ')
        self.assertFalse(set(B.WORDS) & set(B.TABLE))

    def test_counts(self):
        c = B.counts()
        self.assertEqual(c['C09122808300'], (11, 11, 10))
        self.assertEqual(c['C09122808400'], (15, 15, 15))
        self.assertEqual(c['C09122809400'], (59, 52, 53))
        self.assertEqual(c['C09122810100'], (42, 40, 38))
        self.assertEqual(c['C09122812300'], (21, 20, 21))
        self.assertEqual(tuple(sum(x) for x in zip(*c.values())), (148, 138, 137))


if __name__ == '__main__':
    unittest.main()
