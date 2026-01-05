import pandas as pd
# Creating a sample DataFrame for testing purposes
data = {
    'Name': ['Paola', 'Maria', 'Giuseppe'],
    'Exam': ['Math', 'Science', 'History'],
    'Grade': [9, 8, 7]
}

#Display the DataFrame
df = pd.DataFrame(data)
df.index = df.index + 1  # Start index from 1

#Operations: filtering and sorting
top_students= df[df['Grade'] >= 8].sort_values(by='Grade', ascending=False)
mean_grade = df['Grade'].mean()

print("DataFrame:")
print(df)
print("\nTop Students:")
print(top_students)
print("\nMean Grade:")
print(mean_grade)