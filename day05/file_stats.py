import sys

def count_nucleotides(file_path):
    # Initialize counters for nucleotides
    A_count = 0
    T_count = 0
    C_count = 0
    G_count = 0

    # Open the file and read its content
    with open(file_path, 'r') as file:
        for line in file:
            # Clean line (remove newlines and spaces)
            line = line.strip()
            
            # Count occurrences of each nucleotide
            A_count += line.count('A')
            T_count += line.count('T')
            C_count += line.count('C')
            G_count += line.count('G')
    
    # Calculate the total number of nucleotides
    total_nucleotides = A_count + T_count + C_count + G_count
    
    # Calculate percentages
    A_percent = (A_count / total_nucleotides) * 100
    T_percent = (T_count / total_nucleotides) * 100
    C_percent = (C_count / total_nucleotides) * 100
    G_percent = (G_count / total_nucleotides) * 100
    
    # Calculate GC content
    GC_content = (G_count + C_count) / total_nucleotides * 100
    
    # Print the results
    print(f"A: {A_count} ({A_percent:.2f}%)")
    print(f"T: {T_count} ({T_percent:.2f}%)")
    print(f"C: {C_count} ({C_percent:.2f}%)")
    print(f"G: {G_count} ({G_percent:.2f}%)")
    
    # Check the GC content and print the message
    if GC_content > 60:
        print("High GC content")
    else:
        print("Low GC content")

if __name__ == "__main__":
    # Ensure the script receives a file path as a command-line argument
    if len(sys.argv) != 2:
        print("Usage: python file_stats.py <file_path>")
        sys.exit(1)

    # Get the file path from command line argument
    file_path = sys.argv[1]
    
    # Call the function to count nucleotides and GC content
    count_nucleotides(file_path)
