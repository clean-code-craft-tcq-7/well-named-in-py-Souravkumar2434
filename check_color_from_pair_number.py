import print_reference_module as pm
def get_color_from_pair_number(pair_number):
    zero_based_pair_number = pair_number - 1
    major_index = zero_based_pair_number // len(pm.MINOR_COLORS)
    if major_index >= len(pm.MAJOR_COLORS):
        raise Exception('Major index out of range')
    minor_index = zero_based_pair_number % len(pm.MINOR_COLORS)
    if minor_index >= len(pm.MINOR_COLORS):
        raise Exception('Minor index out of range')
    return pm.MAJOR_COLORS[major_index], pm.MINOR_COLORS[minor_index]


def test_number_to_pair(pair_number,
                        expected_major_color, expected_minor_color):
    major_color, minor_color = get_color_from_pair_number(pair_number)
    assert(major_color == expected_major_color)
    assert(minor_color == expected_minor_color)
