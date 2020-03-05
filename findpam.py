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


# Find the reverse complementary sequence of FASTA. Because the DNA is a double-stranded structure and the read
# direction is from 5' to 3', when detecting the PAM sequence of another chain, the complementary sequence needs to
# be read in reverse.
def reverse_complement(seq):
    complement = []
    for i in range(0, len(seq)):  # Follow base complementary pairing to replace bases one by one
        if seq[i] == "A":
            complement += "T"
        elif seq[i] == "T":
            complement += "A"
        elif seq[i] == "C":
            complement += "G"
        else:
            complement += "C"
    complement = ''.join(complement)
    reverse_complement = complement[::-1]  # Read the entire sequence in reverse
    return reverse_complement


# Read the entire FASTA sequence from the 20th base. If two consecutive G bases appear, enter the previous 20 base
# sequences into the list and start a new line until the entire FASTA file is read.
def positive_PAM(seq):
    forward = []
    for i in range(20, len(seq) - 1):
        if seq[i] == "G" and seq[i + 1] == "G":
            forward += seq[i - 20:i] + "\n"
    forward = ''.join(forward)
    return forward



# Read the reverse complementary strand in the forward direction and look for the PAM sequence again from 5' to 3'.
def negative_PAM(seq):
    opposite = []
    for i in range(20, len(seq) - 1):
        if seq[i] == "G" and seq[i] == "G":
            opposite += seq[i - 20:i] + "\n"
    opposite = ''.join(opposite)
    return opposite



def main():
    # You can change the filename to read and input any AFSTA file. "rh" and "rb" are header and baselist respectively.
    filename = "sequence.fasta"  # Change the file name when you use this python file.
    rh = ReadFASTA(filename).read_fasta_head()
    rb = ReadFASTA(filename).read_fasta_base()
    sequence = "".join(rb)  # Change the list as a string to search for PAM later.
    rc_sequence = reverse_complement(sequence)
    ForwardPAM = positive_PAM(sequence)
    ReversePAM = negative_PAM(rc_sequence)

    print("Gene sequence is:")
    for i in range(len(rh)):  # I use a "for" loop here because rh(read header) is a "list".
        print(rh[i])
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


if __name__ == "__main__":
    main()
