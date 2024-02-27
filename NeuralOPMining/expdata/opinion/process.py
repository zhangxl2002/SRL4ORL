from datasets import Dataset

def BME2BIO(label):
    if label.endswith("-*"):
        label = label[:-2]
    if label.startswith("E") or label.startswith("M"):
        return "I" + label[1:]
    if label.startswith("S"):
        return "B" + label[1:]
    return label

def BIO2id(label):
    label_to_id = {
        "O": 0,
        "B-AGENT": 1,
        "I-AGENT": 2,
        "B-DSE": 3,
        "I-DSE": 4,
        "B-TARGET": 5,
        "I-TARGET": 6
    }
    return label_to_id[label]


def process():
    # 读取文本文件
    with open("aaai19srl.train.conll", "r", encoding="utf-8") as f:
        lines = f.readlines()

    # 初始化列表以存储数据
    data = []

    # 初始化变量以存储当前句子和标签序列
    current_sentence = []
    current_labels = []

    # 统计标签类别和出现次数的字典
    label_counts = {}

    # 解析文本文件并整理数据
    for line in lines:
        parts = line.strip().split("\t")
        if len(parts) == 1 and current_sentence:  # 新句子的开始
            data.append({"sentence": current_sentence, "labels": current_labels})
            current_sentence = []
            current_labels = []
        if len(parts) == 3:
            current_sentence.append(parts[1])
            label = BME2BIO(parts[2])
            current_labels.append(BIO2id(label))
            if label in label_counts:
                label_counts[label] += 1
            else:
                label_counts[label] = 1

    # 添加最后一个样本
    if current_sentence:
        data.append({"sentence": current_sentence, "labels": current_labels})

    # 打印前几个样本进行检查
    for i, sample in enumerate(data[:5]):
        print(f"{i} {sample['sentence']} {sample['labels']}")

    for label, count in label_counts.items():
        print(f"{label}: {count}")

    dataset = Dataset.from_list(data)
    # dataset.save_to_disk(".")
    dataset.to_json("mpqa.jsonl")

if __name__ == "__main__":
    process()
