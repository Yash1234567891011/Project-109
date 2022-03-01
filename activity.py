import pandas as pd
import statistics
import plotly.figure_factory as ff
import plotly.graph_objects as go 
df=pd.read_csv("data.csv")
math_list=df["math score"].to_list()
math_mean=statistics.mean(math_list)
math_median=statistics.median(math_list)
math_mode=statistics.mode(math_list)
print("mean,median,mode of math is {},{},{} ".format(math_mean,math_median,math_mode))
math_std_dev=statistics.stdev(math_list)
math_first_std_start,math_first_std_end=math_mean-math_std_dev,math_mean+math_std_dev
math_second_std_start,math_second_std_end=math_mean-(2*math_std_dev),math_mean+(2*math_std_dev)
math_third_std_start,math_third_std_end=math_mean-(3*math_std_dev),math_mean+(3*math_std_dev)

math_list_data_within_first_std=[result for result in math_list if result > math_first_std_start and result<math_first_std_end]
math_list_data_within_second_std=[result for result in math_list if result > math_second_std_start and result<math_second_std_end]
math_list_data_within_third_std=[result for result in math_list if result > math_third_std_start and result<math_third_std_end]

print("{}% of data for math lies within 1 std dev".format(len(math_list_data_within_first_std)*100.0/len(math_list)))
print("{}% of data for math lies within 2 std dev".format(len(math_list_data_within_second_std)*100.0/len(math_list)))
print("{}% of data for math lies within 3 std dev".format(len(math_list_data_within_third_std)*100.0/len(math_list)))

fig=ff.create_distplot([math_list],["Math"],show_hist=False)
fig.add_trace(go.Scatter(x=[math_mean,math_mean],y=[0,0.17],mode="lines",name="mean"))
fig.add_trace(go.Scatter(x=[math_first_std_start,math_first_std_start],y=[0,0.17],mode="lines",name="std1"))
fig.add_trace(go.Scatter(x=[math_first_std_end,math_first_std_end],y=[0,0.17],mode="lines",name="std1"))
fig.add_trace(go.Scatter(x=[math_second_std_start,math_second_std_start],y=[0,0.17],mode="lines",name="std2"))
fig.add_trace(go.Scatter(x=[math_second_std_end,math_second_std_end],y=[0,0.17],mode="lines",name="std2"))
fig.add_trace(go.Scatter(x=[math_third_std_start,math_third_std_start],y=[0,0.17],mode="lines",name="std3"))
fig.add_trace(go.Scatter(x=[math_third_std_end,math_third_std_end],y=[0,0.17],mode="lines",name="std3"))
fig.show()