# Printing sequence features

The analyzer will print features from your sequence stored in your fasta file. Simply call functions to print the longest repeating subsequence on your file, and/or to print amino acid statistics (sequence length, percentage of each amino acid in the sequence and histogram of the occurences.) To use the program, follow the instructions below.

### Install requirements:

```
pip install -r requirements.txt
```

### Run program from command line:

```
python analyzer.py file --longest_subseq --features
```

## Notes:

Providing the file path is mandatory. Calling for functions is optional (but if no function is called, nothing is printed)
