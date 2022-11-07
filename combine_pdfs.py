import sys
from PyPDF2 import PdfFileMerger

def combine(root, pdfs):
    merger = PdfFileMerger()
    
    for file_name in pdfs:
        merger.append(f'{root}/{file_name}')
    
    merger.write(f'{root}.pdf')
    merger.close()
    print('Combine done')

if __name__ == '__main__':
    ch_num = int(sys.argv[1])
    print('ch_num', ch_num)

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
    elif ch_num == 3:
        # chapter 3
        root = '3_Sliding_Window'
        pdfs = [
            '121._best_time_to_buy_and_sell_stock.pdf',
            '3._longest_substring_without_repeating_character.pdf',
            '424._longest_repeating_character_replacement.pdf',
            '567._permutation_in_string.pdf',
            '76._minimum_window_substring.pdf',
        ]
    elif ch_num == 4:
        # chapter 4
        root = '4_Stack'
        pdfs = [
            '20._valid_parentheses.pdf',
            '155._min_stack.pdf',
            '150._evaluate_reverse_polish_notation.pdf',
            '22._generate_parentheses.pdf',
            '739._daily_temperatures.pdf',
            '853._car_fleet.pdf',
        ]
    elif ch_num == 5:
        # chapter 5
        root = '5_Binary_Search'
        pdfs = [
            '704._binary_search.pdf',
            '74._search_a_2d_matrix.pdf',
            '875._koko_eating_bananas.pdf',
            '33._search_in_rotated_sorted_array.pdf',
            '153._find_minimum_in_rotated_sorted_array.pdf',
            '981._time_based_key-value_store.pdf',
        ]
    elif ch_num == 6:
        # chapter 6
        root = '6_Linked_list'
        pdfs = [
            '92._reverse_linked_list_ii.pdf',
            '21._merge_two_sorted_lists.pdf',
            '143._reorder_list.pdf',
            '19._remove_nth_node_from_end_of_list.pdf',
            '138._copy_list_with_random_pointer.pdf',
            '2._add_two_numbers.pdf',
            '141._linked_list_cycle.pdf',
            '287._find_the_duplicate_number.pdf',
            '146._lru_cache.pdf'
        ]


    combine(root, pdfs)
