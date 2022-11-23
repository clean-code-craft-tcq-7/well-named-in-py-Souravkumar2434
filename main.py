import check_color_from_pair_number
import check_pair_number_from_colors

if __name__ == '__main__':
  check_color_from_pair_number.test_number_to_pair(4, 'White', 'Brown')
  check_color_from_pair_number.test_number_to_pair(5, 'White', 'Slate')
  check_pair_number_from_colors.test_pair_to_number('Black', 'Orange', 12)
  check_pair_number_from_colors.test_pair_to_number('Violet', 'Slate', 25)
  check_pair_number_from_colors.test_pair_to_number('Red', 'Orange', 7)
  print_reference_module()
  print('Done :)')
