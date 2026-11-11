# Three General Staff drafts of May-June 1901 (C09122813500, C09122814000, C09122815900)

Added on 11 November 2026. These three drafts follow the five drafts to Maj.-Gen. Fukushima ([READING1901B.en.md](READING1901B.en.md)) in the same binder. All three carry either a plaintext draft or kana glosses, so the plaintext of the enciphered parts is known. What was examined here is which table they were written with.

## C09122813500 (31 May, Vice-Chief of Staff to Lt.-Gen. Yamaguchi, no. 113): written with the table of the incoming telegrams (00-67)
- Sheet 1 is the plaintext draft; sheet 2 is the same draft with kanji numerals and kana written beside it. Only names and posts are put into figures (new garrison commander Ōshima Hisanao, chief of staff Akiyama Yoshifuru, staff officers Tachibana Koichirō, Suzuki Tomosuke, Sakai Haruzō, adjutants Iida Eizō and others, chief surgeon Shōda Kitarō, intendant …, Tianjin garrison commander Yamane Takesuke …).
- Three readings (the JACAR catalogue transcription, the first reader's view of the image, and OpenAI Codex given neither plaintext nor table) were set beside the values that the incoming table ([READING1901.en.md](READING1901.en.md)) gives. Of the 20 words read (97 pairs as given by the table), all but two places follow the incoming table.
  - 新 18 67, 駐 20 38, 屯 58 67, 軍 29 67, 司令官 18 52 15 01 67, 大島久直 53 53 18 11 16 27 20 65 28, 秋山好 00 16 12 11 65 18, 鈴木朝資 30 31 16 58 64 30 41, 春蔵 08 39 57 27, 副官 34 28 01 67, 飯田栄三 15 15 06 40 15 57 27, 庄田喜太郎 18 65 27 06 16 05 66 27 and others.
  - Disagreements: in 立花 (Tachibana) タ and バ are written 06 and 10 (the table has ダ and パ there; all three readings agree). For ボ in 参謀長 and 参謀 the catalogue has 65 and 63 against 62 in the table (the image does not settle it). Codex reads ブ in 医部長 and 監督部長 as 36 (the table has 35).
- **The value 68, outside the table, stands for the numeral 一 ("one").** 立花小一郎 (Tachibana Koichirō) is 06 20 10 07 54 **68** 66 27 (タチバナ・コ・一・ロウ; タ and バ one above the table, as noted). The catalogue transcription ("五四六八六六二七" with the kana コーロウ), the first reader and Codex ("686627") agree. As 68, the value after the last kana (67 = ン), is the numeral 一, values from 68 up appear to be codes for numerals or words. In C09122806100, 69 (the ニ of 任地ハ) would read if 69 = 二 ("two") (conjecture; one occurrence). 91 is not settled.
- In the second half (from the Tianjin garrison on) the thin numerals are lost in the bilevel image; neither the first reader nor Codex can pick up the digits.
- Codex's readings per strip: [second/C09122813500_codex.txt](../second/C09122813500_codex.txt).

## C09122814000 (3 June, Vice-Chief Terauchi to Maj. Tachibana) and C09122815900 (June, telegram in Latin script on the merit survey): a third table
- C09122815900 is a romaji telegram with two runs of two-digit pairs, glossed with katakana above the pairs: 28 10 37 18 16 42 29 17 (ク ン セ キ チ ヨ ウ サ = 勲績調査, merit survey) and 85 18 10 16 29 58 19 (ペ キ ン チ ウ ザ イ = 北京駐在, stationed in Peking).
- C09122814000 has numerals beside the draft phrase 遅クモ十月頃迄交代セシムル ("relieve him by October at the latest"). 49 47 with the gloss オソ, then 28 43 (クモ) and 48 29 06 19 (コウタイ) can be read in the image. 99 41 (ゴロ) and 37 17 23 21 (セシムル) are the catalogue transcription ("七九九四一四", "三、七一七二三、二一") divided anew; they were not checked in the image.
- These 20 values are explained by the same grid as the table of the drafts to Fukushima ([READING1901B.en.md](READING1901B.en.md)), tens digit = vowel row, but with the consonant columns numbered in reverse and the voiced sounds moved to the upper half:
  - lower half: units 9 a, 8 ka, 7 sa, 6 ta, 5 na, 4 ha, 3 ma, 2 ya, 1 ra, 0 wa (tens 0-4 = a, i, u, e, o)
  - upper half: units 9 ga, 8 za, 7 da, 6 ba, 5 pa (tens 5-9 = a, i, u, e, o); 10 = ン.
  - The rule was worked out from the glossed values, so agreement with them (28 of 28 kana) is no test. Only ゴロ, コウタイ and セシムル, read with the rule after it was set up (the ra column = 1 first appears there), are an outside check; ゴロ and セシムル rest on the catalogue transcription.
  - The 17 of 15900 has a gloss that looks like サ, but the table gives シ (the same value as the シ of セシムル in 14000).
  - The place of 十月 (93 and some illegible digits after it) is not settled. 93 has units digit 3 in the upper half, not a kana cell, and may be a code for the numeral 十 (conjecture).
- Table: [src/table1901c.py](../src/table1901c.py).

## Taken together
- In the drafts of the same binder, those to Fukushima (February-May) use the grid table, the one to Yamaguchi (Tianjin, 31 May) the table of the incoming telegrams, and the June ones to Tachibana and on the merit survey a third table. The table changed with the date or with the correspondent.
- Both the incoming table and the grid table have values outside the kana for numerals or words (68 = 一 in the incoming table; 59, 60, 80, 89, 99 in the grid table).

## Human check
No human has checked the transcriptions. The readings are by AI (first reader Claude Opus 5.5, second reader OpenAI Codex gpt-6-astra, reasoning high).
