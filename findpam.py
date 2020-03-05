class ReadFASTA:

    def __init__(self, fasta):  # this "__init__" takes one argument which is stored as attributes
        self.fasta = fasta

    # Tead the beginning title, because in a FASTA file, there may be several beginnings with different sequences.
    def read_fasta_head(self):
        headlist = []
        for line in open(self.fasta):
            if line[0] == '>':  # The first character of the title of the FASTA file format is ">".
                header = line.strip("\n")
                headlist.append(header)
        return headlist

    # Read the sequence part, link all base sequences together.
    def read_fasta_base(self):
        baselist = []
        for line in open(self.fasta):
            if line[0] != '>':  # The first character of the title of the FASTA file format is ">".
                baselist.append(line.strip("\r\n"))
        return baselist


# You can change the filename to read and input any AFSTA file. "rh" and "rb" are header and baselist respectively.

filename = "mazF.fa"
rh = ReadFASTA(filename).read_fasta_head()
rb = ReadFASTA(filename).read_fasta_base()
sequence = "".join(rb)  # Change the list as a string to search for PAM later.


# print("Gene sequence is:")
# print(rh)
# print(sequence)


# Find the reverse complementary sequence of FASTA. Because the DNA is a double-stranded structure and the read
# direction is from 5' to 3', when detecting the PAM sequence of another chain, the complementary sequence needs to
# be read in reverse.
def reverse_complement(seq):
    complement = []
    for i in range(0, len(sequence)):  # Follow base complementary pairing to replace bases one by one
        if sequence[i] == "A":
            complement += "T"
        elif sequence[i] == "T":
            complement += "A"
        elif sequence[i] == "C":
            complement += "G"
        else:
            complement += "C"
    complement = ''.join(complement)
    reverse_complement = complement[::-1]  # Read the entire sequence in reverse
    return reverse_complement


rc_sequence = reverse_complement(sequence)


# print()
# print("Reverse complement sequence is:")
# print(rc_sequence)


# Read the entire FASTA sequence from the 20th base. If two consecutive G bases appear, enter the previous 20 base
# sequences into the list and start a new line until the entire FASTA file is read.
def positive_PAM(seq):
    forward = []
    for i in range(20, len(sequence) - 1):
        if sequence[i] == "G" and sequence[i + 1] == "G":
            forward += sequence[i - 20:i] + "\n"
    forward = ''.join(forward)
    return forward


ForwardPAM = positive_PAM(sequence)


# print()
# print("Forward Strand PAM:")
# print(ForwardPAM)


# Read the reverse complementary strand in the forward direction and look for the PAM sequence again from 5' to 3'.
def negative_PAM(seq):
    opposite = []
    for i in range(20, len(rc_sequence) - 1):
        if rc_sequence[i] == "G" and rc_sequence[i] == "G":
            opposite += rc_sequence[i - 20:i] + "\n"
    opposite = ''.join(opposite)
    return opposite


ReversePAM = negative_PAM(rc_sequence)


# print()
# print("Reverse Strand PAM:")
# print(ReversePAM)


def output_file():
    f = open('Guide Sequences.txt', 'w')  # Create and open a text file called "Guide Sequences".
    for a in range(len(rh)):  # I use a "for" loop here because rh(read header) is a "list".
        f.write(rh[a])  # Write headers into the text file.
        f.write('\n')
    f.write('\n')
    f.write("Forward PAM sequences:")
    f.write('\n')
    f.write(ForwardPAM)  # Write forward PAM sequences into the text file.
    f.write('\n')
    f.write("Reverse PAM sequences:")
    f.write('\n')
    f.write(ReversePAM)  # Write reverse PAM sequences into the text file.
    f.close()


output_file()


def main():
    print("Gene sequence is:")
    print(rh)
    print(sequence)
    print()
    print("Reverse complement sequence is:")
    print(rc_sequence)
    print()
    print("Forward Strand PAM:")
    print(ForwardPAM)
    print()
    print("Reverse Strand PAM:")
    print(ReversePAM)
output_file()
if __name__ == "__main__":
    main()