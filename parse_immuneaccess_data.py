#!/usr/bin/env python3

datafile = "CONTROL_6174_pLN_CD8+.tsv"
output = "control_data.csv"

with open(datafile, 'r') as f, open(output, 'w') as o:
    
    header = f.readline().strip().split('\t')
    v_pos = header.index('v_gene')
    v_fam_pos = header.index('v_family')
    j_pos = header.index('j_gene')
    j_fam_pos = header.index('j_family')
    cdr3_pos = header.index('amino_acid')
    frame_pos = header.index('frame_type')
    
    o.write('V_gene,CDR3_sequence,J_gene,HLA_peptide')
    
    for line in f:
        splitline = line.strip().split('\t')
        if splitline[frame_pos] == 'In':
            
            # if V- or J-gene is unknown, use family instead
            if splitline[v_pos] != 'unresolved':
                v_gene = splitline[v_pos]
            else:
                v_gene = splitline[v_fam_pos]
                
            if splitline[j_pos] != 'unresolved':
                j_gene = splitline[j_pos]
            else:
                j_gene = splitline[j_fam_pos]
                
            o.write('\n'+','.join([v_gene.replace('TCRBV',''), splitline[cdr3_pos], j_gene.replace('TCRBJ','')])+',Control')