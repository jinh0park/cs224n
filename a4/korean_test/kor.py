from Korpora import Korpora
corpus = Korpora.load("korean_parallel_koen_news")

src = corpus.train.get_all_pairs()  # eng
tgt = corpus.train.get_all_texts()  # kor

test_src = corpus.test.get_all_pairs()
test_tgt = corpus.test.get_all_texts()


with open('./train.kor', 'w', encoding='UTF-8') as f:
    for sent in tgt:
        f.write(sent + '\n')

with open('./train.en', 'w', encoding='UTF-8') as f:
    for sent in src:
        f.write(sent + '\n')

with open('./dev.kor', 'w', encoding='UTF-8') as f:
    for sent in tgt[:300]:
        f.write(sent + '\n')

with open('./dev.en', 'w', encoding='UTF-8') as f:
    for sent in src[:300]:
        f.write(sent + '\n')

with open('./test.kor', 'w', encoding='UTF-8') as f:
    for sent in test_tgt:
        f.write(sent + '\n')

with open('./test.en', 'w', encoding='UTF-8') as f:
    for sent in test_src:
        f.write(sent + '\n')