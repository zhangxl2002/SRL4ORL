from datasets import load_dataset,Sequence,ClassLabel

raw_datasets = load_dataset("zhangxl2002/test")

# raw_datasets["train"][0]["sentence"]

# raw_datasets["train"][0]["labels"]

raw_datasets = raw_datasets.cast_column("labels", Sequence(feature=ClassLabel(num_classes=7, names=['O', 'B-AGENT', 'I-AGENT', 'B-DSE', 'I-DSE', 'B-TARGET', 'I-TARGET'], names_file=None, id=None), length=-1, id=None))

orl_feature = raw_datasets["train"].features["labels"]

# Sequence(feature=ClassLabel(num_classes=7, names=['O', 'B-AGENT', 'I-AGENT', 'B-DSE', 'I-DSE', 'B-TARGET', 'I-TARGET'], names_file=None, id=None), length=-1, id=None)

label_names = orl_feature.feature.names

# raw_datasets["train"].features["sentence"].feature  
# Value(dtype='string', id=None)

# raw_datasets["train"].features["labels"].feature  
# ClassLabel(names=['O', 'B-AGENT', 'I-AGENT', 'B-DSE', 'I-DSE', 'B-TARGET', 'I-TARGET'], id=None)

words = raw_datasets["train"][100]["sentence"]
labels = raw_datasets["train"][100]["labels"]
line1 = ""
line2 = ""
for word, label in zip(words, labels):
    full_label = label_names[label]
    max_length = max(len(word), len(full_label))
    line1 += word + " " * (max_length - len(word) + 1)
    line2 += full_label + " " * (max_length - len(full_label) + 1)

print(line1)
print(line2)