from datetime import datetime
import math


def Check_Stream_Time(S):
    dict = {}

    origin = datetime.strptime("00:00:00", "%H:%M:%S")

    for st in S:
        dict2 = {}
        P = st.split(",")
        delta = (datetime.strptime(P[0], "%H:%M:%S") - origin).seconds
        if P[1] in dict:
            dict2[P[0]]=delta
            dict[P[1]].append(dict2)
        else:
            dict2[P[0]]=delta
            dict[P[1]]=[dict2]
    print("Place everything in a dictionary:\n{}\n".format(dict))
    return dict



def print_out(data,discount):
    print ("\nDetail BreakDown")
    total = 0
    for each_stream in data:
        for each_time in data[each_stream]:
            if type(each_time) is dict:
                for timestamp in each_time.keys():
                    if discount == each_stream:
                        print("{} = {} cents \t(discounted)".format(timestamp, each_time[timestamp]))
                    else:
                        print ("{} = {} cents".format(timestamp,each_time[timestamp]))

            else:
                total += data[each_stream][-1]

    print ("Total = {}".format(total))


S = ["00:01:25,123-45-6789", "00:03:01,987-65-4321", "00:03:00,123-45-6789"]

def main():
    data = Check_Stream_Time(S)
    cost,discount = Count_cost(data)
    print_out(cost,discount)

if __name__ == "__main__":
    main()