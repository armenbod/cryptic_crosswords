#  🇨ryptic_ 🇨rosswords with 🇱🇱🅼s

Using LLMs to generatively produce answers to cryptic crossword clues.

For further information on the use case motivation and methodology, please visit the following: [[Part 1: tbc]()] [[Part 2: tbc]()]


## Requirements:

If you are not using Colab, or prefer to create your own environment:

1. You need to install the bleeding edge version of the `transformers` module to run (more information [here](https://huggingface.co/docs/transformers/installation#install-from-source)):
```
! pip install git+https://github.com/huggingface/transformers
```
2. Install the `requirements.txt` file

Otherwise, you can run the cells at the top of the notebook to install the depencies on Colab.

This has been tested using Python >=3.10.

## Scripts

The trainer and wrapper python files are originally derived from the [HuggingFace transformers](https://github.com/huggingface/transformers/tree/main/examples/pytorch/question-answering) examples page. Some minor changes were made - please compare files with the original commit if interested.

## Data

The clues dataset has been downloaded from this website: [link](https://cryptics.georgeho.org/data/clues)

## Parameters

Editable parameters are available in the `param.py` file.


