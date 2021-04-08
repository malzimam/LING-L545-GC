THE TEN DEPENDENCY SENCETNCES

- The sentence number is different one number before depending on the UD Annotatrix page ([Fran's GitHub pages](https://ftyers.github.io/ud-annotatrix/) or [Jonathan's GitHub Pages](https://jonorthwash.github.io/ud-annotatrix)).
- The most errors are related to copula verb structure; When the copula is omitted, the copula complement (nominal or adjectival) should be annotated as ROOT. However, when the copula is overtly present on surface, it should be annotated as ROOT. The following errors explain: 

I-

The sentence number in TESTINGOUT.conllu: (2) 

بالنسبة إلى أولئك الذين يتابعون الانتقال الخاص بوسائل التواصل الاجتماعي في الكابيتول هيل, سيكون الأمر مختلفاً بعض الشيء.

The error is: 

The root in the sentence is ADJ (مختلفا) but it should be the copula verb (يكون) because it is not omitted in the sentence.  

II-

The sentence number in TESTINGOUT.conllu: (9) 

لربما كان الزي الواجب ارتداؤه خانقاً زيادة عن اللزوم.

The error is: 

The root in the sentence is ADJ (خانقاً) but it should be the copula verb (كان) because it is not omitted in the sentence.  

III-

The sentence number in TESTINGOUT.conllu: (17) 

ثمة أوجه تشابهٍ هنا بين الألعاب وحياتنا اليومية.

The error is: 

The root in the sentence is NOUN (أوجه) but it should be the ADP (بين) because the copula verb is omitted, so the copula complement (ADP) should be annotated as ROOT. 

IV-

The sentence number in TESTINGOUT.conllu: (17) 

قد يكون "خنزير" خنزيراً وحيداً, غير أنه لا يترك وحده أبداً

The error is: 

The root in the sentence is NOUN (خنزيراً) but it should be the copula verb (يكون) because it is not omitted in the sentence.  

V-

The sentence number in TESTINGOUT.conllu: (21) 

قال السيد بانفالكار أنه شعر ذات مرة أن عليهم ترك المبنى.

The error is: 

The NOUN (ترك) is annotated as obj but it is not because the embedded sentences (أن عليهم ترك المبنى) does not have a verb for the object.



VI-

The sentence number in TESTINGOUT.conllu: (29) 

ويتجلى هذا بأبهى صوره عندما يكون اسم الشخص الشهير نادرا جدا في البداية.

The error is: 

The root in the sentence is ADJ (نادرا) but it should be the copula verb (يكون) because it is not omitted in the sentence.  

VII-

The sentence number in TESTINGOUT.conllu: (38) 

أحياناً يكون أشبه بقوة عظمى.

The error is: 

The root in the sentence is ADJ (أشبه) but it should be the copula verb (يكون) because it is not omitted in the sentences.  

VIII-

The sentence number in TESTINGOUT.conllu: (42) 

لم ير الطائرات من قبل سوى بعض المدونين.

The error is: 

The NOUN (المدونين) in the sentence is not modified as nsubj** but it is**.** The verb (ير) needs a subj but has not.

IX-

The sentence number in TESTINGOUT.conllu: (112) 

باتت هواتفنا المحمولة أكثر من مجرد هواتف هذه الأيام.

The error is: 

` `the ADJ (أكثر) is annotated mistakenly as the ROOT in this sentence. The AUX (باتت) should be annotated as VERB and be the ROOT as in the sentence number (137)**.** The two verbs in the two sentence are from the same verb category in Arabic.

X-

The sentence number in TESTINGOUT.conllu: (170) 

أكثر من 330 فرداً من الطاقم موجودون على متن السفينة

The error is: 

` `The ADJ (أكثر) is annotated mistakenly as the ROOT is in this sentence but the ADJ (موجودون) which should be annotated as the ROOT because the copula verb is omitted, so the copula complement (The ADJ (أكثر)) is annotated as ROOT 

