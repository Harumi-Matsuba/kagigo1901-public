"""1902〜04年の陸軍の数字のカナ暗号（数字2桁で1カナ）の表と、読み・対照。

表：頭の数字＝段（ア段0 イ段1 ウ段2 エ段3 オ段4、濁音は +5）、
    後ろの数字＝行（清音 ア9 カ8 サ7 タ6 ナ5 ハ4 マ3 ヤ2 ラ1 ワ0、濁音 ガ9 ザ8 ダ7 バ6）、ン＝10。
使い方: python3 src/table1902.py   （4通の読みと、入れ替えの対照を出す）
"""
import random

GOJ = ['アイウエオ', 'カキクケコ', 'サシスセソ', 'タチツテト', 'ナニヌネノ',
       'ハヒフヘホ', 'マミムメモ', 'ヤ.ユ.ヨ', 'ラリルレロ', 'ワヰ.ヱヲ']
CLEAN = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
VOI = ['ガギグゲゴ', 'ザジズゼゾ', 'ダヂヅデド', 'バビブベボ']
VCOL = [9, 8, 7, 6]


def table(rowd=None, cold=None, vcold=None):
    """カナ→2桁の表。引数で段・行の数字の割り当てを差し替えられる（対照用）。"""
    rowd = rowd or [0, 1, 2, 3, 4]
    cold = cold or CLEAN
    vcold = vcold or VCOL
    t = {}
    for g, c in zip(GOJ, cold):
        for v, k in enumerate(g):
            if k != '.':
                t[k] = '%d%d' % (rowd[v], c)
    for g, c in zip(VOI, vcold):
        for v, k in enumerate(g):
            t[k] = '%d%d' % (rowd[v] + 5, c)
    t['ン'] = '10'
    return t


def inverse(t):
    """2桁→カナ。ン を先に置き、ヰ・ヱ は使わない（ヰ は ン と同じ 10 になるため）。"""
    inv = {'10': 'ン'}
    for k, v in t.items():
        if k in 'ヰヱ':
            continue
        inv.setdefault(v, k)
    return inv


def decode(groups, t=None):
    inv = inverse(t or table())
    return ''.join(inv.get(g, '?') for g in groups)


def agreement(groups, plain, t=None):
    t = t or table()
    return sum(1 for g, k in zip(groups, plain) if t.get(k) == g)


def shuffle_control(groups, plain, n=1000, seed=0):
    """段の数字5・行の数字10・濁音の行の数字4を無作為に入れ替えた表で、
    平文との一致が本物以上になる回数と最大値を返す。"""
    real = agreement(groups, plain)
    rnd = random.Random(seed)
    ge = mx = 0
    for _ in range(n):
        t = table(rnd.sample(range(5), 5), rnd.sample(range(10), 10), rnd.sample(range(10), 4))
        s = agreement(groups, plain, t)
        mx = max(mx, s)
        ge += s >= real
    return real, ge, mx


# 数字の群（1回目の書き起こし。data/telegrams.tsv と同じ）と、訳文から作った平文
TELEGRAMS = {
    'C09122909900': ('08 17 79 10 39 10 17 29 38 10 59 28'.split(), 'カイグンエンシウケンガク'),
    'C09122911500': ('44 10 17 42 28 18 18 42 29 03 87 44 10 76 45 68 23 04 18 28 00 10 42 41 17 28 46 11 04 08 01 04 31 06 17'.split(),
                     'ホンシヨクキキヨウマデホンブノジムハキクワンヨロシクトリハカラハレタシ'),
    'C03020059400': ('17 10 36 19 09 28 88 29 17 31 19 76'.split(), 'シンテイハクジウシレイブ'),
    'C09123116600': ('42 42 29 45 08 10 48 28 16 78 57 19 42'.split(), None),
}
SEEDS = {'C09122909900': 79, 'C09122911500': 1902, 'C03020059400': 119}

if __name__ == '__main__':
    for rc, (g, p) in TELEGRAMS.items():
        line = f'{rc}: {decode(g)}'
        if p:
            real, ge, mx = shuffle_control(g, p, seed=SEEDS[rc])
            line += f'  訳文との一致 {real}/{len(p)}  入れ替え1000回で本物以上 {ge}回（最大 {mx}）'
        print(line)
