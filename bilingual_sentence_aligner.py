############################################################################################################
# AIM     : Script to matching sentence pairs provided in two different TXT files
# USAGE   : python3 bilingual_sentence_aligner.py -i1 "input1.txt" -i2 "input2.txt" -e "utf-8" -o "out.csv"
############################################################################################################

import sys
import argparse
import pandas as pd
from datetime import datetime
from sentence_transformers import SentenceTransformer
from polyfuzz import PolyFuzz
from polyfuzz.models  import Embeddings
from flair.embeddings import TransformerWordEmbeddings
from flair.embeddings import SentenceTransformerDocumentEmbeddings

startTime = datetime.now()
#model initialization
embeddings = SentenceTransformerDocumentEmbeddings('LaBSE')
LaBSE = Embeddings(embeddings, min_similarity=0, model_id="LaBSE")
model = PolyFuzz([LaBSE])


msg = "Adding description"

# Initialize parser & add arguments
parser = argparse.ArgumentParser(description = msg)
parser.add_argument("-i1", "--input1", help = "Input txt file1")
parser.add_argument("-i2", "--input2", help = "Input txt file2")
parser.add_argument("-o", "--output", help = "Output CSV file")
parser.add_argument("-e", "--encoding", help = "TXT encoding type (utf8 or utf-16)")
args = parser.parse_args()

if args.input1 is None:
    sys.exit("ERROR : input variable missing!")

if args.input2 is None:
    sys.exit("ERROR : input variable missing!")

if args.output is None:
    sys.exit("ERROR : output variable missing!")

if args.encoding is None:
    sys.exit("ERROR : encoding type missing!")


print("Passed inputs : ")
print("----------------")
print("Input File1 : " + args.input1)
print("Input File2 : " + args.input2)
print("Output File : " + args.output)
print("Enc Type    : " + args.encoding)


input_path1  = args.input1
input_path2  = args.input2
output_path  = args.output
enctype      = args.encoding


with open(input_path1, encoding=enctype) as f1:
    lst1 = f1.readlines()

with open(input_path2, encoding=enctype) as f2:
    lst2 = f2.readlines()

#perform matching
model.match(lst1, lst2)
dfx = model.get_matches()
dfx.columns = ['COLUMN-1', 'COLUMN-2', 'SIMILARITY']
dfx.sort_values(by='SIMILARITY', ascending=False)
dfx.to_csv(output_path,index=None)
print("Execution completed in :",datetime.now() - startTime)
