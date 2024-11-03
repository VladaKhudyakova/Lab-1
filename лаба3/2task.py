# TODO Напишите функцию find_common_participants


def find_common_participants(gr1, gr2, splitter=','):
    set_1_gr = set(gr1.split(splitter))
    list_sec_gr = gr2.split(splitter)
    comon_s = set_1_gr.intersection(list_sec_gr)
    comm_l = []
    for a in comon_s:
        comm_l.append(a)
    comm_l.sort()
    return comm_l


participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"
find_common_participants(participants_first_group, participants_second_group)
# TODO Провеьте работу функции с разделителем отличным от запятой
