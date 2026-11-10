日本語: [PRIOR_CHECK.md](PRIOR_CHECK.md)

# Prior-work check — Army numeric kana cipher (1902–04)

Date of check: 2026-10-20. Checker: a separate session that did not take part in the work of solving this table. The search was made with the intention of showing that it "has already been read."
What was received: the table in the "conclusion" of the work record (first digit = row (dan), following digit = column (gyō), ン = 10), the reference codes of the telegrams said to have been read (C09122909900, C09122911500, C09123116600, C03020059400), and the unread C09122806100. The process of decipherment (the working files) was not seen. The correctness of the table itself was not checked (this judgment concerns only whether there is prior work).

## Category: not found
(In the sources searched below, no document that describes this table or this method, and no record of these telegrams having been read, was found. No claim of priority can be made.)

Main grounds:
1. **No description of a table of the same construction.** The Army page of Cryptiana (meijiarmy.htm, the version re-fetched on 2026-10-20; its size, 45,346 bytes, is the same as the saved version in prior/) contains two coordinate-type numeric ciphers of the Army. In both, the arrangement differs from the present table.
   - 1874: a coordinate-type system in which 2 digits from 「一～七」 represent a kana, in iroha order (line 31 of the page).
   - The 1894 「数字暗号」: a 10×10 table reconstructed from C06060666300, C06060668300 and C06060799800. The figure (meijiarmy3.jpg, fetched on 2026-10-20 and inspected visually) is in iroha order, with voiced kana following the unvoiced ones. It is not rows (vowels) × columns (consonants) of the gojūon.
   - The section on 「鑰号暗号」 on the same page says 「具体的内容はわからない」 (the specific contents are not known) and has no description of decipherment.
2. **The assignment of a name is undecided.** Candidates for the 「数字暗号」 used in 1902–04 are Kongō (坤号) (1896 to January 1901; C06082459900, C07082181400) and the 「数字ノ分」 of Tokugō (特号) (C03025477100). Cryptiana's English version (meijiarmy_e.htm, line 63) also says that whether Tokugō succeeded Kongō is "yet to be confirmed." No document describing the contents of the table was found for either. This agrees with the work record's "Yakugō (鑰号) or undetermined." No ground for writing this table as the "table of Yakugō (鑰号)" was found in this check either.
3. **Pairs of plain text and cipher text:** the records of C09122909900, C09122911500 and C03020059400 carry contemporary decoded texts (according to the work record; the images were not viewed in this check). These are pairs in the original records, not documents describing the table or the method. C09123116600 is said to have no decoded text.

## Sources searched and results (all dates 2026-10-20)
| Source searched | Method | Result |
|---|---|---|
| Cryptiana: meijiarmy.htm, meijiarmy_e.htm, meiji.htm, meijinavy.htm, unsolved.htm, jtelegraph.htm, meiji1904.htm, meijijapan.htm, meijijapan2.htm, jcipherdisk.htm, security.htm, crypto.htm (index) | Re-fetched with curl (cp932); grep for 「鑰」, 「数字暗号」, 「二桁」, 「五十音」, 「段」, 「C09122」, 「C09123」, 「C03020」 and so on; the Army, Navy and diplomatic sections were read | No description of the present table. As in the previous item, the coordinate systems of 1874 and 1894 exist but the arrangement differs. The 「1904年のカナ暗号」 in meiji.htm (Foreign Ministry, 2 digits + 5-digit separation) is also a serpentine arrangement in iroha order. unsolved.htm has no entry for the Japanese Army of the Meiji period |
| Works by Nagata Yoriyuki (『暗号』 etc.) and Hiyama Yoshiaki, 『暗号を盗んだ男たち』 | Web search (Japanese) and the NDL full-text search API (lab.ndl.go.jp/dl/api/book/search) | 「鑰号暗号」 and 「坤号暗号」: 0 hits. 「陸軍電信符号」: 12 hits (collections of regulations on accounting and hygiene, etc.; not books on ciphers). **The main texts could not be read** (see "Sources that could not be checked" below) |
| JACAR catalogue (full-text search, 3-second intervals, rows=100) | The terms 「鑰号」 (10 hits), 「数字暗号」, 「暗号表」, 「陸軍暗号」, 「暗号解読」. The full catalogue texts of C08010012300, C08010165300, C03025477100, C03023117900, C02030240100 and C03025713100 were read | All are administrative documents about names, distribution, return and requisition, with no description of the contents of a table or of decipherment. C03023117900 (1898) has 「９９欄」, 「５０欄」, 「８０欄」 and 「９０欄」 in an 「い号表」 of the Kongō (坤号) type, a form of table in which words and personal names are entered in numbered fields, but it is not known whether it is gojūon rows × columns |
| CiNii Research API | 「陸軍 暗号 明治」, 「陸軍 暗号 日露戦争」, 「鑰号」, 「数字暗号 仮名 明治」, 「電信 暗号 明治 陸軍省」, 「大野哲弥 暗号」 and so on | The closest are four papers by Ōno Tetsuya (情報化社会・メディア研究: 2009 Taiwan Expedition, 2010 the Army Ministry cipher of Meiji 7, 2012 Satsuma Rebellion, 2014 First World War). Their titles concern 1874–77 and 1914; none has a title treating 1902–04. **The main texts were not read** |
| J-STAGE API | 「明治 陸軍 暗号」 (114 hits), 「日露戦争 暗号 電信 陸軍」, 「鑰号」, 「陸軍電信符号 暗号」 | None of the titles of the top 15 hits applies (Noborito Laboratory, Anglo-Japanese Alliance, etc.) |
| Cyphersolver ledger (ledger/, version 04457698 of 2026-10-14; not re-fetched with gh) | The 74 items of catalogue.json were searched for Japan, JACAR, 陸軍, Meiji, kana and Russo; the whole repository was grepped for japanese army, Meiji, JACAR, kagigo, yakugo, 鑰 and C0912; gh issue search (dbourdeau/cyphersolver for Japan and JACAR) | The only hits are around Sun Yat-sen (1916–17, B03050…). No Army item of the Meiji period |
| Cryptoole (satorunet/cryptoole, e5c78ed, not updated since 2026-10-14) | gh search code (repository specified; 「陸軍」, "Meiji") | No hits |
| satoru.net/crypt/ | Fetched and grepped (陸軍, 明治, 鑰, 1902, JACAR, 数字暗号) | No hits |
| GitHub (gh search code / repos) | The 4 reference codes; 「鑰号 暗号」; 「陸軍 数字暗号 仮名 段 行」; "Meiji army telegram cipher JACAR"; 「日露戦争 暗号電報 解読」; "kana two-digit cipher 1902"; repos for yakugo cipher, meiji army cipher, japanese army cipher, cryptiana and others | Nothing relevant (the code search for 「鑰」 gave only glyph tables). The repos search for cryptiana gave only jamiechong/artichoke (a Jefferson cipher) |
| Web search (standard mode, Japanese and English, about 8 queries) | The reference codes, Ōno Tetsuya, Nagata Yoriyuki, 鑰号/坤号/特号, "Meiji army numeric kana cipher 1902", "Russo-Japanese War Japanese army cipher" | No hits (what appeared: Wikipedia's "Japanese cryptology from the 1500s to Meiji" has a section on Army ciphers of about 1941 but does not describe the Meiji Army; an NDL column; MAGIC; etc.) |
| Wikipedia (en) "Japanese cryptology from the 1500s to Meiji"; NDL column 「近代暗号」 (ndl.go.jp/modern/column/02.html) | Fetched and grepped | No description of the numeric ciphers of the Meiji Army |

## Sources searched where nothing was found (the extent to which it can be said there was nothing)
- The sources marked "none" in the Result column of the table above. However, JACAR's full-text search draws only about the first 350 characters of the catalogue (according to the work record). Explanations written only in the frames of the main text cannot be picked up. GitHub's code search is weak on Japanese terms.

## Sources that could not be checked
- **NDL Search OpenSearch API:** HTTP 429 (limit on simultaneous accesses). Stopped without repeating. The NDL full-text search API could be used instead (table above).
- **The main texts of Nagata Yoriyuki, 『暗号』 and 『ながた暗号塾入門』; Hiyama Yoshiaki, 『暗号を盗んだ男たち』; Ōno Tetsuya, 『国際通信史でみる明治日本』 and others:** not read (the contents of NDL personal-transmission books were not obtained). Nagata's 『暗号』 is cited by Cryptiana (pp. 145–151, in the Navy section of meijinavy.htm), but whether it has a description corresponding to the Army's numeric cipher of 1902–04 could not be confirmed.
- **Books and materials of the National Institute for Defense Studies (the physical items on the use of Yakugō (鑰号), Kongō (坤号) and Tokugō (特号)):** those without images in JACAR. An inquiry to the archive is needed.
- **HathiTrust:** the full-text search URL was tried once with curl and stopped at HTTP 403 (Cloudflare's "Just a moment..." check). No circumvention was tried.
- **DECODE:** login is required. The URL was not tried.
- **Google Books:** not tried.
- **Bulletins, coterie magazines and personal sites not in CiNii:** there is no means of searching them. Mr. Tomokiyo of Cryptiana has not been contacted.
- The images of the four papers by Ōno Tetsuya and of the documents Cryptiana cites (such as the 1894 telegrams, C06060666300) were not opened in this check.

---

# Addition: the 1901 table (2026-11-10)

Date of check: 2026-11-10. Checker: a separate reader (Claude Sonnet) who took no part in rebuilding the table. It received the table (00 ア to 67 ン) and the reference codes of the seven telegrams, and searched with the intention of showing that this had already been published. The ledger part was repeated by the side that rebuilt the table, on the latest version (origin/main 77d4c6c39, 2026-11-10 04:17 UTC).

## Category: the readings exist (contemporary translations); no publication of this table was found
- All seven telegrams have their contemporary translations, which are also transcribed in the JACAR catalogue records. The telegrams were read at the time; what is new here is only the reconstruction of the table.
- No source in the range below gives the table itself (the syllabary by vowel rows, voiced and half-voiced kana right after the plain ones, numbered from 00). No claim of priority is made.

## Sources searched and results
- **Cryptiana (Satoshi Tomokiyo)**
  - meijiarmy2.htm (2026-10-24): the page on the 1902-04 table (row/column coordinates). C09122806100 is headed "An Unidentified Code", "This appears to be in some different code"; no table is reconstructed. The other six reference codes do not occur.
  - meijiarmy.htm: the "Tokugō cipher (numeric part)" is thought to be the successor of the Kongō cipher, "but unknown". No table. The reconstructed 1894 numeric cipher is numbered differently (in the Fukushima example on that page: い01, ま41, や40, あ52, ん69).
  - meijijapan2.htm: the Foreign Ministry's 1904 kana code (one kana = two digits, sent in groups of five, two tables). The layout is close; the grid is different.
  - unsolved.htm (last updated 2026-11-05): no mention of Tokugō, 1901, Fukushima or C091228.
- **Cyphersolver ledger** (origin/main 77d4c6c39): C09122805800, C09122805900, C09122806000, C09122801000, C09122796200, C09122724200: no hits. C09122806100 only as "not read with the 1902 table" in targets/army1902. Catalogue 715 (the five drafts sent by the General Staff): "no decipherment, key or Japanese reading". Nothing in issues or pull requests.
- **GitHub**: code search (特号暗号, "53645 83718", "00161 21108", the reference codes): none. Repository search: only this repository.
- **Web search** (four searches, Japanese and English): no table or paper found.
- **JACAR catalogue records** (seven): the content field is the transcribed translation; no digit-to-kana correspondence or table (the head of each field was read).

## Not checked
- The Cryptiana blog (its search URL returned 404).
- Title searches in CiNii, J-STAGE and NDL Search (not done).
- The texts of the books of Nagata Junkō, Sasaki Takashi and Ōno Tetsuya (not read; it cannot be said that they do not mention it).
- The originals at the National Institute for Defense Studies (the instructions for Tokugō, the table itself).

---

# Addition: the five outgoing drafts of 1901 (2026-11-10)

Date: 2026-11-10. Checker: a separate reader who took no part in finding the table (Claude Sonnet). Given the five reference codes, part of the digits, the table and the reading, the checker looked, with the aim of refuting, for an earlier reading or a printed plaintext. The ledger and Cryptiana's meijiarmy2.htm were also looked up again on the side that found the table.

## Category: not found
- Within the range below, neither a plaintext of the five drafts nor a reading by anyone else was found. This is not a claim to be the first.

## Where we looked
- **Cyphersolver ledger** (origin/main 8ccc45534, 2026-11-10 10:01 UTC): searched the whole tree for the five reference codes, Tamura, Fukushima, 41411, 02624, "99603 52109", Himeji, Waldersee, 通報綴, 福島安正, 田村怡与造. The hits are the entry for catalogue 715 and its survey notes (catalogue.json, docs/solve/715.html, working files under research/jacar/), all "no decipherment". Himeji, Waldersee, 福島安正, 田村怡与造: no hits. In issues and pull requests (the 100 most recently updated, and searches), the only items on catalogue 715 or the 1901 army telegrams are the reports from this repository; no reading by anyone else.
- **Cryptiana (Tomokiyo Satoshi)**: unsolved.htm has no item on Tamura, Fukushima or 1901 army telegrams. meijiarmy.htm (2014-10-19) does not mention the five. The only 1901 telegram in meijiarmy2.htm (2026-10-24) is C09122806100. Nothing in the 20 latest blog posts.
- **satoru.net/crypt/**: nothing.
- **GitHub**: repository search finds only this repository. In code search the reference codes occur only in the ledger's survey notes. Digit groups ("41411 45248" etc.) hit large numbers of unrelated tables and could not be used.
- **Web search** (six searches in Japanese and English: Tamura Iyozō to Fukushima Yasumasa 1901, the Russo-Chinese secret agreement with Li Hongzhang and Zhang Zhidong, Waldersee's visit to Japan, 通報綴, etc.): no edition, article or source collection giving the text of the five.
- **JACAR catalogue** (C09122809400, C09122808400 and others): the content field is the cipher text as transcribed; no record giving a translation or draft under another reference code was seen. The Japanese draft C09122808100 in the same file (on the Field Marshal's visit) is not the plaintext of any of the five. The catalogue gives "Lt.-Gen. Yamaguchi" as creator of C09122809400 (the draft has a marginal note "send the full text of this telegram to Divisional Commander Yamaguchi as well"; the signature reads Tamura).

## Not checked
- NDL Search, CiNii, J-STAGE (not searched).
- The text of 『日本外交文書』 vol. 34 and of source collections on Fukushima Yasumasa (not read; it cannot be said that they do not contain it).
- Individual records of Cryptoole (only the search page was seen).
- The second half of the item list of the file (only the first 20 items of the catalogue list; in images, C09122807700–C09122809900, C09122810100 and C09122812300 were viewed).
- The Cryptiana pages and the web searches were read through a summarising fetch, so something may have been missed.
