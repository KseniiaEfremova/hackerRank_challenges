def calculate_minimum_classes(number_students):
    max_class_size = 30
    min_classes = 2

    number_required_classes = number_students // max_class_size
    if number_students % max_class_size != 0:
        number_required_classes += 1
    number_required_classes = max(number_required_classes, min_classes)
    print('Proposed Allocation:', number_required_classes, 'classes')

    allocation = {}
    size = number_students // number_required_classes
    rest = number_students % number_required_classes
    for i in range(1, number_required_classes + 1):
        class_size = size
        if i <= rest:
            class_size += 1
        allocation['Class ' + str(i)] = class_size
    print(allocation)


def calculate_minimum_classes_2(number_students):
    max_class_size = 30
    min_classes = 2
    number_required_classes = number_students // max_class_size
    if number_students % max_class_size != 0:
        number_required_classes += 1
    number_required_classes = max(number_required_classes, min_classes)
    class_size = number_students // number_required_classes
    rest = number_students % number_required_classes
    allocation = {}
    for numb_class in range(1, number_required_classes+1):
        if rest == 0:
            allocation[f"Class {numb_class}"] = class_size
        else:
            allocation[f"Class {numb_class}"] = class_size + 1
            rest -= 1
    print(allocation)

