import pandas as pd

port numpy as np

data-I

'student ID': range (1, 21), Course' np.random.choice (['Math', 'Science', 'History'], size-20), 'Score': np.random.randint (60, 100, size-20).

Hours Studied: np.random. uniform (5, 30, size=20)

student data pd.DataFrame (data)
correlation_per_course = student_data.groupby("Course') [[ Hours studied', 'score']].corr().iloc[0::2, -1).reset_index (level-1, drop true0
print("Correlation coefficient between Hours Studied and Score for each course:")

print (correlation_per_course)

strongest_corr_course = correlation_per_course.idxmax()

weakest_corr_course = correlation_per_course.idmin()
print("\ncourse with the strongest correlation:", strongest corr_course)
print("Course with the weakest correlation:", weakest_corr_course)

course_aggregate = student_data.groupby('course')[['Score', 'Hours Studied'11.mean () 
print (Aggregated DataFrame with average score and average hours studied for each course:")

print (course aggregate)
