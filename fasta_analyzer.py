
def parse_fasta (fasta):
    sequences = {}
    nuc = ""
    with open (fasta, encoding='utf-8') as file:
        for line in file:
            if line.strip('\n') == '':
                continue
            if line.startswith('>'):
                header = line.lstrip('>').rstrip('\n')
                nuc = ''
                sequences[header] = nuc
            else:
                nuc = nuc + line.strip('\n').upper()
                sequences[header] = nuc
    return sequences
parsed = parse_fasta("samples.fasta")
print(parsed)

