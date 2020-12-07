# Bilingual-Sentence-Aligner

The code in this repo could be utilized to find matching sentence pairs btween to TXT files, by making use of Google's recent LaBSE model.
This is a simplified implementation of the same using PolyFuzz library.

To install necessary packages for the script, run:

    pip install -r requirements.txt

To view script usage help from terminal, run:

    python3 exec_[scriptname].py -h

### exec_alignfiles.py

The script accepts 2 TXT files as input and starts finding matching pairs using LaBSE.
Along with TXT files, file encoding type and output filename must be specified.

To initiate the process:

    python3 bilingual_sentence_aligner.py -i1 "input1.txt" -i2 "input2.txt" -e "utf-8" -o "out.csv"

NOTE : The Two text files are expected to have tokenized sentences for pairing.

The output will be a CSV file with 3 columns:

* COLUMN-1 : Sentence from TXT file 1
* COLUMN-2 : Matching Sentence from TXT file2 corresponding to COLUMN-1
* COLUMN-3 : Similarity between COLUMN-1 & COLUMN-2