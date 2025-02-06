import argparse
from Bio import SeqIO

def parse_fastq(file1, file2):
    with open(file1, "r") as f1, open(file2, "r") as f2:
        for record1, record2 in zip(SeqIO.parse(f1, "fastq"), SeqIO.parse(f2, "fastq")):
            print("File 1:", record1.id, record1.seq, record1.letter_annotations["phred_quality"])
            print("File 2:", record2.id, record2.seq, record2.letter_annotations["phred_quality"])

def main():
    parser = argparse.ArgumentParser(description='Process paired-end FASTQ files.')
    parser.add_argument('file1', type=str, help='Path to the first FASTQ file')
    parser.add_argument('file2', type=str, help='Path to the second FASTQ file')
    
    args = parser.parse_args()
    
    parse_fastq(args.file1, args.file2)

if __name__ == "__main__":
    main()
