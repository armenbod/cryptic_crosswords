# Pleaase change config as necessary

# Dataset paths
clues_path_raw = './data/clues.csv'
clues_path_processed = './data/clues_processed.csv'
clues_path_train = './data/clues_train.csv'
clues_path_validation = './data/clues_validation.csv'
clues_path_test = './data/clues_test.csv'

# Modelling parameters
model_name_t5 = 'google/t5-small-ssm'
batch_size = 192
lr = 2e-3
num_epochs = 25
max_seq_length = 64 

# Output path
output_dir = './tmp/debug_seq2seq_xword/'
overwrite_dir = True
predictions_path = f'{output_dir}/test_predictions_{output_dir}.json'