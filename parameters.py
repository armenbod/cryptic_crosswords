# Pleaase change config as necessary

# Dataset paths
clues_path_raw = './data/clues.csv'
clues_path_processed = './data/clues_processed.txt'
clues_path_train = './data/clues_train.txt'
clues_path_validation = './data/clues_validation.txt'
clues_path_test = './data/clues_test.txt'

# Modelling parameters
model_name_t5 = 'google/t5-small-ssm'
batch_size = 192
lr = 2e-3
num_epochs = 25
max_seq_length = 64 

# Output path
output_dir = './tmp/debug_seq2seq_xword_v3/'
overwrite_dir = True
predictions_path = f'test_predictions_{output_dir}.json'