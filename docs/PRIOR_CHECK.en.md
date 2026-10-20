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
