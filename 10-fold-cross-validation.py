from modules.token import sentences

import argparse
import codecs

if __name__ == '__main__':

    print "Starting 10-fold cross validation ..."

    argpar = argparse.ArgumentParser(description='')

    argpar.add_argument('-i', '--infile', dest='in_file', help='in file', required=True)
    argpar.add_argument('-t', '--train-fold', dest='train_fold', help='train fold', default='1')
    argpar.add_argument('-s', '--splits', dest='splits', help='splits', default='1')
    argpar.add_argument('-o1', '--output1', dest='output_file_1', help='output file', default='output.txt')
    argpar.add_argument('-o2', '--output2', dest='output_file_2', help='output file', default='output.txt')

    args = argpar.parse_args()

    sentence_count = 0
    for sentence in sentences(codecs.open(args.in_file, encoding='utf-8')):
        sentence_count += 1

    print "\tNumber of sentences: {0}".format(sentence_count)

    sentences_per_split = round(sentence_count/int(args.splits), 0)

    print "\tSentences per split: {0}".format(sentences_per_split)

    nine_folds = []
    one_fold = []

    split_count = 0
    sentence_count_2 = 0

    for sentence in sentences(codecs.open(args.in_file, encoding='utf-8')):

        sentence_count_2 += 1

        if sentences_per_split * (int(args.train_fold) - 1) < sentence_count_2 <= sentences_per_split * int(args.train_fold):
            train = True
            one_fold.append(sentence)

        else:
            nine_folds.append(sentence)

    print "\t# Sentences in the one-fold file: {0}".format(len(one_fold))
    print "\t# Sentences in the nine-fold file: {0}".format(len(nine_folds))

    with open(args.output_file_1, "a") as o:
        for sentence in one_fold:
            for token in sentence:
                print >> o, token.original_form + "\t" + token.gold_pos
            print >> o, ""

    with open(args.output_file_2, "a") as o:
        for sentence in nine_folds:
            for token in sentence:
                print >> o, token.original_form + "\t" + token.gold_pos
            print >> o, ""
