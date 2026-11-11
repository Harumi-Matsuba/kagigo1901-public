# A Japanese Army numeric kana cipher of 1902–04 (telegrams in JACAR): table and readings

This repository records the reconstruction of a cipher used by the Imperial Japanese Army in domestic telegrams in 1902–04, in which **two digits stand for one kana**, and the reading of four telegrams. The table is a coordinate system: the first digit gives the vowel row of the Japanese syllabary (gojūon dan) and the second digit the consonant column (gyō). The same table was used unchanged from March 1902 (Osaka) to January 1904 (Kokura, Moji).

日本語: [README.md](README.md).

## Addition: three drafts of May-June 1901 (2026-11-11)
- The three drafts that follow the five drafts to Fukushima in the same binder were viewed in the images ([docs/READING1901C.en.md](docs/READING1901C.en.md)). They carry a plaintext draft or kana glosses, so the plaintext of the enciphered parts is known; the question was which table they use.
- **C09122813500 (31 May, to Lt.-Gen. Yamaguchi) uses the table of the incoming telegrams.** The 20 words read (97 pairs) follow that table except in two places. **The value 68, outside the table, is the numeral 一** (the 一 of 立花小一郎; the catalogue transcription, the first reader and Codex agree). The second half cannot be read in the image.
- **C09122814000 (3 June, to Maj. Tachibana) and C09122815900 (telegram on the merit survey) use a third table**: tens digit = vowel row as in the grid of the Fukushima drafts, but with the consonant columns numbered in reverse (9 a, 8 ka, 7 sa, 6 ta, 5 na, 4 ha, 3 ma, 2 ya, 1 ra, 0 wa; upper half 9 ga, 8 za, 7 da, 6 ba, 5 pa). Worked out from 20 glossed values ([src/table1901c.py](src/table1901c.py)); three words read after the rule was set up (ゴロ, コウタイ, セシムル) also fit.
- **No human has checked the transcriptions.** First reader Claude Opus 5.5, second reader OpenAI Codex gpt-6-astra (reasoning high).

## Addition: the 1901 table of the outgoing drafts (2026-11-10)
- **Status: a table found; two drafts are full readings, three are partial readings.** Five drafts from the General Staff (Maj.-Gen. Tamura) to Maj.-Gen. Fukushima in Peking, February–May 1901 (catalogue 715 of the Cyphersolver ledger). No contemporary translation has been found. Within the range searched on 2026-11-10 (the added section of [docs/PRIOR_CHECK.en.md](docs/PRIOR_CHECK.en.md)), no earlier reading and no printed plaintext was found. This is not a claim to be the first.
- **The table**: two digits per kana, a grid with tens digit = vowel row and units digit = consonant column. Lower half 01–50: tens 0–4 = a i u e o; units 1 ア, 2 k, 3 g, 4 s, 5 z, 6 t, 7 d, 8 n, 9 h, 0 b. Upper half 51–95: tens 5–9 = a i u e o; units 1 p, 2 m, 3 y, 4 r; 55 = ワ, 65 = ン. It is not the table of the incoming telegrams (below). In full, with the reading: [docs/READING1901B.en.md](docs/READING1901B.en.md).
- **Reading** ([ ] = word code, ? = conjecture; 〔 〕 = doubtful kana. Word codes: 99 = Russia, 60 = China, 80 = minister, 89 = Germany?, 59 = government?):
  - C09122808400 (14 Feb): 大島ノ事ハ今相談中、若シ行ケネバ楠瀬ハ如何、柴ハ兎ニ角返ス — "The matter of Ōshima is under discussion now. If he cannot go, how about Kusunose? Shiba will be sent back in any case." (full reading)
  - C09122812300 (1 May): 帰朝スル様ニ…ナレリ、又交代兵ノ数ハ[公使]ガ…ザレバ望ミヲ充タシ難シ — "… is to return home. Also, as to the number of relief troops, unless the Minister …, the wish is hard to meet." (full reading; the readers disagree on the romaji of the verb)
  - C09122808300 (Feb): 神尾ノ〔ケコウ〕許サズ、姫路ニ遣ル積リ — "Kamio's 〔…〕 does not permit; we intend to send him to Himeji." (ケコウ is taken as 健康, health, with ン dropped; conjecture)
  - C09122809400 (2 Mar): to our advice that the Russo-〔Chinese〕 secret agreement is disadvantageous, Li Hongzhang had the Chinese Minister tell [the Government?] that … the advice is hard to accept …; Zhang Zhidong has asked our [Government?] that this treaty should not come into being; a telegram of the same meaning has come from Xi'an.
  - C09122810100 (8 Mar): the Field Marshal wishes to come to Japan from Kiaochow Bay … 〔モチ〕 the [German?] Minister … sounding out how he would be received; if it looks as though we shall receive him suitably, recommend the 〔pleasure〕 trip.
- **Numbers**: of 148 pairs, 138 have a value in the table and 137 are counted as read (92.6%; by telegram 90.9%, 100%, 89.8%, 90.5%, 100%; this includes 7 pairs of word codes supported by a record). Control: none of 1,000 tables with permuted digits did as well as the real one (kana covered by dictionary words: real 58, max 37). Digit agreement with the independent second transcription (Codex): 285/296 (96.3%); lowest per telegram 92.4% for C09122809400 (89.8% when counted by two-digit pairs). No calibration ([docs/METHOD.en.md](docs/METHOD.en.md) §10).
- **Not read**: five values outside the table (59, 60, 80, 89, 99; probably codes for words), the first group of C09122809400, and a few kana that do not fit a word ([docs/OPEN.en.md](docs/OPEN.en.md) §1b).
- **No human has checked the transcriptions.** They are by AI (first: Claude Fable 5.2; second: OpenAI Codex gpt-6-astra, reasoning effort high; prior-work check: Claude Sonnet). Agreement among AIs is no substitute for human checking.

## Addition: the 1901 table (2026-11-10)
- **Status: reconstruction of a table.** In seven telegrams of February-April 1901 (from officers in China and one from Hiroshima), the parts where only the sensitive words are put into two digits per kana can be read with the reconstructed table. All seven have their contemporary translations in the same files: **the telegrams were read at the time.** What is new here is the reconstruction of the table; in the range searched on 2026-11-10 (the added section of [docs/PRIOR_CHECK.en.md](docs/PRIOR_CHECK.en.md)) no publication of this table was found. No claim of priority is made.
- **The table**: the syllabary by vowel rows, each voiced and half-voiced kana right after its plain kana, numbered from 00 (ア00 カ01 ガ02 … ワ14, イ15 … リ26, ウ27 … ル39, エ40 … レ52, オ53 … ン67). In full: [docs/READING1901.en.md](docs/READING1901.en.md). It is a different table from the 1902-04 one below.
- **Numbers**: in the two telegrams the table was applied to after it was fixed (C09122796200 from Chungking, and the two runs of C09122806100 from Hiroshima made only of values inside the table), agreement with the words of the translation is 16/16. Control: none of 1,000 random permutations of the 68 kana did as well (best: 4). Digit agreement with an independent second transcription (Codex): 123/135 (91.1%) over six telegrams; lowest single telegram C09122801000 at 75.0% (the lower of two runs; [docs/METHOD.en.md](docs/METHOD.en.md) §9.3).
- **C09122806100 (1901-02-18)**: given as unread in the October 2026 version. With the same table it reads ンチワ (任地ハ), フクム (服務) and テンシヨク. 69 and 91 are outside the table ([docs/OPEN.en.md](docs/OPEN.en.md)).
- The five drafts from the General Staff to Maj.-Gen. Fukushima have the same layout but are not readable with this table. They are read with a different table (see "Addition: the 1901 table of the outgoing drafts" above).
- **No human has checked the transcriptions.** They are by AI (first: Claude Fable 5.2; second: OpenAI Codex gpt-6-astra, reasoning effort high; prior-work check: Claude Sonnet). Agreement among AIs is no substitute for human checking.

## Summary (2026-10-20, partly updated 2026-10-25)
- **Status: the table and two telegrams are full readings; two telegrams are partial readings; one telegram is unread.**
  - Full readings: C09122911500 (1902-03-27, whole text in 36 digit pairs) and C09123116600 (1904-01-25, 13 pairs, no contemporary translation).
  - Partial readings: C09122909900 (1902-03-28) and C03020059400 (1904-01). The readings are given, but the reliability figures fall short of the thresholds used here (see [docs/OPEN.en.md](docs/OPEN.en.md)).
  - C09122806100 (1901-02-18) is not readable with this 1902 table. On 2026-11-10 part of it was read with a different table (see "Addition: the 1901 table" below).
- **Figures**
  - C09122911500: 35/35 pairs agree with the contemporary translation. With tables whose row and column digits were randomly permuted, 0 of 1,000 reached the real score (max 16). Independent second transcriptions (Codex): 97.2% and 100%. Proportion of pairs with a value: 35/36 (the final "80" is taken as an end mark, not counted).
  - C09123116600: no translation. The reading "ヨヨウノカンコクチズダイヨ" (要用ノ韓国地図貸与, "please lend the required maps of Korea") matches the reply draft in the same file (sending maps of Korea). Using a kana-bigram model built from plaintext telegrams in the JACAR catalogue (18,810 kana), 0 of 1,000 permuted tables scored at or above the real reading. Second transcriptions (Codex ×2): 26/26 and 26/26.
  - C09122909900: 11/12 against the furigana of the outgoing draft (イ is written 17, the table gives 19; Tomokiyo reads 14 = ヒ, see [docs/OPEN.en.md](docs/OPEN.en.md)). Lowest second-transcription agreement 84.6% (one Claude Sonnet run).
  - C03020059400: 12/12 against the translation, taking the 5th pair as 04 following Tomokiyo Satoshi's reading of the image and the spelling ゼウ for 場 as correct (11/12 with the first transcription 09). Lowest second-transcription agreement 87.5%, below the 90% required for a full reading.
- **Whether this table is the "Yakugō" (鑰号) cipher is not settled.** It was used in domestic Army telegrams during the Yakugō period (printed June 1900, abolished June 1904), but the instructions for Yakugō have not been found. It may instead be the numeric part of the Tokugō (特号) cipher, successor of Kongō (坤号) (conjecture; [docs/METHOD.en.md](docs/METHOD.en.md)).
- **Prior work:** Cryptiana (Tomokiyo Satoshi) describes Army coordinate-type numeric ciphers of 1874 and 1894. Both use iroha order, unlike this table (gojūon row × column). A search on 2026-10-20 by a checker who did not take part in the decipherment, intended to find prior solutions ([docs/PRIOR_CHECK.en.md](docs/PRIOR_CHECK.en.md)), found no prior reading of this table or these telegrams. We do not claim "first".
- **Human checking is partial.** Transcriptions were made by AI. Tomokiyo Satoshi checked the images of the four telegrams by eye and published his readings on Cryptiana ([meijiarmy2.htm](https://cryptiana.web.fc2.com/code/meijiarmy2.htm), 2026-10-24); one character of C03020059400 was corrected accordingly (2026-10-25). Other characters cannot be called human-checked. Agreement between AI models is not a substitute for human checking.
- **Use of AI:** most of the work was done by Claude Opus 5.5. Independent second transcriptions and character judgements were done by OpenAI Codex (codex-cli 0.163.0-alpha.10.2, default model) and Claude Sonnet; the prior-work search by Claude Sonnet in a separate context. The publisher gave directions.

## The table
| Row (first digit) | Clean columns (second digit) | Voiced |
|---|---|---|
| a 0, i 1, u 2, e 3, o 4 | a9 ka8 sa7 ta6 na5 ha4 ma3 ya2 ra1 wa0 | row digit +5; columns ga9 za8 da7 ba6 |

- ン = 10. The final 80 is taken as an end mark (conjecture).
- Examples: カ=08, シ=17, ガ=59, ブ=76, ン=10.
- The table was inferred from the 12 pairs of C09122909900 and then applied to the three telegrams found later. Only the ba column (6) was fixed from ブ=76 in C09122911500.

## Readings (details: [docs/READING.en.md](docs/READING.en.md))
| Reference, frame | Date, sender | Digits | Reading |
|---|---|---|---|
| C09122911500 fr. 0110 | 1902-03-27 Osaka, Chief of Staff Ōyama → Lt.-Gen. Terauchi | 36 pairs | ホンシヨクキキヨウマデホンブノジムハキクワンヨロシクトリハカラハレタシ ("Until I return to Tokyo, please take care of the General Staff's affairs") |
| C09123116600 fr. 0026 | 1904-01-25 Kokura → Maj.-Gen. Iguchi, General Staff | 13 pairs | ヨヨウノカンコクチズダイヨ + plaintext サレタシ ヲハラ |
| C09122909900 fr. 0079 | 1902-03-28 Osaka, Ōyama → Maj.-Gen. Fukushima | 12 pairs | カイグンエンシウケンガク ("naval exercise observation") + plaintext ノケン キヨカス (partial reading) |
| C03020059400 fr. 0119 | 1904-01, Div. commander Inoue → War Minister | 12 pairs | シンテイハクゼウシレイブ (= 辛碇泊場司令部; 5th pair 04 following Tomokiyo's reading of the image; partial reading) |

## Contents
| Path | Contents |
|---|---|
| `docs/READING.md` | per-telegram transcription, alignment and reading |
| `docs/METHOD.md` | search, inference of the table, controls, second transcriptions, AI use, limits |
| `docs/READING1901.md` | the 1901 table and its telegrams |
| `docs/OPEN.md` | open questions |
| `docs/PRIOR_CHECK.md` | prior-work check by a separate checker |
| `data/telegrams.tsv` | list of telegrams |
| `docs/READING1901B.md` | the 1901 table of the outgoing drafts and the reading of the five drafts |
| `data/telegrams1901.tsv`, `data/outgoing1901.txt`, `data/outgoing1901.tsv` | list of the 1901 telegrams; first transcription of the five drafts; reading run by run |
| `src/table1901b.py` | the 1901 outgoing table, readings and control |
| `src/table1901.py` | the 1901 table, readings and control |
| `data/transcription.txt` | digit transcriptions (first reader) |
| `second/` | second transcriptions (Codex replies, Sonnet digit columns) and prompts |
| `src/table1902.py` | table, decoding, permutation control |
| `src/score.py` | agreement of second transcriptions (per-column edit distance) |
| `src/control_lm.py` | bigram control for C09123116600 (corpus not included) |
| `tests/` | `python3 -m unittest discover -s tests` |

No images are included. Sources are cited by JACAR (Japan Center for Asian Historical Records) reference code and frame number; see [SOURCES.en.md](SOURCES.en.md).

## Update history
- 2026-11-11: added three drafts of the same binder (C09122813500, C09122814000, C09122815900; [docs/READING1901C.en.md](docs/READING1901C.en.md), [src/table1901c.py](src/table1901c.py)): 68 = 一 in the incoming table, and a third table in June. The earlier tables and readings are unchanged. The open points (docs/OPEN.en.md §1, §1b) were updated.
- 2026-11-10 (third update): in the five outgoing drafts the five values outside the table are now read as word codes (99 = Russia, 60 = China, 80 = minister agree with a Foreign Ministry record; 89 = Germany and 59 = government are conjecture). Pairs counted as read changed from 130 to 137 (of 148). The first group of C09122809400 changed from "digits not settled" to "99506". The reading 決マラザレバ in C09122812300 was withdrawn because the readers disagree on the romaji.
- 2026-11-10 (second update): the five drafts sent out by the General Staff changed from "unread" to "two full readings, three partial readings" (outgoing table added; before, no pair had a value, now 138 of 148 pairs).
- 2026-11-10: the 1901 table added. C09122806100 changed from "unread" to "partly readable with the 1901 table" (ンチワ, フクム, テンシヨク; before, no pair had a value). The pairing of its first run moved by one digit (04 56 71 … → 45 67 18 …).
- 2026-10-25: the digit list of C09122911500 corrected; one character of C03020059400 changed following Satoshi Tomokiyo's reading of the image.

## License
Code (src/, tests/): MIT. Original documents and data: CC BY 4.0 ([LICENSE](LICENSE)).
