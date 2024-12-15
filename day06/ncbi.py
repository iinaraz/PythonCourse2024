from Bio import Entrez
from datetime import datetime
import os
import argparse

Entrez.email = "iina.takala@weizmann.ac.il"

def ncbi_search(term, dir, database="nucleotide", n_results=10):

    date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # Handle the Search
    handle = Entrez.esearch(db=database, term=term, idtype="acc", retmax=n_results)
    record = Entrez.read(handle)
    handle.close()

    if len(record["IdList"]) > 0:

        total_results = int(record["Count"])

        with open(os.path.join(dir, "date.txt"), "w") as date_file:
            date_file.write(date)

        with open(os.path.join(dir, "database.txt"), "w") as db_file:
            db_file.write(database)

        with open(os.path.join(dir, "term.txt"), "w") as term_file:
            term_file.write(term)

        with open(os.path.join(dir, "max.txt"), "w") as max_file:
            max_file.write(str(n_results))

        with open(os.path.join(dir, "total.txt"), "w") as total_file:
            total_file.write(str(total_results))

    
        return(date, database, term, n_results, total_results)
    
    else:
        print(f"No search results found for {term}")


def print_file_contents(dir):

    file_contents = []
    file_order = ["date.txt", "database.txt", "term.txt", "max.txt", "total.txt"]

    # Read each file's contents and store them
    for file in file_order:
        file_path = os.path.join(dir, file)
        with open(file_path, "r") as f:
            content = f.read().strip()  # Strip to remove leading/trailing whitespace
            file_contents.append(content)

    # Join all the contents with a comma
    combined_contents = ", ".join(file_contents)

    return(combined_contents)


if __name__ == "__main__":

    parser = argparse.ArgumentParser()
    parser.add_argument("--organism", help="Name of the organism", type = str, required = True)
    parser.add_argument("--gene", help="Name of the gene", type = str, required = True)
    parser.add_argument("--database", help="Database to use: nucleotide, protein, genome", type = str, required = False, default="nucleotide")
    parser.add_argument("--n_results", help="Number of search results to save", type = int, required = False, default=10)
    # parser.add_argument("--dir", help="Directory for the search", type = str, required = False)
    args = parser.parse_args()

    orgnsm = args.organism
    gene = args.gene
    term = orgnsm + " " + gene

    database = args.database
    n_results = args.n_results

    directory_name = os.path.join("ncbi_search", term, database)

    print("date,database,term,max,total")

    # Check if a folder with the same name exists
    if os.path.exists(os.path.join(directory_name)):
        print("Search results exist")
        print(print_file_contents(directory_name))
    else:
        print("New search")
        os.makedirs(directory_name)
        print(ncbi_search(term, directory_name))


    












#     # Handle the selection of accession
# def select_accession(gene, accessions, database):

#     gene_name = gene.lower()

#     handle = Entrez.esummary(db=database, id=",".join(accessions))
#     record = Entrez.read(handle)

#     for docsum in record:
#         # Extract the title or gene name (you may need to adjust the tag here based on the db and record structure)
#         title = docsum.get("Title", "").lower()

#         # Check if the gene name is in the title (case-insensitive)
#         if gene_name in title:
#             return docsum["Accession"]  # Return the matching accession number

#     # If no match is found
#     return None

# # Handle Genbank Accession
# doc_id = record["IdList"][0]

# handle = Entrez.efetch(db="nucleotide", id=doc_id, rettype="gb", retmode="text")
# data = handle.read()
# handle.close()
# print(data)

# filename = "temp.data"
# with open(filename, "w") as fh:
#     fh.write(data)

# file_type = "genbank"
# for seq_record in SeqIO.parse(filename, file_type):
#     print(seq_record.id)
#     print(repr(seq_record.seq))
#     print()
#     print(seq_record.seq)
#     print()
#     print(len(seq_record.seq))
#     print()
#     print(seq_record.name)
#     print()
#     print(seq_record.annotations)
