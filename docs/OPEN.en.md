日本語: [OPEN.md](OPEN.md)

# Open points

## 1. What remains open for the 1901 table ([READING1901.en.md](READING1901.en.md))
- **Use of 68-99.** In C09122806100, 91 stands twice where the translation has ニ就キ / ニ就テ ("concerning"), and 69 once where 任地 has ニ. The table's ニ is 21. 91 looks like a code for a word and 69 like a spare value for a kana (conjecture), but these three places are the whole sample.
- **First run of C09122806100.** The form has the 14 digits 〇四五六七一八六五二八九一一. Dropping the leading 〇 and cutting into pairs gives テンシヨク[91], but the leading 〇 and the final 一 are left over. The October 2026 version cut the run into pairs from its first digit (04 56 71 …). The translation says 石橋転任ノ事ニ就キ ("on Ishibashi's transfer"), which is not the same word as テンシヨク (転職).
- **Thirty table values not attested in any telegram.** ザ ナ バ パ ギ ジ ヒ ビ ピ ミ ズ ヌ ブ プ ユ ル エ ケ セ デ ネ ベ ペ ゴ ソ ゾ ホ ボ ポ ロ are placed by the rule of the arrangement. Whether ヰ ヱ ヲ ヂ ヅ exist in the table is unknown (the rule leaves no room for them).
- **Five drafts sent out by the General Staff are unread** ([data/outgoing1901.txt](../data/outgoing1901.txt), 148 pairs). Same layout, and all 23 digit runs are of even length, but:
  - with this table they give no text (21 of the 148 pairs are 68 or more);
  - tried without result: one number added to everything (mod 68, mod 100), a different number for each telegram, different numbers for the two digits, runs or groups reversed, complements to 9 and 10, ten orderings of the syllabary (gojūon and iroha variants) with reversal, digit swap and 100 shifts;
  - the same 59 18 occurs twice in one telegram, so the key does not change with position. It looks like another table using the whole range 00-99;
  - no translation of these five, and no plaintext pair for their table, has been found.
- **Three digits of C09122724200.** The image is poor and some digits were re-read with the table in hand ([READING1901.en.md](READING1901.en.md)).
- **Name.** Whether this table is the "Tokugō cipher (numeric part)" (特号暗号 数字ノ分) is not settled. The use (telegrams with officers in China, 1901) fits, but no instruction text has been found.

## 2. C09122909900 does not reach a full reading
- The lowest value in the independent second transcription is 84.6% (Claude Sonnet, one run on the enlarged image). In that run, a small エ-shaped marking at the lower right of 「三」 in column 1 was entered as one character of the text, and the head of column 2 and the 八 in column 4 were also read as different characters. The other runs are 88.5–100%.
- The horizontal stroke at the head of column 2 is hidden where its right end enters a thick vertical band of ink. Whether it is 一 (the head of ン = 10), or フ or 七, cannot be decided from the image.
- イ is written as 17 (19 in the table). The image also shows 七. Taken to be an error by the writer or in transmission (conjecture).
- Tomokiyo Satoshi reads this 七 as 四 (14 = ヒ, カヒグン) ([meijiarmy2.htm](https://cryptiana.web.fc2.com/code/meijiarmy2.htm), 2026-10-24: "looks like 7 but is clearly different from 7 in other places"). All our independent second transcriptions (Codex ×6, Sonnet ×5) and the three character judgements read 七, so the transcription is not changed. Neither 17 nor 14 gives イ (19), so the agreement with the furigana stays 11/12.

## 3. C03020059400 does not reach a full reading
- The last character of column 1 (second digit of the 5th pair) was changed from 九 to 四 on 2026-10-25. Tomokiyo Satoshi, looking at the image, found it "clearly different from 9 in other places" and like a cursive 四 ([meijiarmy2.htm](https://cryptiana.web.fc2.com/code/meijiarmy2.htm), 2026-10-24; he notes he may be biased by the expected reading). A human reading is given precedence over judgements by AI models.
  - The AI judgements were split: compared with ten digits of the same writer (Codex ×2, Sonnet ×2), the first candidate was 九 in all four runs, but the samples contained no 四 (there is no other 四 in this telegram). In the full transcriptions, Codex read ル (second candidate 四) three times and Sonnet "?" three times; no run read 九.
  - Second-transcription agreement does not change with 四 as the reference, since no run read 九 there.
- 88 (ゼウ) is taken, following Tomokiyo, as the spelling ゼウ for 場 (ぢやう), as in どぜう; earlier it was treated as a slip for ジウ.
- The agreement with the decoded text is now 12/12 (11/12 with the first transcription 09, or if ゼウ is counted as an error). The permutation control stays 0/1000 (max 5).
- It is still not a full reading, because the lowest second-transcription agreement is 87.5% (Sonnet, one run on the enlarged image), below the 90% threshold.

## 4. The name
- It has not been decided which of Yakugō (鑰号), Kongō (坤号) and the 「数字ノ分」 (numeral part) of Tokugō (特号) this table is. No text on their use was found in JACAR; the physical items held by the National Institute for Defense Studies would have to be seen.

## 5. Scope
- Items in the 1904 files of the Army Ministry Daijiki that did not match the JACAR search for 「訳文」 or 「電報訳」 have not been viewed. No numeric telegram of 1903 was found in the Meiji 36 telegram file (catalogue).
