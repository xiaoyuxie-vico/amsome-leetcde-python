from PyPDF2 import PdfFileMerger

def combine(root, pdfs):
    merger = PdfFileMerger()
    
    for file_name in pdfs:
        merger.append(f'{root}/{file_name}')
    
    merger.write(f'{root}.pdf')
    merger.close()
    print('Combine done')

if __name__ == '__main__':
    ch_num = 2

    if ch_num == '1':
        # chapter 1
        root = '1_Array_Sorting'
        pdfs = [
            '217._contains_duplicate.pdf',
            '242._valid_anagram.pdf',
            '1._two_sum.pdf',
            '49._group_anagrams.pdf',
            '347._top_k_frequent_elements.pdf',
            '238._product_of_array_except_self.pdf',
            '128._longest_consecutive_sequence.pdf',
        ]
    elif ch_num == 2:
        # chapter 2
        root = '2_Two_Pointers'
        pdfs = [
            '125._valid_palindrome.pdf',
            '167._two_sum_ii_-_input_array_is_sorted.pdf',
            '15._3sum.pdf',
            '11._container_with_most_water.pdf',
            '42._trapping_rain_water.pdf',
        ]

    combine(root, pdfs)
