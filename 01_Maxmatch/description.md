Description of Maxmatch
This python program implements maximum matching method that uses an algorithm to segment languages that do not use spaces to modify word-boundaries such as Japanese. 
The program needs a dictionary (wordlist) of Japanese I called japanese.dic. 
The program takes a string from the input (ja_gsd-ud-test.conllu.input)and matches the longest word in japanese.dic with it from the beginning. 
After that, it sends the matching word from input to output (ja_gsd-ud-test.conllu.output) and then does the same with the rest of the string. 
When no word is matched in japanese.dic, the program creates words of one character. The following example explains it works:
Input: 
これに不快感を示す住民はいましたが,現在,表立って反対や抗議の声を挙げている住民はいないようです。
Output: 
これ に 不快 感 を 示す 住民 はい まし た が , 現在 , 表 立っ て 反対 や 抗議 の 声 を 挙げ て いる 住民 はい ない よう です 。
Finally, I evaluate the output by using Word Error Rate calculating code (WER). The error average is 6.434.

