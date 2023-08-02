from sequence_utility import split_sequence

def fastq_to_fasta(filename):
    """This function takes a fastq file and removes unuseful strings and writes the header and sequences in the FASTA format

    :param filename: fastq file """

    fastq_sequence = open(filename,"r").readlines() #Gets all lines from the fastq file
    fasta_sequence = open(filename.replace("fastq","fasta"),"w") #Creates a new (empty) fasta file

    for index,line in enumerate(fastq_sequence):
        if line.startswith("@"): #Finds all the headers
            # Finds the sequence line and using the split_sequence method writes it in the fasta file
            fasta_sequence.write(line.replace("@", ">"))
            #Modify the header in order to contain the ">" start character and writes it in the fasta file
            fasta_sequence.write(split_sequence(fastq_sequence[index+3]))

    #Close both files
    fasta_sequence.close()
    fasta_sequence.close()

