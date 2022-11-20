import check_color_from_pair_number
import check_pair_number_from_colors
MAJOR_COLORS = ['White', 'Red', 'Black', 'Yellow', 'Violet']
MINOR_COLORS = ["Blue", "Orange", "Green", "Brown", "Slate"]


def color_pair_to_string(major_color, minor_color):
  return f'{major_color} {minor_color}'

def print_reference_module():
    count = 1
    for i in range(1, len(MAJOR_COLORS) + 1):
        for j in range(len(MINOR_COLORS)):
            print("Pair_no:{}, Major_color {}, Minor_color {}".format(count, MAJOR_COLORS[i - 1], MINOR_COLORS[j]))
            print(count)
            count = count + 1


if __name__ == '__main__':
  check_color_from_pair_number.test_number_to_pair(4, 'White', 'Brown')
  check_color_from_pair_number.test_number_to_pair(5, 'White', 'Slate')
  check_pair_number_from_colors.test_pair_to_number('Black', 'Orange', 12)
  check_pair_number_from_colors.test_pair_to_number('Violet', 'Slate', 25)
  check_pair_number_from_colors.test_pair_to_number('Red', 'Orange', 7)
  print_reference_module()
  print('Done :)')
