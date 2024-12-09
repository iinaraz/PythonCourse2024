import sys

def count_nucleotides(file_path):
    # Open the file and read the first line
    with open(file_path, 'r') as file:
        sequence = file.readline().strip()
    
    # Initialize counts for each nucleotide
    counts = {'A': 0, 'T': 0, 'C': 0, 'G': 0}
    
    # Count the occurrences of each nucleotide
    for nucleotide in sequence:
        if nucleotide in counts:
            counts[nucleotide] += 1
    
    # Calculate the total number of nucleotides
    total_nucleotides = len(sequence)
    
    # Print the counts and percentages for each nucleotide
    for nucleotide, count in counts.items():
        print(f"{nucleotide}: {count} ({(count / total_nucleotides) * 100:.2f}%)")
    
    # Calculate GC content percentage
    gc_content = (counts['G'] + counts['C']) / total_nucleotides * 100
    
    # Print the GC content classification
    if gc_content >= 60:
        print("High GC content")
    else:
        print("Low GC content")

if __name__ == "__main__":
    import sys
    if len(sys.argv) != 2:
        print("Usage: python file_stats.py <filename>")
    else:
        file_path = sys.argv[1]
        count_nucleotides(file_path)