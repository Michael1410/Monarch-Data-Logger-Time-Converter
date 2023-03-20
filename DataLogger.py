
class DataLogger:

    list_of_dict = []
    time_list = []
    day_list = []
    afternoon_list = []
    off_list = []
    on_list = []
    time_list_minutes = []

    def __int__(self, list_of_dict):
        self.list_of_dict = list_of_dict

    @classmethod
    # Iterate through csv data and find all elements under Time key
    # remove dd/mm/yyyy and store time, and input in new_list
    def convert_csv(cls, list_of_dict, time_list):
        for val in list_of_dict:
            k = (val['Time'])
            zet = (k.split(' '))
            p = (val['Ext. Input 1 digital'])
            # print(p)
            time_list.append(zet[1].split(':') + [p])

    @classmethod
    def convert_time_to_int(cls, time_list):
        for i in range(len(time_list) - 1):
            # print(time_list[i])
            time_list[i][0] = int(time_list[i][0])
            time_list[i][1] = int(time_list[i][1])

    @classmethod
    def split_mornings_afternoons(cls, time_list, day_list, afternoon_list):
        for t in range(len(time_list) - 1):
            if time_list[t][0] < 15 and time_list[t][0] > 6:
                day_list.append(time_list[t])
            if time_list[t][0] > 15 or time_list[t][0] < 6:
                afternoon_list.append(time_list[t])

    @classmethod
    # add all off signal times to off_list and all on signal times to on_list
    def seperate_by_states(cls, unsorted_states, off_list, on_list):
        for i in range(len(unsorted_states)-1):
            if unsorted_states[i][2] == '1oFF' and unsorted_states[i - 1][2] != '1off':
                off_list.append(unsorted_states[i][0] * 60 + unsorted_states[i][1])
            elif unsorted_states[i][2] == '1 on' and unsorted_states[i - 1][2] != '1 on':
                on_list.append(unsorted_states[i][0] * 60 + unsorted_states[i][1])

    @classmethod
    def convert_to_minutes(cls, time_list_minutes, lis):
        for q in range(len(lis) - 1):
            time_list_minutes.append(lis[q][0] * 60 + lis[q][1])

    # Find the difference between on and off times
    @classmethod
    def find_difference(cls, on_li, off_li):
        total_time_diff = 0
        res = 0
        for z in range(len(on_li) - 1):
            res = on_li[z] - off_li[z]
            total_time_diff = total_time_diff + res
            # print(total_time_diff)
        return total_time_diff

    @classmethod
    def find_total_run_time(cls, time_list):
        # Find total run time
        total = 0
        for s in range(len(time_list) - 1):
            # print(comp_list[s])
            old_time = time_list[s]
            new_time = time_list[s + 1]

            if new_time < old_time:
                new_time = new_time + 24 * 60
            res = new_time - old_time
            # print(res)
            total = total + res
        return total

    @classmethod
    def calculate_downtime(cls, shift_id, total_run_time, total_time_diff):
        if shift_id == 'Days':
            down_time = total_run_time - total_time_diff - 25
        elif shift_id == 'Afternoons':
            down_time = total_run_time * total_time_diff - 15
        return down_time




