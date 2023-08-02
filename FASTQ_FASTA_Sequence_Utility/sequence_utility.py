import re


def translation(sequence):
    """
    This function takes a DNA sequence and writes it in the codified polypeptide.

    :param sequence: DNA sequence to translate
    :return: sequence_translated: translated sequence
    """

    # Dictionary containing the aminoacids and the codons
    aminoacids = {'TTT': 'F', 'TTC': 'F', 'TTA': 'L', 'TTG': 'L', 'TCT': 'S', 'TCC': 'S', 'TCA': 'S', 'TCG': 'S',
                  'TAT': 'Y',
                  'TAC': 'Y', 'TAA': '*', 'TAG': '*', 'TGT': 'C', 'TGC': 'C', 'TGA': '*', 'TGG': 'W', 'CTT': 'L',
                  'CTC': 'L',
                  'CTA': 'L', 'CTG': 'L', 'CCT': 'P', 'CCC': 'P', 'CCA': 'P', 'CCG': 'P', 'CAT': 'H', 'CAC': 'H',
                  'CAA': 'Q',
                  'CAG': 'Q', 'CGT': 'R', 'CGC': 'R', 'CGA': 'R', 'CGG': 'R', 'ATT': 'I', 'ATC': 'I', 'ATA': 'I',
                  'ATG': 'M',
                  'ACT': 'T', 'ACC': 'T', 'ACA': 'T', 'ACG': 'T', 'AAT': 'N', 'AAC': 'N', 'AAA': 'K', 'AAG': 'K',
                  'AGT': 'S',
                  'AGC': 'S', 'AGA': 'R', 'AGG': 'R', 'GTT': 'V', 'GTC': 'V', 'GTA': 'V', 'GTG': 'V', 'GCT': 'A',
                  'GCC': 'A',
                  'GCA': 'A', 'GCG': 'A', 'GAT': 'D', 'GAC': 'D', 'GAA': 'E', 'GAG': 'E', 'GGT': 'G', 'GGC': 'G',
                  'GGA': 'G',
                  'GGG': 'G'}

    sequence_translated = ''  # Empty string that will contain the translated sequence

    # Splitting the sequence every 3rd character in order to find the codons (upper for generalization)
    for codon in re.findall('...', sequence.upper()):
        if aminoacids[codon] == '*':  # Stops the cycle when a stop codon is reached
            break
        else:
            sequence_translated += aminoacids[codon]  # Adds every aminoacid to the sequence

    return sequence_translated


def split_sequence(sequence):
    """
    This function divides the given sequence in block of 80 characters (followed by \n) in
    conformity with fasta file format.
    :param sequence: sequence to split
    :return splitted_sequence:
    """
    splitted_sequence = "\n".join([(sequence[i:i + 80]) for i in range(0, len(sequence), 80)])
    return splitted_sequence


# print(split_sequence("m}g*LUd0jGACr$6w$vQ??7qCUN,-m]SZ)S{.d&S[W3BRfDG755VxjK;J2u/=(v:-}p6HF)3G96?HP9%47$C8%)t$HPS8L0n%6}jMN7w@7aa)6Q]P_?{J=;(n4DS@j;@b8&LmH_QSNi[u;8*69GL*:x_[e7tTuwR!h[SRabWGyyY*ARR1EXRvjqv3p13]bZev#BvN=ycv5hwZ,(_bGetLe@ev,Y=U8PPPSdNjwFQ5ZJ.{/g;e(X&(QEQ5-2kc_,B.NZGj{5RdX@&:0h4B?.$W(rVhp7*V[N_2CRNF4j+ke#n@:e2E1hSiFNYL2Y}i=Gk#NtEVL&5F5;mjd%nb(S{$B7})vE#t;bf@1%K}1**YA,S5@.#{wMK4M4qVN[KNV9]DPwyvg:PZ[1M=T?V/nAT(A.nC_w1+J=pZm](3pFEU;2ewW8kChq!g(=MVPeSe$tm?$UR?9{{AV_c};Rg-3N{Hkf&9S7XqVSVPbA"))

def find_orf(filename):
    """
    This function given an input file in fasta format, for every sequence, if possible, finds
    ORFs and writes them in a new file filename_orf.fasta.
    After, translates every single ORFs in the respective polypeptides.

    Every ORF and polypeptide is with the original header followed by +number (number of the orf/polypeptide)
    :param filename: fasta file of DNA to find orfs
    :return None: this function acts on file and doesn't return any value
    """

    translated_sequences = open(filename.replace(".fasta", "_translated.fasta"),
                                "w")  # Creates a new file filename_translated.fasta in writing mode that will
    # contain translated polypeptides
    orf_sequences = open(filename.replace(".fasta", "_orf.fasta"),
                         "w")  # Creates a new file filename_orf.fasta in writing mode that will contain found orfs

    with open(filename, 'r') as f:
        data = f.read().split("\n>")

    # Remove empty strings from the list
    sequences = list(filter(None, data))

    for seq in sequences:
        lines = seq.split("\n")
        header = lines.pop(0)  # Saves the header and removes it from the array
        sequence_joined = "".join(lines).replace("\n", "")  # Rebuild the entire sequence

        peptides = list()  # Empty list will contain polypeptides
        orfs = list()  # Empty list will contain both ORFs

        # The re.findall() function uses this regular expression to find all valid ORFs in the sequence
        for orf in re.findall("(?=(ATG(?:\w{3})*?(?:TAA|TAG|TGA)))", sequence_joined):
            orfs.append("".join(orf))  # Finds the ORFS and adds them to the created list
            peptides.append("".join(translation(orf)))  # Find the peptides and adds them to the created list

        # If there are no ORFs in the sequence, the program will skip it
        if len(orfs) == 0 or len(peptides)==0:
            continue

        # Writes the ORFs in the file
        for orf in orfs:
            orf_sequences.write(header + "_ORF_" + str(orfs.index(orf) + 1) + "\n") #Formats the header nicely adding _ORF_number
            orf_sequences.write(split_sequence(orf) + "\n")

        # Writes the peptides in the file
        for peptide in peptides:
            translated_sequences.write(header + "_PEPTIDE_" + str(peptides.index(peptide)+ 1) + "\n") #Formats the header nicely adding _PEPTIDE_number
            translated_sequences.write(split_sequence(peptide)+"\n")

    #Closes both files
    orf_sequences.close()
    translated_sequences.close()