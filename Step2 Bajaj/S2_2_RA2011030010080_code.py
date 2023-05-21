import pandas as pd
import matplotlib.pyplot as plt

# Assuming you have a DataFrame named 'appointment' with a 'gender' column

# Count the number of appointments by gender
appointment_counts = appointment['gender'].value_counts()

# Create a pie chart
plt.pie(appointment_counts, labels=appointment_counts.index, autopct='%1.1f%%')
plt.title('Appointments by Gender')


plt.show()
