import pandas
data = pandas.read_csv('weather_data.csv')
data_dict = data.to_dict()
temp_list = data['temp'].to_list()
total = 0
for num in temp_list:
    total += num
avg_temp = total/len(temp_list)
print(avg_temp)
print(data['temp'].mean())

print(data['temp'].max())

print(data.condition)
