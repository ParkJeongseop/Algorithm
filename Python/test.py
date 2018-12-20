# input_seq = input("input seq: ")
# complement = {'A' : 'T', 'T' : 'A', 'G' : 'C', 'C':'G'}
#
# complement_base_list = []
# for base in input_seq:
#     complement_base = complement[base]
#     complement_base_list.append(complement_base)
#
# complement_seq = ''.join(complement_base_list)
# print(complement_seq)

nucl_type = input("Input nucleic acid type: ")

if nucl_type == 'RNA':
    start_codon = 'AUG'
elif nucl_type == 'DNA':
    start_codon = 'ATG'
else:
    print('Error')

print(start_codon)