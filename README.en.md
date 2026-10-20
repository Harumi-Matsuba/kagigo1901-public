# A Japanese Army numeric kana cipher of 1902–04 (telegrams in JACAR): table and readings

This repository records the reconstruction of a cipher used by the Imperial Japanese Army in domestic telegrams in 1902–04, in which **two digits stand for one kana**, and the reading of four telegrams. The table is a coordinate system: the first digit gives the vowel row of the Japanese syllabary (gojūon dan) and the second digit the consonant column (gyō). The same table was used unchanged from March 1902 (Osaka) to January 1904 (Kokura, Moji).

日本語: [README.md](README.md).

## Summary (2026-10-20)
- **Status: the table and two telegrams are full readings; two telegrams are partial readings; one telegram is unread.**
  - Full readings: C09122911500 (1902-03-27, whole text in 36 digit pairs) and C09123116600 (1904-01-25, 13 pairs, no contemporary translation).
  - Partial readings: C09122909900 (1902-03-28) and C03020059400 (1904-01). The readings are given, but the reliability figures fall short of the thresholds used here (see [docs/OPEN.en.md](docs/OPEN.en.md)).
  - Unread: C09122806100 (1901-02-18), a different method not readable with this table.
- **Figures**
  - C09122911500: 35/35 pairs agree with the contemporary translation. With tables whose row and column digits were randomly permuted, 0 of 1,000 reached the real score (max 16). Independent second transcriptions (Codex): 97.2% and 100%. Proportion of pairs with a value: 35/36 (the final "80" is taken as an end mark, not counted).
  - C09123116600: no translation. The reading "ヨヨウノカンコクチズダイヨ" (要用ノ韓国地図貸与, "please lend the required maps of Korea") matches the reply draft in the same file (sending maps of Korea). Using a kana-bigram model built from plaintext telegrams in the JACAR catalogue (18,810 kana), 0 of 1,000 permuted tables scored at or above the real reading. Second transcriptions (Codex ×2): 26/26 and 26/26.
  - C09122909900: 11/12 against the furigana of the outgoing draft (イ is written 17, the table gives 19). Lowest second-transcription agreement 84.6% (one Claude Sonnet run).
  - C03020059400: 10/12 against the translation. Lowest second-transcription agreement 87.5%.
- **Whether this table is the "Yakugō" (鑰号) cipher is not settled.** It was used in domestic Army telegrams during the Yakugō period (printed June 1900, abolished June 1904), but the instructions for Yakugō have not been found. It may instead be the numeric part of the Tokugō (特号) cipher, successor of Kongō (坤号) (conjecture; [docs/METHOD.en.md](docs/METHOD.en.md)).
- **Prior work:** Cryptiana (Tomokiyo Satoshi) describes Army coordinate-type numeric ciphers of 1874 and 1894. Both use iroha order, unlike this table (gojūon row × column). A search on 2026-10-20 by a checker who did not take part in the decipherment, intended to find prior solutions ([docs/PRIOR_CHECK.en.md](docs/PRIOR_CHECK.en.md)), found no prior reading of this table or these telegrams. We do not claim "first".
- **No human has checked the transcriptions.** Transcriptions were made by AI only. Agreement between AI models is not a substitute for human checking.
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
| C03020059400 fr. 0119 | 1904-01, Div. commander Inoue → War Minister | 12 pairs | シンテイアクゼウシレイブ (= 辛碇泊場司令部; two pairs disagree with the translation; partial reading) |

## Contents
| Path | Contents |
|---|---|
| `docs/READING.md` | per-telegram transcription, alignment and reading |
| `docs/METHOD.md` | search, inference of the table, controls, second transcriptions, AI use, limits |
| `docs/OPEN.md` | open questions |
| `docs/PRIOR_CHECK.md` | prior-work check by a separate checker |
| `data/telegrams.tsv` | list of telegrams |
| `data/transcription.txt` | digit transcriptions (first reader) |
| `second/` | second transcriptions (Codex replies, Sonnet digit columns) and prompts |
| `src/table1902.py` | table, decoding, permutation control |
| `src/score.py` | agreement of second transcriptions (per-column edit distance) |
| `src/control_lm.py` | bigram control for C09123116600 (corpus not included) |
| `tests/` | `python3 -m unittest discover -s tests` |

No images are included. Sources are cited by JACAR (Japan Center for Asian Historical Records) reference code and frame number; see [SOURCES.en.md](SOURCES.en.md).

## License
Code (src/, tests/): MIT. Original documents and data: CC BY 4.0 ([LICENSE](LICENSE)).
