fname = 'train_data_kaggle.txt'
positive_text = 'positive_text.txt'
negative_text = 'negative_text.txt'

positive_lines = 0;     # 3995
negative_lines = 0;     # 3091
with open(fname) as f:
    content = f.readlines()

content = [line.strip('\n') for line in content]

for line in content:
    pos_or_neg = line.split('\t')[0]
    text = line.split('\t')[1]
    if pos_or_neg == '1':
        positive_lines += 1;
        with open(positive_text,'a') as myfile:
            myfile.write(text + '\n')
    elif pos_or_neg == '0':
        negative_lines += 1;
        with open(negative_text, 'a') as myfile:
            myfile.write(text + '\n')

print(positive_lines , negative_lines)