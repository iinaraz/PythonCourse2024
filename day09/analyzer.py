import argparse
from Bio import SeqIO
import re
import matplotlib.pyplot as plt
from collections import Counter

def extract_sequence_from_file(file_path):

    # Parse the file using SeqIO
    record = next(SeqIO.parse(file_path, "fasta"))
    
    return str(record.seq)

def find_longest_repeated_subsequence(sequence):

    n = len(sequence)
    longest_subseq = ""
    
    # Start checking substrings from the longest possible length
    for length in range(n, 0, -1):
        for i in range(n - length + 1):
            subseq = sequence[i:i + length]
            if len(re.findall(f"(?={re.escape(subseq)})", sequence)) > 1:
                return subseq
            
    return longest_subseq

def amino_acid_features(sequence):

    # Remove whitespace
    sequence = sequence.replace(" ", "").upper()
    
    # Print aa sequence length
    sequence_length = len(sequence)
    print(f"Amno acids total: {sequence_length}")
    
    # Count occurrences of each amino acid
    amino_acid_counts = Counter(sequence)
    
    # Calculate percentage of each amino acid
    print("\nPercentage of each amino acid:")
    for aa, count in amino_acid_counts.items():
        percentage = (count / sequence_length) * 100
        print(f"{aa}: {percentage:.2f}%")
    
    # Plot histogram
    plt.figure(figsize=(10, 6))
    plt.bar(amino_acid_counts.keys(), amino_acid_counts.values(), color='skyblue', edgecolor='black')
    plt.title('Amino Acid Occurrence')
    plt.xlabel('Amino Acids')
    plt.ylabel('Count')
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.show()

def main():

    ## ----------------- SET UP ARGUMENTS -----------------------
    # Create parser
    parser = argparse.ArgumentParser(description="Analyze amino acid sequences.")

    # Add argument for file
    parser.add_argument("file", type=str, help="Path to the input FASTA file.")
    
    # Add arguments for functions
    parser.add_argument("--longest_subseq", action="store_true", help="Find the longest duplicated subsequence.")
    parser.add_argument("--features", action="store_true", help="Analyze amino acid features and show histogram.")
    
    args = parser.parse_args()

    # Save path to file from args
    file_path = args.file
    
    ## --------------------- RUN PROGRAM ---------------------------
    # Extract sequence from the file
    sequence = extract_sequence_from_file(file_path)

    # Optional functions
    if args.longest_subseq:
        longest_subseq = find_longest_repeated_subsequence(sequence)
    
        if longest_subseq:
            print("The longest repeated subsequence is:", longest_subseq)
        else:
            print("No repeated subsequence found.")

    if args.features:
        amino_acid_features(sequence)

if __name__ == "__main__":
    main()