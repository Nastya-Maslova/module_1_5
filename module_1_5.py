immutable_var = 1,2.5,"строка",True
print(immutable_var)
#immutable_var[0] = 2
#print(immutable_var)
#TypeError: 'tuple' object does not support item assignment
# кортеж это неизменяемый тип данных, который нужен для оптимизации производственности и простоты реализации
mutable_list= [1,2,3,4]
mutable_list[0]=2
print(mutable_list)