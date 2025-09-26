import matplotlib.pyplot as plt

days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
temperatures = [22, 24, 19, 23, 25, 28, 26]  

plt.plot(days, temperatures, marker='o', linestyle='-', color='b')

plt.xlabel("Days of the Week")
plt.ylabel("Temperature (°C)")
plt.title("Temperature Variation Over a Week")

plt.grid(True)
plt.show()
