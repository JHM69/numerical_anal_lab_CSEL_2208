def u_cal(u, n):
	temp = u
	for i in range(1, n):
		temp = temp * (u - i)
	return temp

def fact(n):
	if n == 1: return 1
	return n*fact(n-1)

n = 5
x = [ 45, 50, 55, 60, 65]
	
y = [[0 for _ in range(n)] for __ in range(n)]
y[0][0] = 0.7071
y[1][0] = 0.7660
y[2][0] = 0.8192
y[3][0] = 0.8660
y[4][0] = 0.8268


z = y 


# Calculating the Foroward difference table
for i in range(1, n):
    for j in range(n - i):
        y[j][i] = y[j + 1][i - 1] - y[j][i - 1]


# Calculating the backward difference table
for i in range(1, n):
    for j in range(n - 1, i - 1, -1):
        z[j][i] = z[j][i - 1] - z[j - 1][i - 1]

# Displaying the Foroward difference table
for i in range(n):
	print(x[i], end = "\t")
	for j in range(n - i):
		print(y[i][j], end = "\t")
	print("")

# Displaying the backward difference table
for i in range(n):
    for j in range(i + 1):
        print(z[i][j], end="\t")
    print()

value = int(input())

sum1 = y[0][0]
sum2 = z[n-1][0]
u1 = (value - x[0]) / (x[1] - x[0])
u2 = (value - x[n - 1]) / (x[1] - x[0])
for i in range(1,n):
	sum1 = sum1 + (u_cal(u1, i) * y[0][i]) / fact(i)
	sum2 = ( sum2 + (u_cal(u2, i) * z[n - 1][i]) / fact(i))

print("\nValue at ", value, "\nForoward Interpolation: ", round(sum1, 6), "\nBackward Interpolation: ", round(sum2, 6))

