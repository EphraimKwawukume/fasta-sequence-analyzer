import sys

if len(sys.argv) < 2:
    print("Usage: python fasta_analyzer.py <input.fasta> [output.tsv]")
    sys.exit(1)

input_fasta = sys.argv[1]

if len(sys.argv) >= 3:
    output_tsv = sys.argv[2]
else:
    output_tsv = "summary.tsv"



def parse_fasta (fasta):
    header = "unknown_header" 
    #This is incase a FASTA file ever starts with raw DNA before the first > line, it wont crash and give an error
    sequences = {}
    nuc = ""
    with open (fasta, encoding='utf-8') as file:
        for line in file:
            clean_line = line.rstrip("\n")
            if clean_line == '':
                continue
            #if a line is met which does does not have any characters the interpreter skips/or does not does check the rest of the conditions on this empty line and goes to the next line
            #its nothing crazy just prevents waste of time in the case of a file carrying multiple empty lines ,the compiler does not waste time on them 
            if clean_line.startswith('>'):
                header = clean_line.lstrip('>')
                nuc = ''
                sequences[header] = nuc
                #so if a >header does not have any sequnce in the fasta file it can be recorded in the dictionary too
            else:
                nuc = nuc + clean_line.upper()
                sequences[header] = nuc
    return sequences

def calc_gc_percent(seq):
    gc_count = seq.count('G') + seq.count('C')
    if len(seq) == 0:
      return 0.0 
    #this is so that we dont get an error trying to divide by zero
    gc_percent = (gc_count/len(seq))* 100
    return round (gc_percent, 2)

def count_stop_codons(seq):
    num = 0
    stop_codons =["TAA", "TAG", "TGA"]
    for i in range(0,len(seq),3):
        codon = seq[i:i+3]
        if  codon in stop_codons:
            num += 1
    return num

def write_summary_report(output_tsv, parsed):
    with open(output_tsv,'w', encoding='utf-8') as output:
        output.write("Sequence_ID\tLength_bp\tGC_Percent\tA_Count\tT_Count\tG_Count\tC_Count\tStop_Codons\n")
        for header,seq in parsed.items():
            length = len(seq)
            GC_percent = calc_gc_percent(seq)
            A_count = seq.count('A')
            G_count = seq.count('G')
            C_count = seq.count('C')
            T_count = seq.count('T')
            stops = count_stop_codons(seq)
            row = f"{header}\t{length}\t{GC_percent}\t{A_count}\t{T_count}\t{G_count}\t{C_count}\t{stops}\n"
            output.write(row)

parsed = parse_fasta(input_fasta)
write_summary_report(output_tsv, parsed)
print(f"Done! Analyzed {len(parsed)} sequences from {input_fasta} -> {output_tsv}")