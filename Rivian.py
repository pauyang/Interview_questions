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


def Count_cost(data):
    cost = {}

    discount = ''
    for each_stream in data:
        total = 0
        for each_time in data[each_stream]:
            for timestamp in each_time.keys():

               # print (each_time[timestamp])
                if each_time[timestamp] <180:
                    each_time[timestamp] = math.ceil(4* float(each_time[timestamp]))

                elif each_time[timestamp] >= 180:
                    each_time[timestamp] = math.ceil(float(each_time[timestamp] / 60.00))* 225
            total += each_time[timestamp]

        data[each_stream].append(total)

        if discount =='':
            max_stream = each_stream
            max = data[each_stream][-1]
            max_stream_num = int(''.join(max_stream.split('-')))

        stream_num = int(''.join(each_stream.split('-')))
        if data[each_stream][-1] >= max:
            if stream_num >= max_stream_num:
                discount = each_stream

    for each_time in data[discount]:
      if type(each_time) is dict:
          for timestamp in each_time.keys():
              each_time[timestamp]= each_time[timestamp]//2
      else:
          data[discount][-1] = each_time//2

    print ("50% discount awarded to stream: {}\n".format(discount))
    print ("Cost is calculated to associated stream:\n{}".format(data))

    return data,discount

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