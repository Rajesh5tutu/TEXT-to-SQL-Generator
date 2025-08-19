import sqlite3

# Connect to SQLite
connection = sqlite3.connect("student.db")

# Create a cursor object
cursor = connection.cursor()

# Create the STUDENT table
table_info = """
CREATE TABLE IF NOT EXISTS STUDENT (
    NAME TEXT,
    CLASS TEXT,
    SECTION TEXT,
    MARKS INTEGER
);
"""
cursor.execute(table_info)

# Insert records
students = [
    ('Krish', 'Data Science', 'A', 90),
    ('Sudhanshu', 'Data Science', 'B', 100),
    ('Darius', 'Data Science', 'A', 86),
    ('Vikash', 'DEVOPS', 'A', 50),
    ('Dipesh', 'DEVOPS', 'A', 35),
    ('Riya', 'AI/ML', 'B', 78),
    ('Kunal', 'Cloud Computing', 'C', 65),
    ('Sneha', 'Data Science', 'A', 92),
    ('Aditya', 'DEVOPS', 'B', 55),
    ('Meera', 'AI/ML', 'A', 88),
    ('Tanvi', 'Cloud Computing', 'B', 73),
    ('Yash', 'Data Science', 'C', 60),
    ('Kabir', 'DEVOPS', 'A', 47),
    ('Neha', 'AI/ML', 'B', 81),
    ('Aarav', 'Cloud Computing', 'A', 90),
    ('Ishita', 'Data Science', 'B', 84),
    ('Rahul', 'DEVOPS', 'C', 42),
    ('Simran', 'AI/ML', 'A', 95),
    ('Arjun', 'Cloud Computing', 'B', 70),
    ('Priya', 'Data Science', 'A', 89),
    ('Nikhil', 'DEVOPS', 'B', 53),
    ('Ananya', 'AI/ML', 'C', 66),
    ('Dev', 'Cloud Computing', 'A', 91),
    ('Sana', 'Data Science', 'B', 76),
    ('Manav', 'DEVOPS', 'A', 49),
    ('Tanya', 'AI/ML', 'B', 80),
    ('Harsh', 'Cloud Computing', 'C', 61),
    ('Pooja', 'Data Science', 'A', 93),
    ('Shruti', 'DEVOPS', 'B', 58),
    ('Kritika', 'AI/ML', 'C', 67),
    ('Om', 'Cloud Computing', 'A', 87),
    ('Naina', 'Data Science', 'B', 74),
    ('Siddharth', 'DEVOPS', 'C', 45),
    ('Aisha', 'AI/ML', 'A', 96),
    ('Rohan', 'Cloud Computing', 'B', 72),
    ('Ishaan', 'Data Science', 'C', 63),
    ('Divya', 'DEVOPS', 'A', 52),
    ('Aman', 'AI/ML', 'B', 79),
    ('Bhavya', 'Cloud Computing', 'C', 64),
    ('Rehan', 'Data Science', 'A', 91),
    ('Jiya', 'DEVOPS', 'B', 56),
    ('Veer', 'AI/ML', 'C', 68),
    ('Lavanya', 'Cloud Computing', 'A', 89),
    ('Aryan', 'Data Science', 'B', 75),
    ('Mira', 'DEVOPS', 'C', 43),
    ('Parth', 'AI/ML', 'A', 94),
    ('Tara', 'Cloud Computing', 'B', 71),
    ('Vivaan', 'Data Science', 'C', 62),
    ('Niharika', 'DEVOPS', 'A', 48),
    ('Zoya', 'AI/ML', 'B', 77),
    ('Shaurya', 'Cloud Computing', 'C', 59)
]

cursor.executemany("INSERT INTO STUDENT VALUES (?, ?, ?, ?)", students)

# Display all records
print("The inserted records are:")
for row in cursor.execute("SELECT * FROM STUDENT"):
    print(row)

# Commit and close
connection.commit()
connection.close()