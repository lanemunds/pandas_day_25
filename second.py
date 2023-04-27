import pandas
data = pandas.read_csv('weather_data.csv')
data_dict = data.to_dict()
temp_list = data['temp'].to_list()
total = 0
for num in temp_list:
    total += num
avg_temp = total/len(temp_list)
# print(avg_temp)
# print(data['temp'].mean())

# print(data['temp'].max())

# print(data.condition)

# print(data[data.temp == data['temp'].max()])

monday = data[data.day == 'Monday']

data_dict_1 = {
    'students': ['Amy', 'James', 'Angela'],
    'scores': [76, 56, 65]
}
data_1 = pandas.DataFrame(data_dict_1)
data_1.to_csv('new_data.csv')
