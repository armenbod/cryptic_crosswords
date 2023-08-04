#  🇨ryptic_ 🇨rosswords with LL🅼s

Using LLMs to generatively produce answers to cryptic crossword clues.


For further information on the use case motivation and methodology, please visit the following:

* For `main.part1.ipynb` : [[Part 1](https://armbod.medium.com/fine-tuning-a-llm-to-generatively-solve-cryptic-crossword-clues-part-1-2-429f50a5953b)]
* For `main.part2.ipynb` : [[Part 2: tbc]()]


## Requirements:

If you are not using Colab, or prefer to create your own environment:

1. You need to install the bleeding edge version of the `transformers` module to run the QA wrapper files (more information on installation options [here](https://huggingface.co/docs/transformers/installation#install-from-source)):
```
! pip install git+https://github.com/huggingface/transformers
```
2. Install the `requirements.txt` file

Otherwise, you can run the cells at the top of the notebook to install the dependencies on Colab.

This has been tested using Python >=3.10.

## Scripts

The trainer and wrapper python files are originally derived from the [HuggingFace transformers](https://github.com/huggingface/transformers/tree/main/examples/pytorch/question-answering) examples page. An addition was made to the runfile to save predictions in a .json format - please compare files with the original commit if interested. 

## Data

The clues dataset has been downloaded from this website: [link](https://cryptics.georgeho.org/data/clues). Please download and save into the ./data folder. I saved the filename as 'clues.csv'.

## Parameters

Editable parameters are kept in the `parameters.py` file.

## Keep Colab Running

Colab may timeout prior to model training completing. Using this ['hack'](https://stackoverflow.com/questions/54057011/google-colab-session-timeout) you can keep the notebook alive. Note that also that using the free version of Colab puts a daily time limit per user to access to GPUs, so running for too many epochs may risk you running out of free resources.



