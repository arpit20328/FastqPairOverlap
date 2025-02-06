import argparse
from Bio import SeqIO
import gzip

def parse_fastq(file1, file2):
    records1 = []
    records2 = []
    open_func = gzip.open if file1.endswith('.gz') else open
    with open_func(file1, "rt") as f1, open_func(file2, "rt") as f2:
        for record1, record2 in zip(SeqIO.parse(f1, "fastq"), SeqIO.parse(f2, "fastq")):
            records1.append(record1)
            records2.append(record2)
    return records1, records2

def main():
    parser = argparse.ArgumentParser(description='Process paired-end FASTQ files.')
    parser.add_argument('file1', type=str, help='Path to the first FASTQ file')
    parser.add_argument('file2', type=str, help='Path to the second FASTQ file')
    
    args = parser.parse_args()
    
    records1, records2 = parse_fastq(args.file1, args.file2)
    
    # Store the records in files or process them as required
    with open("output_file1.txt", "w") as out1, open("output_file2.txt", "w") as out2:
        for record in records1:
            out1.write(f"{record.id}\t{record.seq}\t{record.letter_annotations['phred_quality']}\n")
        for record in records2:
            out2.write(f"{record.id}\t{record.seq}\t{record.letter_annotations['phred_quality']}\n")

if __name__ == "__main__":
    main()
