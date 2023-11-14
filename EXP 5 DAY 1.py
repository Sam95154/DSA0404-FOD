import numpy as np
student_scores = np.array([[76,65,83,59],[89,75,82,90],[35,60,45,50],[95,84,93,87]])
average_scores = np.mean(student_scores,axis=0 )
print("Average Scores for each subject :",average_scores)
index_avg = np.argmax(average_scores)
subjects = ["Maths","Science","English","History"]
subject_high_avg = subjects[index_avg]
print("Subject with Highest Average :",subject_high_avg)
