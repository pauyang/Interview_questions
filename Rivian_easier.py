from datetime import datetime
import math
def Check_Stream_Time (S):

    dict={}
    origin = datetime.strptime("00:00:00", "%H:%M:%S")

    for st in S:
        P= st.split(",")
        delta = (datetime.strptime(P[0],"%H:%M:%S") - origin).seconds
        if P[1] in dict:
            dict[P[1]].append(delta)
        else:
            dict[P[1]]=[delta]
    print(dict)
    return dict

def Count_cost(Total_Time):
    cost ={}
    # print (list(Total_Time.keys())[0])

    discount = ''

    for each_stream in Total_Time:
        for each_time in Total_Time[each_stream]:
            if each_time < 180:
                if each_stream in cost:
                    cost[each_stream].append(4 * each_time)
                else:
                    cost[each_stream] =[4 * each_time]
            elif each_time >=180:
                if each_stream in cost:
                    cost[each_stream].append(math.ceil(float(each_time) / 60.00) * 225)
                else:
                    cost[each_stream] = [math.ceil(float(each_time) / 60.00) * 225]

        if discount =='':
            max_stream = each_stream
            max = sum(cost[each_stream])
            max_stream_num = int(''.join(max_stream.split('-')))

        stream_num = int(''.join(each_stream.split('-')))
        if sum(cost[each_stream]) >=max:
            if stream_num >= max_stream_num:
                 discount = each_stream

    new_price = []
    for each_cost in cost[discount]:
        new_price.append(each_cost//2)
    cost[discount]=new_price
    print ("50% discount on streaming activity: {}".format(discount))
    print(cost)
    return cost








S =["00:01:25,123-45-6789","00:03:01,987-65-4321","00:03:00,123-45-6789"]

time = Check_Stream_Time(S)
cost = Count_cost(time)
