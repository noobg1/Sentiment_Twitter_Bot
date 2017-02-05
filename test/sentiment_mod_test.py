import sys
sys.path.append('../src/')
from sentiment_mod import sentiment_utility


positive_text = 'positive_text.txt'
negative_text = 'negative_text.txt'

positive_lines = 0;     # 3995
negative_lines = 0;     # 3091
positive_lines_false_sentences = []
negative_lines_false_sentences = []

with open(positive_text) as f:
    content_positive = f.readlines()

with open(negative_text) as f:
    content_negative = f.readlines()

for text in content_positive:
    if sentiment_utility(text)['compound'] < 0 :
        positive_lines += 1
        positive_lines_false_sentences.append(text)

for text in content_negative:
    if sentiment_utility(text)['compound'] > 0 :
        negative_lines += 1
        negative_lines_false_sentences.append(text)


print ('pos: {0} out of actual {1}'.format( positive_lines,
len(content_positive)))
print ('neg: {0} out of actual {1}'.format( negative_lines, len(content_negative)))

# print positive_lines_false_sentences
# print(negative_lines_false_sentences)