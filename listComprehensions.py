
x = int(input())
y = int(input())
z = int(input())
n = int(input())

x_list = list(range(x+1))
y_list = list(range(y+1))   
z_list = list(range(z+1))

result_list = list()
for i in x_list:
    for j in y_list:
        for k in z_list:
            if (i+j+k) != n:
                result_list.append([i,j,k])

print(result_list)