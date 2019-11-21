import os.path as path
from one_a import PatternCount
from one_b import FrequentWords
# from one_c


def get_dataset(dataset):
    with open(path.join(path.dirname(__file__) + f'/../../datasets/chapter_one/{dataset}.txt'), "r") as f:
        lines = []
        for i in f:
            lines.append(i.strip())
        return lines


if __name__ == "__main__":
    got_data = get_dataset("d_one_2")
    print(PatternCount(got_data[0], got_data[1]))
    print(FrequentWords(got_data[0], 9))
