日本語: [METHOD.md](METHOD.md)

# Method, figures, use of AI, limits

## 1. How the telegrams were found
- The starting points were C09122806100 (1901-02), a partially enciphered telegram with a decoded text, and C09122909900 (1902-03), found by searching the catalogue.
- JACAR's full-text search draws only on the beginning of the catalogue content field. Moreover, in the General Staff Office Miscellaneous (Confidential) files, the content field itself is cut off at about 320 characters. The following ranges were therefore viewed frame by frame in the images (retrieval at intervals of 3 seconds or more).
  - General Staff Office, Miscellaneous (Confidential), 『明治３４年・３５年 電報綴 北清事件』 and the dispatch file (通報綴) of the same years: all items whose images could be obtained (about 420 items, 1,088 frames; 404 errors for 5).
  - Of the incoming telegrams of 1904 in the Army Ministry Daijiki, the 235 items that matched 「訳文」 or 「電報訳」 in a JACAR search (1,749 frames; 404 errors for 3).
  - In the catalogue content field, about 2,200 items were searched for runs of digits and for transcriptions in which 2-digit kanji numerals are listed separated by 読点. C09123116600 was found this way.
- Five numeric kana-cipher telegrams were found (four with a decoded text, one without). In addition there were telegrams in 5-digit numbers and roman letters (four, such as General Staff Office → Major General Fukushima; a different method). Groups of 2 kana in parentheses belong to the 『陸軍電信符号』 (Army telegraph code), which is for saving charges and is not a cipher (confirmed from Cryptiana's description and the decoded texts).

## 2. Inference of the table
- From the 12 pairs of C09122909900 and the furigana of the outgoing telegram (カイグンエンシウケンガク), the following was found: ン is 10 all three times. The remainder of the first digit divided by 5 matches the vowel (a0, i1, u2, e3). A first digit of 5 or more occurs only for voiced consonants. After the カ row, the digit is 8 for unvoiced and 9 for voiced.
- Since the row digits run ア9 カ8 サ7, the table was built taking the rows to be in reverse gojūon order. With C09122911500, found afterwards, the table agreed on all 35 pairs (the column 6 of the バ row was determined from the ブ in this telegram).
- Neither this table nor a method of adding a periodic digit (period 1–7) to the table fits C09122806100 (1901-02).

## 3. Control tests
- Permutation control (`src/table1902.py`): tables in which the 5 vowel-row digits, the 10 row digits and the 4 row digits of the voiced consonants were randomly permuted were used, and the number of times (out of 1000) that the agreement with the decoded text equals or exceeds that of the real table was counted. C09122911500: 0 times (maximum 16, real 35). C09122909900: 0 times (maximum 7, real 11; but the table was built from this telegram, so this is only a guide). C03020059400: 0 times (maximum 5, real 12; real 10 before the correction of 2026-10-25).
- C09123116600, which has no decoded text: plain-text kana (18,810 characters) were collected from the telegrams in the JACAR catalogue content field, and a likelihood for sequences of 2 kana was built. The number of permuted tables that reached the reading from the real table (−42.8) or better was 0 out of 1000; the best was −46.0. The kana used for training are sentences from the JACAR catalogue and are not included in this repository.
  - In the first version, ン and ヰ were both 10 in the table, ヰ appeared in the reading, and 12 permuted tables were at or above the real one. The 0 times above is the value from a run after correcting this by giving priority to ン and penalizing values not in the table.

## 4. Independent second transcription
- The first transcription was made by Claude Opus 5.5 reading the enlarged images. For the second, a different model was given only the image and the instructions (`second/PROMPT*.md`), without the values, the first reading or the decoded text.
  - OpenAI Codex (codex-cli 0.163.0-alpha.10.2; the model does not appear in the run record, so the default model): `codex exec --ephemeral -s read-only -i <image>`, with the prompt on standard input. The run record shows no command execution or file reading.
  - Claude Sonnet: an Agent of Claude Code (model=sonnet). Given only the image path and the same instructions.
- Only the digits are compared. Counted by edit distance per column, agreement rate = (number of reference characters − number of edits) / number of reference characters (`src/score.py`). In a bracketed alternative [a/b] the first candidate is used; ? is an error. A marking not in the text that was entered as a character is also counted as an error (this way of counting was decided and recorded before the second re-take for C09122909900).
- All values are given, and the lowest is used for the judgment.

| Telegram | Runs and values | Lowest |
|---|---|---|
| C09122911500 (72 characters) | Codex 100%, 97.2% | 97.2% |
| C09123116600 (26 characters) | Codex 100%, 100% | 100% |
| C09122909900 (26 characters) | Before enlargement: Codex 92.3%, 92.3%; Sonnet 84.6%. After enlargement: Codex 96.2%, 100%, 100%, 100%; Sonnet 88.5%, 84.6%, 92.3%, 92.3% | 84.6% |
| C03020059400 (24 characters) | Before enlargement: Sonnet 87.5%. After enlargement: Codex 95.8%, 95.8%, 91.7%; Sonnet 91.7%, 87.5% | 87.5% |

- For characters on which the transcriptions differed, each character was cut out with its value hidden and judged by Codex and Sonnet (twice, in separate contexts). There was no place where the two judgments agreed on a character different from the first transcription, and the first transcription was not corrected (number corrected: 0).

## 5. Calibration
- The contemporary decoded texts (three telegrams) and the furigana of the outgoing telegram (C09122909900) were used for calibration. Character agreement: C09122911500 35/35, C09122909900 11/12, C03020059400 12/12 (after one character was corrected following Tomokiyo Satoshi's reading of the image and ゼウ was accepted as a spelling, 2026-10-25; earlier 10/12). C09123116600 has no decoded text, so there is no calibration.

## 6. Relation to Yakugō (鑰号) (conjecture)
- The Yakugō (鑰号) cipher was printed in June 1900 as a revision of Butsugō (物号), and was used from January 1901 to June 1904 (JACAR C09122592800, C10061983200, C06040646600). In September 1900, while in use, it was described as 「秘密ヲ守ルノ点ニ於テハ頗ル確実ナルモ使用上甚タ不便」 (very reliable as regards keeping secrecy, but very inconvenient in use). The attached 「乙号」 had the 「鑰語標点」, which staff officers memorized (C02030445900, 1901-03).
- This table is simple and did not change from March 1902 to January 1904. It cannot be decided whether it is a use, without the key, of a method in which the key (鑰語) changes the values, or a different cipher (the 「数字ノ分」 of Tokugō (特号), thought to be the successor of Kongō (坤号), C03025477100).

## 7. Limits
- Human checking is partial: Tomokiyo Satoshi published readings made by eye from the images on Cryptiana (2026-10-24), and one character was corrected accordingly. Agreement among AIs is no substitute for human checking.
- The sample is four telegrams (66 pairs). Of the values in the table, only some actually appeared (parts of the ア, カ, サ, タ, ナ, ハ, マ, ヤ, ラ and ワ rows, and parts of the voiced ガ, ザ, ダ and バ rows). The values that did not appear are inferences from the rules.
- The JACAR images are binarized (JBIG2), so thin marks and the presence of dakuten are hard to tell.
- The survey is limited to the ranges above. Items in the 1904 files of the Army Ministry Daijiki that did not match the search have not been viewed.

## 8. Use of AI
- Claude Opus 5.5 (Anthropic): searching for and retrieving sources, transcription of images (first), inference of the table, control tests, writing of the documents.
- OpenAI Codex: independent second transcription, judgment of characters.
- Claude Sonnet: independent second transcription, judgment of characters, prior-work check (a separate context that did not take part in the decipherment).
- Publisher: gave instructions on the direction of the work. Did not check the transcriptions or the readings.

## 9. The 1901 table (added 2026-11-10)
Correspondence and readings: [READING1901.en.md](READING1901.en.md); script: `src/table1901.py`.

### 9.1 How it was found
- Telegrams in romanised Japanese exchanged with officers stationed in China contain groups of five digits. In the survey of October 2026 these were taken for plain romaji telegrams and the digits were overlooked.
- In C09122724200, which has a translation, both digit runs have 14 digits (5 + 5 + 4), matching the seven kana of each of the two words in the translation (独逸皇帝, 天皇陛下). The five-digit grouping is a transmission format; the unit is two digits. In the five outgoing drafts, too, all 23 digit runs are of even length.
- Four telegrams from Maj.-Gen. Fukushima (C09122805800, 805900, 806000, 801000) have translations in the same file, and the recipient wrote kana beside the digits. Collecting the values from the translated words and these annotations gives ア00 カ01 ガ02 サ03 …: a running number through the syllabary by vowel rows, with each voiced kana right after its plain one (タ05 ダ06, ゲ42, ゼ44, ド59). The numbers 00-67 were filled in by this rule.

### 9.2 Control
- **Two telegrams the table was applied to after it was fixed** (not used to infer it): the ten pairs of C09122796200 and, from C09122806100, the two runs made only of values inside the table (ンチワ, フクム; six pairs). Agreement with the expected kana (the words of the translation in the spelling of the telegrams): 16/16. With the 68 kana of the table randomly permuted, none of 1,000 tables did as well (best: 4).
- モ, ト and グ in C09122796200 occur in no other telegram; they were fixed beforehand by the rule of the arrangement alone.
- The four telegrams used to infer the table give 42/42 (not a test, since they built the table). The 14 pairs of C09122724200 include digits re-read with the table in hand and are not counted.
- The spelling of the expected kana (を as オ, the particle は as ハ or ワ) was settled after reading; in that respect it was not fixed blind.

### 9.3 Independent second transcription
- OpenAI Codex (codex-cli 0.163.0-alpha.10.2, model gpt-6-astra, reasoning effort high) was given the image of the message field of each of the six telegrams received from China, one at a time, from an empty directory. It was not given the table, the first transcription or the translations. The run logs show no command execution and no file reads. Prompt: `second/PROMPT1901.md`; answers: `second/codex1901/` (run1_ = the six images of the first run, run2_ = the four enlarged images). The images show the recipient's kana annotations (the prompt says to ignore them).
- Agreement of digits (first transcription as reference, edit distance): six telegrams together 123/135 (91.1%); by telegram C09122805800 48/49, C09122805900 7/8, C09122806000 8/8, C09122796200 19/20, C09122801000 17/22 (77.3%), C09122724200 24/28 (85.7%).
- The digits that differed were looked at again on enlarged images by the first reader (Claude) and left as first read (no digit changed). No judgement by another model was made.
- The two telegrams with the lowest agreement (C09122801000, C09122724200) were read once more, with the same prompt, from four enlarged images (the top two lines cut into a left and a right half). The cut split the groups and the answers were fragments: C09122801000 15/20 of the digits inside the crops (75.0%), C09122724200 25/28 (89.3%). Both runs are given; the better one is not selected.
- So for C09122801000 (ゲンスイガ, コウテイヨリ) the agreement with the second reader is 75.0-77.3%, below 90%. In C09122724200 Codex both times read a "7" before the second group of the first run (59153 7 25427 4515) and read the first group of the second run as 4507x. The reading given here (59153 25427 4515, 45676) was made with the table in hand; these two points are not settled. The table values that occur only in these two telegrams (カ ガ リ ス ツ ゲ ヘ コ ド ヨ, ten values) are weaker to that extent.
- The contemporary translations and the recipient's annotations are what the readings rest on. Agreement among AIs is no substitute for human checking.

### 9.4 Limits
- No human has checked the transcriptions.
- The sample is seven telegrams, 72 pairs (leaving out the values outside the table in C09122806100). 38 of the 68 values are attested.
- These telegrams were read at the time; what is new here is only the reconstruction of the table. The name of the table (whether it is the numeric part of the Tokugō cipher) is not confirmed.
- The five outgoing drafts are not read by this table. They are read by a different table (§10).

### 9.5 Use of AI (1901 table)
- Claude Fable 5.2 (Anthropic): transcription of the images (first), inference of the table, control, writing of the documents.
- OpenAI Codex (gpt-6-astra, reasoning effort high): independent second transcription.
- Claude Sonnet: prior-work check (a separate reader that took no part in rebuilding the table).
- Publisher: gave instructions on the direction of the work. Did not check the transcriptions or the readings.

## 10. The 1901 table of the outgoing drafts (added 2026-11-10)
Alignment and reading: [READING1901B.en.md](READING1901B.en.md); script: `src/table1901b.py`.

### 10.1 How it was found
- The table of the incoming telegrams (§9) does not read these drafts, and exhaustive additions, reversals and reorderings gave no text. There is no contemporary translation.
- The lead was the romaji right after the digits. At the end of C09122812300, `48456 241 mitasigatasi` ("… is hard to meet"): taking the four pairs as ノゾミヲ ("the wish", object), the differences ノ−ゾ = 3 and ゾ−オ = 4 are the same as in the o-row of the incoming table (オ コ ゴ ソ ゾ ト ド ノ). Hence オ41 コ42 ゴ43 ソ44 ゾ45 ト46 ド47 ノ48.
- In C09122808400, `41411 45248 kotowa…` is then オオ・・ノ ("the matter of …"), i.e. オオシマノ; in C09122809400, `64422 11493` is ・コ・・・・ with the third and sixth pair equal, i.e. リコウシヨウ (Li Hongzhang). This fixes シ14, ウ21, マ52, ミ62, リ64, ヨ93 and shows a grid with tens digit = vowel row and units digit = consonant column (lower half ア k g s z t d n h b, upper half p m y r w).
- Only these three words (13 different values) and the grid rule were used to fix the table. The other readings (ヒメジニ, クスノセハ, シバハトニ, ワガ, テウシドウ, ゼウヤクノ, デンポウキ, ゲンスイハコウシウワンヨリニホンニ, カレオヒキ, ワレハソウ, ヨウスナレハ, キテウスル, コウタイヘイノスウハ and so on) came out of the table.

### 10.2 Control
- There is no translation, so a public dictionary is used for scoring: the readings of JMdict (English edition, fetched 2026-11-10), normalised to full-size katakana, 175,531 words of three kana or more; the score is the number of kana in each digit run that can be covered by non-overlapping dictionary words (`cover` in `src/table1901b.py`). The dictionary is not included here.
- With the first transcription as it stands (digits read before the table was known): 58 for the real table. Of 1,000 grids with the row and column digits randomly permuted, none reached that (max 37); of 1,000 tables with the 70 kana randomly reassigned, none (max 36).
- With the four re-read places: 67 for the real table, again none of 1,000 (max 38 and 42).
- The dictionary has modern spellings, so the historical spellings (ゼウヤク, テウ, キテウ, チウコク) and personal names score nothing; the scoring is to that extent unfavourable to the real table.

### 10.3 Independent second transcription
- OpenAI Codex (codex-cli 0.163.0-alpha.10.2, model gpt-6-astra, reasoning effort high) was given the image of the message field of each of the five drafts, one at a time, from an empty folder. The table and the first transcription were not given. The run logs show no command execution or file reading. Prompt: `second/PROMPT1901B.md`; replies: `second/codex1901b/`.
- Digit agreement (first transcription as reference; digits only, aligned, counting matching digits): C09122808300 22/22, C09122808400 30/30, C09122809400 109/118 (92.4%), C09122810100 82/84 (97.6%), C09122812300 42/42, total 285/296 (96.3%).
- Differences in C09122809400: the first group (first 99506, Codex 77306), the head of 64422 (Codex took it as struck out: 422), 14222 (Codex 14223), 35215 (Codex took the fourth digit as struck out), the final 12112 (Codex 121 and a blot). Counted by two-digit pairs: 53/59 (89.8%).
- Differences in C09122810100: 42291 (Codex 42211), 94427 (Codex 94421), and the leading 4 of a struck-out group (kept by Codex). The first two are the digits we re-read after the table was known; a reader who did not know the table read the same.
- Of the four places re-read after the table was known, the two in C09122809400 (43962→43162, 16598→16593) were read by Codex as in the first transcription. These two are treated as conjecture and are not counted as read.
- The differences were not put to a further model. Only the four places above were changed; data/outgoing1901.txt (the first transcription) is left as it was, and the re-readings are kept apart in `src/table1901b.py`.

### 10.4 Checks against content
- C09122810100 (8 March), "the Field Marshal wishes to come to Japan from Kiaochow Bay": Fukushima's telegram of 22 April (C09122801000) has "the Field Marshal has received the Emperor's permission to go to Japan". The Spectator of 8 June 1901 reports that Count Waldersee had left China for Japan.
- A draft in Japanese in the same file, C09122808100 (to Maj.-Gen. Fukushima, from Tamura), asks him to convey to the Field Marshal an invitation to visit Japan on the way home (seen in a reduced image and in the JACAR catalogue text; it is not the plaintext of any of the five).
- C09122808400 (14 February), "Shiba will be sent back in any case": Fukushima's telegram of 25 February (C09122805900) has "Shiba is to leave at the beginning of next month".
- C09122809400 (2 March) falls in the period of Japan's advice to China on the Russo-Chinese agreement about Manchuria. The details have not been compared with the sources.

### 10.5 Limits
- No human has checked the transcriptions.
- There is no contemporary plaintext, so no calibration. The reading rests on the control and on the fact that the words that came out of the table fit the context.
- Two drafts are full readings (C09122808400, C09122812300). Three are partial ([OPEN.en.md](OPEN.en.md) §1b).

### 10.5b Word codes and a check of the re-readings (added 2026-11-10)
- For the five values outside the table, words were proposed from the context and then compared with records. The passage "Li Hongzhang had [60][80] tell …" in the telegram of 2 March was compared with the Foreign Ministry minutes of the Chinese Minister's call of 1 March (JACAR B03030000800), giving 60 = China and 80 = minister. 99 = Russia comes from the contexts "[99][60] articles" and "… secret agreement". 89 = Germany and 59 = government are conjecture and are not counted as read.
- To look for more telegrams in the same table, 84 catalogue entries of the same binder (C09122807700–C09122816000) were fetched. The only cipher telegrams to Fukushima are the five.
- Seven re-read places (the first group and two digits in C09122809400; romaji in C09122810100 and C09122812300) were cut out as strips and given, without the table and without our readings, to Codex ([second/PROMPT1901B2.md](../second/PROMPT1901B2.md); output in second/codex1901b/strip_*.txt) and to Claude Sonnet. The rule fixed beforehand: a re-reading is supported if both agree with it, and stays open if they split. Result: in no place did both agree with the re-reading. Both read the first group as 99506, and our re-reading (99606) was withdrawn. The other places split or were not supported (see the notes under each telegram in [READING1901B.en.md](READING1901B.en.md)).

### 10.6 Use of AI (outgoing table)
- Claude Fable 5.2 (Anthropic): first transcription from the images, finding the table, controls, writing the documents.
- OpenAI Codex (gpt-6-astra, reasoning effort high): independent second transcription.
- Claude Sonnet: prior-work check (a separate reader who took no part in finding the table).
- The publisher: direction of the work. The publisher has not checked the transcriptions or the readings.
