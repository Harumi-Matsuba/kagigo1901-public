"""1901年の陸軍の数字のカナ暗号（清国駐在の将校などからの電報）の表と、読み・対照。

表：五十音を段ごとに並べ、濁音・半濁音を清音のすぐ後ろに挟んで、00 から順に番号を振る。
    00 ア カ ガ サ ザ タ ダ ナ ハ バ パ マ ヤ ラ ワ
    15 イ キ ギ シ ジ チ ニ ヒ ビ ピ ミ リ
    27 ウ ク グ ス ズ ツ ヌ フ ブ プ ム ユ ル
    40 エ ケ ゲ セ ゼ テ デ ネ ヘ ベ ペ メ レ
    53 オ コ ゴ ソ ゾ ト ド ノ ホ ボ ポ モ ヨ ロ ン
電報では、機密の語だけをこの2桁に換え、数字を5桁ずつに区切って、残りをローマ字の平文で打つ。
使い方: python3 src/table1901.py   （7通の読みと、表をかき混ぜた対照を出す）
"""
import random

ROWS = ['アカガサザタダナハバパマヤラワ', 'イキギシジチニヒビピミリ', 'ウクグスズツヌフブプムユル',
        'エケゲセゼテデネヘベペメレ', 'オコゴソゾトドノホボポモヨロン']
SEQ = ''.join(ROWS)

# (参照コード, 役割, [(数字の連なり, 訳文・書き込みから期待されるカナ), ...])
# 役割 build＝表の推定に使った電報、test＝表を決めた後に当てた電報、
#      reread＝画像が粗く、表が分かってから読み直した桁を含む電報（一致の数に入れない）
# 期待されるカナは、訳文の語を電報の綴り（ヲ→オ、助詞のハはハかワ）で書いたもの。
TELEGRAMS = [
    ('C09122805800', 'build', [('00161 21108', 'アキヤマハ'), ('08130 62027 0321', 'ハラダチウサニ'),
                               ('00531 62151 15441 35205 18', 'アオキニメイゼラレタシ')]),
    ('C09122805900', 'build', [('00531 660', 'アオキノ')]),
    ('C09122806000', 'build', [('45671 867', 'テンシン')]),
    ('C09122801000', 'build', [('42673 01502', 'ゲンスイガ'), ('54274 51565 26', 'コウテイヨリ')]),
    ('C09122724200', 'reread', [('59153 25427 4515', 'ドイツコウテイ'), ('45676 02748 1501', 'テンノウヘイカ')]),
    ('C09122796200', 'test', [('53645 83718 16530 05329', 'オモトムシキオアオグ')]),
    ('C09122806100', 'test', [('67201 4', 'ンチワ'), ('34283 7', 'フクム')]),
]
# C09122806100 のそのほかの数字（表の外の値 69・91 を含む）は docs/OPEN.md。


def pairs(run):
    d = run.replace(' ', '')
    return [d[i:i + 2] for i in range(0, len(d), 2)]


def decode(run, seq=SEQ):
    return ''.join(seq[int(p)] if int(p) < len(seq) else '・' for p in pairs(run))


def agreement(role=None, seq=SEQ):
    ok = tot = 0
    for _, r, runs in TELEGRAMS:
        if role and r != role:
            continue
        for run, exp in runs:
            got = decode(run, seq)
            tot += len(exp)
            ok += sum(a == b for a, b in zip(got, exp))
    return ok, tot


def control(role='test', n=1000, seed=1901):
    """表の68字を無作為に並べ替えた表で、期待されるカナと合う組の数が本物以上になった回数。"""
    rnd = random.Random(seed)
    real = agreement(role)[0]
    ge = 0
    best = 0
    for _ in range(n):
        s = list(SEQ)
        rnd.shuffle(s)
        a = agreement(role, ''.join(s))[0]
        best = max(best, a)
        ge += a >= real
    return real, ge, best


if __name__ == '__main__':
    for ref, role, runs in TELEGRAMS:
        for run, exp in runs:
            print(ref, role, run, decode(run), exp, 'OK' if decode(run) == exp else 'NG')
    for role in ('build', 'test'):
        ok, tot = agreement(role)
        real, ge, best = control(role)
        print(role, '%d/%d' % (ok, tot), 'かき混ぜ1000回で本物以上', ge, '最大', best)
