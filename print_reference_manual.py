MAJOR_COLORS = ['White', 'Red', 'Black', 'Yellow', 'Violet']
MINOR_COLORS = ["Blue", "Orange", "Green", "Brown", "Slate"]


def color_pair_to_string(major_color, minor_color):
  return f'{major_color} {minor_color}'

def print_reference_module():
    count = 1
    print("Refrence Module:-")
    for i in MAJOR_COLORS:
        for j in MINOR_COLORS:
            print("Pair_no: {}, Major_color: {}, Minor_color: {}".format(count, i, j))
            count = count + 1
