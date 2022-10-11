from PyPDF2 import PdfFileMerger

def combine(root, pdfs):
    merger = PdfFileMerger()
    
    for file_name in pdfs:
        merger.append(f'{root}/{file_name}')
    
    merger.write(f'{root}.pdf')
    merger.close()
    print('Combine done')

if __name__ == '__main__':
    root = '1_Array_Sorting'
    pdfs = [
        '217._contains_duplicate.pdf',
        '242._valid_anagram.pdf',
        '1._two_sum.pdf',
        '49._group_anagrams.pdf',
        '347._top_k_frequent_elements.pdf',
        '238._product_of_array_except_self.pdf',
        '242._valid_anagram.pdf',
        '128._longest_consecutive_sequence.pdf',
    ]

    combine(root, pdfs)
