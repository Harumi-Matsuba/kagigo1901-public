"""1901年、参謀本部（田村少将）から福島少将への起案5通の数字のカナ暗号の表と、読み・対照。

表：2桁でカナ1字。十の位＝段、一の位＝行の格子。
    前半 01〜50：十の位 0ア段 1イ段 2ウ段 3エ段 4オ段、
                 一の位 1ア 2カ 3ガ 4サ 5ザ 6タ 7ダ 8ナ 9ハ 0バ（バ行は 10・20・30・40・50）
    後半 51〜95：十の位 5ア段 6イ段 7ウ段 8エ段 9オ段、
                 一の位 1パ 2マ 3ヤ 4ラ、55＝ワ、65＝ン
    後半の一の位 6〜0 と 75・85・95 は、カナの値としては決まっていない。
    電報に出る 59・60・80・89・99 は語の符号（WORDS）。
着電の表（src/table1901.py）とは別の表。体裁は同じで、機密の語だけを2桁に換え、5桁ずつに区切る。
使い方: python3 src/table1901b.py [JMdict_e のパス]
        （5通の読みと数を出す。辞書のパスを付けると、数字を入れ替えた表との対照も出す）
"""
import random
import re
import sys

G1 = ['アイウエオ', 'カキクケコ', 'ガギグゲゴ', 'サシスセソ', 'ザジズゼゾ',
      'タチツテト', 'ダヂヅデド', 'ナニヌネノ', 'ハヒフヘホ', 'バビブベボ']
G2 = ['パピプペポ', 'マミムメモ', ['ヤ', None, 'ユ', None, 'ヨ'], 'ラリルレロ', ['ワ', 'ン', None, None, None]]


def table(d1=(0, 1, 2, 3, 4), u1=tuple(range(1, 11)), d2=(0, 1, 2, 3, 4), u2=(1, 2, 3, 4, 5)):
    """2桁の値→カナ。引数で段・行の数字の割り当てを差し替えられる（対照用）。"""
    t = {}
    for i, g in enumerate(G1):
        for v in range(5):
            t[d1[v] * 10 + u1[i]] = g[v]
    for i, g in enumerate(G2):
        for v in range(5):
            if g[v]:
                t[50 + d2[v] * 10 + u2[i]] = g[v]
    return t


TABLE = table()

# 表にない値＝語の符号。(語, 史料の裏づけがあるか)。
# 99・60・80 は、1901年3月1日の清国公使来談の筆記（JACAR B03030000800）と 3月2日の電報の突き合わせによる。
# 89・59 は文脈からの推定（59 は 外務省・外務大臣 でも文が通る）。
WORDS = {99: ('露', True), 60: ('清', True), 80: ('公使', True), 89: ('独', False), 59: ('政府', False)}

# (参照コード, 日付, [(数字の連なり＝1回目の書き起こし, 読み直した連なり または None), ...])
# 1回目の書き起こしは、表が分かる前に画像から読んだもの。
# 読み直しは、表が分かってから画像を見直して変えた桁（4か所）。そのうち C09122810100 の2か所は、
# 表を知らない2回目の読み手（Codex）も同じ桁を読んだ。C09122809400 の2か所は2回目の読み手が1回目と同じに読んだので、推定として扱う。
TELEGRAMS = [
    ('C09122808300', '1901-02', [('02624 14832 4221', None), ('1982 1518', None)]),
    ('C09122808400', '1901-02-14', [('41411 45248', None), ('22244 83409', None), ('14100 94618', None)]),
    ('C09122809400', '1901-03-02', [
        ('99506 22652 2248', None), ('5503', None), ('64422 11493 2109 6080', None), ('5918', None),
        ('99603 52109', None), ('43962 14222 09118 40306', '43162 14222 09118 40306'),
        ('5918 36211 44721', None), ('35215 32248', None),
        ('34110 16598 6492', '34110 16593 6492'), ('37659 12112', None)]),
    ('C09122810100', '1901-03-08', [
        ('33652 41109 42291 42155 65936 41849 6518', '33652 41109 42211 42155 65936 41849 6518'),
        ('92168 98048', None), ('02844 11912', None), ('55840 94427', '55840 94421'),
        ('93212 40884 09626 57321', None)]),
    ('C09122812300', '1901-05-01', [('12362 12474', None), ('42210 61139 11482 42109 8003', None), ('48456 241', None)]),
]

# 読みに数えない組（電報, 連なりの番号, 組の番号）：表にある値だが、語として確かでないもの。
DOUBTFUL = {
    ('C09122808300', 0, 4),   # 32＝ケ（ケコウ）
    ('C09122809400', 0, 1),   # 50＝ボ（99506。60＝清 の書き誤りとみる・推定）
    ('C09122809400', 0, 4),   # 52＝マ（ミツマク。ヤ＝53 なら密約）
    ('C09122809400', 5, 1),   # 96→16＝チ（読み直し。2回目の読み手は 96）
    ('C09122809400', 8, 4),   # 98→93＝ヨ（読み直し。2回目の読み手は 98）
    ('C09122810100', 1, 0),   # 92＝モ
    ('C09122810100', 1, 1),   # 16＝チ
    ('C09122810100', 4, 6),   # 62＝ミ（ミンユウ。マ＝52 なら漫遊）
}


def pairs(run):
    d = re.sub(r'\s', '', run)
    return [int(d[i:i + 2]) for i in range(0, len(d), 2)]


def decode(run, t=None):
    t = t or TABLE
    return ''.join(t.get(p, '[%02d]' % p) for p in pairs(run))


def decode_words(run):
    """語の符号を語に置き換えた読み。推定の語には ? を付ける。"""
    out = []
    for p in pairs(run):
        if p in TABLE:
            out.append(TABLE[p])
        elif p in WORDS:
            out.append('[%s%s]' % (WORDS[p][0], '' if WORDS[p][1] else '?'))
        else:
            out.append('[%02d]' % p)
    return ''.join(out)


def readings(reread=True):
    """(参照コード, 連なりの番号, 使った連なり, 読み) の一覧。"""
    out = []
    for ref, _, runs in TELEGRAMS:
        for i, (first, second) in enumerate(runs):
            run = second if (reread and second) else first
            out.append((ref, i, run, decode(run)))
    return out


def counts():
    """電報ごとの (組の数, 表にある値の組, 読みに数える組)。読みに数える組には、裏づけのある語の符号を含む。"""
    res = {}
    for ref, _, runs in TELEGRAMS:
        n = intab = sense = 0
        for i, (first, second) in enumerate(runs):
            for j, p in enumerate(pairs(second or first)):
                n += 1
                if p in TABLE:
                    intab += 1
                    if (ref, i, j) not in DOUBTFUL:
                        sense += 1
                elif WORDS.get(p, ('', False))[1]:
                    sense += 1
        res[ref] = (n, intab, sense)
    return res


# ---- 対照：公開の辞書（JMdict）の読みで覆えるカナの数 ----
SMALL = str.maketrans('ァィゥェォャュョッヮ', 'アイウエオヤユヨツワ')


def load_words(jmdict_path):
    """JMdict の <reb>（読み）を片仮名・大書きにそろえ、3字以上のものを集める。ヲ は オ にする。"""
    words = set()
    for m in re.finditer(r'<reb>([^<]+)</reb>', open(jmdict_path, encoding='utf-8').read()):
        w = ''.join(chr(ord(c) + 0x60) if 'ぁ' <= c <= 'ゖ' else c for c in m.group(1)).translate(SMALL)
        if len(w) >= 3 and re.fullmatch(r'[ア-ヴ]+', w):
            words.add(w.replace('ヲ', 'オ'))
    return words


def cover(t, seqs, words, maxlen):
    """連なりごとに、重ならない辞書の語（3字以上）で覆えるカナの数の最大を足す。"""
    tot = 0
    for ps in seqs:
        s = ''.join(t.get(p, '?') for p in ps)
        best = [0] * (len(s) + 1)
        for i in range(1, len(s) + 1):
            best[i] = best[i - 1]
            for n in range(3, min(maxlen, i) + 1):
                if s[i - n:i] in words:
                    best[i] = max(best[i], best[i - n] + n)
        tot += best[len(s)]
    return tot


def control(words, reread=False, n=1000, seed=1901):
    """段・行の数字を入れ替えた表と、字を総入れ替えした表で、覆えるカナの数が本物以上になった回数。"""
    seqs = [pairs(r) for _, _, r, _ in readings(reread)]
    maxlen = max(map(len, words))
    real = cover(TABLE, seqs, words, maxlen)
    rnd = random.Random(seed)
    ge = mx = 0
    for _ in range(n):
        t = table(rnd.sample(range(5), 5), rnd.sample(range(1, 11), 10), rnd.sample(range(5), 5), rnd.sample(range(1, 6), 5))
        c = cover(t, seqs, words, maxlen)
        mx = max(mx, c)
        ge += c >= real
    codes = sorted(TABLE)
    kana = [TABLE[c] for c in codes]
    ge2 = mx2 = 0
    for _ in range(n):
        k = kana[:]
        rnd.shuffle(k)
        c = cover(dict(zip(codes, k)), seqs, words, maxlen)
        mx2 = max(mx2, c)
        ge2 += c >= real
    return real, ge, mx, ge2, mx2


if __name__ == '__main__':
    for ref, i, run, text in readings():
        print(ref, i, run, text, decode_words(run) if '[' in text else '')
    tot = [0, 0, 0]
    for ref, c in counts().items():
        print(ref, '組 %d 表にある値 %d 読みに数える %d' % c)
        tot = [a + b for a, b in zip(tot, c)]
    print('合計', '組 %d 表にある値 %d 読みに数える %d' % tuple(tot))
    if len(sys.argv) > 1:
        w = load_words(sys.argv[1])
        for rr in (False, True):
            print('読み直し' + ('あり' if rr else 'なし'), '本物 %d、段・行の入れ替えで本物以上 %d回（最大 %d）、総入れ替えで %d回（最大 %d）' % control(w, rr))
