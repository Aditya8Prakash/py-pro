import pandas as pd
import plotly.figure_factory as ff
import statistics

array = ["math score","reading score","writing score"]

for i in array :

    print("for",i,":")

    print("\n")

    df = pd.read_csv('data.csv')
    score = df[i].to_list()

    mean = sum(score)/len(score)
    median = statistics.median(score)
    mode = statistics.mode(score)

    stanDev = statistics.stdev(score,mean)

    print("    mean = ",mean)
    print("    median = ",median)
    print("    mode = ",mode)
    print("    standeredDevation = ",stanDev)

    print("\n")

    f_std_start,f_std_end = mean-stanDev,mean+stanDev
    data_within_one_std = [result for result in score if result > f_std_start and result < f_std_end]

    s_std_start,s_std_end = mean-(2*stanDev),mean+(2*stanDev)
    data_within_two_std = [result for result in score if result > s_std_start and result < s_std_end]

    t_std_start,t_std_end = mean-(3*stanDev),mean+(3*stanDev)
    data_within_three_std = [result for result in score if result > t_std_start and result < t_std_end]

    print("     {}% of data lies within 1 standered dev".format(len(data_within_one_std)*100/len(score)))
    print("     {}% of data lies within 2 standered dev".format(len(data_within_two_std)*100/len(score)))
    print("     {}% of data lies within 3 standered dev".format(len(data_within_three_std)*100/len(score)))

    print("\n\n")

    fig = ff.create_distplot([score],["Result"])
    fig.show()