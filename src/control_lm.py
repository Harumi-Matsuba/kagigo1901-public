"""訳文のない C09123116600 の読みの対照（カナ2字の連なりの尤度）。

使い方: python3 src/control_lm.py コーパス.txt
  コーパス.txt は平文のカナ電報の文（1行に1つ）。2026-10-20 の値は、JACAR の目録の内容欄から
  8字以上のカタカナの連なりを集めた 18,810字（この電報自身は除く）で出した。目録の文なので同梱していない。
"""
import collections
import math
import random
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import table1902 as T  # noqa: E402

C = T.TELEGRAMS['C09123116600'][0]


def main(path):
    txt = [m for line in open(path, encoding='utf-8') for m in re.findall(r'[ァ-ヶー]{8,}', line)]
    corpus = '｜'.join(txt)
    uni = collections.Counter(corpus)
    bi = collections.Counter(zip(corpus, corpus[1:]))
    V = len(uni) + 1

    def lp(s):
        return sum((math.log((bi[(a, b)] + 0.5) / (uni[a] + 0.5 * V)) if '?' not in (a, b) else -2 * math.log(V))
                   for a, b in zip(s, s[1:]))

    real = T.decode(C)
    rs = lp(real)
    rnd = random.Random(1904)
    ge, best = 0, None
    for _ in range(1000):
        t = T.table(rnd.sample(range(5), 5), rnd.sample(range(10), 10), rnd.sample(range(10), 4))
        s = T.decode(C, t)
        sc = lp(s)
        ge += sc >= rs
        if best is None or sc > best[0]:
            best = (sc, s)
    print(f'学習のカナ {len(corpus)}字  本物 {real} {rs:.1f}  入れ替えで本物以上 {ge}/1000  最良 {best[1]} {best[0]:.1f}')


if __name__ == '__main__':
    main(sys.argv[1])
