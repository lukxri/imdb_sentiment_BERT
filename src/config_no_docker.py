import os
import transformers

# this is the maximum number of tokens in the sentence
MAX_LEN = 512

# batch sizes is low because model is huge!
TRAIN_BATCH_SIZE = 4
VALID_BATCH_SIZE = 4

# let's train for a maximum of 10 epochs
EPOCHS = 10

# define path to BERT model files
# Now we assume that all the data is stored inside
# /home/user/data
BERT_PATH = "../data_bert/"

# this is where you want to save the model
MODEL_PATH = "../data_bert/model.bin"

# training file
TRAINING_FILE = "../data_bert/imdb.csv"

TOKENIZER = transformers.BertTokenizer.from_pretrained(
    BERT_PATH,
    do_lower_case=True
)
