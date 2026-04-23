import pandas as pd
import numpy as np

# Patient Data
patients = pd.DataFrame({
    "Patient_ID": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    "Name": ["Amit", "Neha", "Raj", "Simran", "Karan", "Pooja", "Arjun", "Meena", "Rohit", "Anjali"],
    "Age": [25, 40, 35, 60, 28, 50, 45, 30, 55, 38],
    "Gender": ["M", "F", "M", "F", "M", "F", "M", "F", "M", "F"],
    "Dept_ID": [1, 2, 1, 3, 2, 1, 3, 2, 1, 3],
    "Treatment_Cost": [20000, 30000, None, 50000, 15000, None, 45000, 25000, 40000, None],
    "Days_Admitted": [3, 5, 4, 7, 2, 6, 8, 3, 5, 4]
})

# Department Data
departments = pd.DataFrame({
    "Dept_ID": [1, 2, 3],
    "Dept_Name": ["General", "Cardiology", "Orthopedic"]
})

# Doctors Data
doctors = pd.DataFrame({
    "Dept_ID": [1, 2, 3],
    "Doctor_Name": ["Dr. Sharma", "Dr. Mehta", "Dr. Singh"]
})

patients["Treatment_Cost"] = patients["Treatment_Cost"].fillna(patients["Treatment_Cost"].mean())
patients["Cost_per_day"] = patients["Treatment_Cost"] / patients["Days_Admitted"]

# print(patients)

patients_department = pd.merge(patients,departments,on="Dept_ID",how="inner")
# print(patients_department)

final_data = pd.merge(patients_department , doctors , on="Dept_ID" , how="inner")

print(final_data)

final_data["Patient_Category"] = np.where(final_data["Treatment_Cost"] >= 40000 , "High Cost",
                                          np.where((final_data["Treatment_Cost"] >=20000) & 
                                                   (final_data["Treatment_Cost"] < 40000) ,"Medium Cost" , "Low Cost"))


# print(final_data)

# group by 

# Find:

# Average treatment cost per department
# Total patients per department
# Maximum days admitted per department

average_treatment = final_data.groupby("Dept_Name")["Treatment_Cost"].sum()
print(average_treatment)

patient_per_department = final_data.groupby("Dept_Name")["Patient_ID"].count()

print(patient_per_department)

maxium_days = final_data.groupby("Dept_Name")["Days_Admitted"].max()

high_treatment = final_data.loc[final_data["Treatment_Cost"].idxmax()]
# print(high_treatment)

longest_day = final_data.loc[final_data["Days_Admitted"].idxmax()]

sorting_treatment_cost = final_data.sort_values(by="Treatment_Cost" , ascending=False)
sorting_days_admitted = final_data.sort_values(by="Days_Admitted" , ascending=False)

filter_patient = final_data.loc[(final_data["Treatment_Cost"] > 30000) & (final_data["Days_Admitted"]>5)]

departments_average = final_data.groupby("Dept_Name")["Treatment_Cost"].mean().reset_index(name="Average_treatment_department")

dept_avg = pd.DataFrame(departments_average)

final = pd.merge(final_data , dept_avg , on = "Dept_Name" , how = "inner")

show_patient = final.loc[final["Treatment_Cost"] > final["Average_treatment_department"]]

print(show_patient)