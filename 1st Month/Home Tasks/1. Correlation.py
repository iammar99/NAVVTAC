import numpy as np


# ------------------------------------
#   Student data
# ------------------------------------

student_data = {
    "study_hours": [4,6,5,7,8,3,6,7,5,4],
    "attendence": [80,90,85,95,92,75,88,94,87,78],
    "assignment_score": [70,85,78,90,92,65,83,89,80,72],
    "mid_score": [68,82,75,88,90,60,80,85,77,70],
    "final_score": [72,88,80,92,94,63,85,90,82,74],
    "gpa": [2.8,3.5,3.2,3.8,3.9,2.5,3.4,3.7,3.3,2.9]
}

print(np.round(np.corrcoef(list(student_data.values())), 2))

# ------------------------------------
#   Buisness data
# ------------------------------------

buisness_data = {
    "advertising_budget": [20,25,30,35,40,15,28,33,22,18],
    "sales_calls": [50,60,65,70,75,45,62,68,55,48],
    "website_visits": [200, 250, 270, 300, 320,180,260,290,230,210],
    "customer_reviews": [3.8,4.2,4.0,4.5,4.6,3.5,4.1,4.4,3.9,3.7],
    "monthly_sales": [2000, 2500,2700, 3000, 3200, 1800, 2600,2900,2300, 2100],
    "profit": [500,700,750,900, 950,400,720,880,650,550]
}

np.round(np.corrcoef(list(buisness_data.values())), 2)

# ------------------------------------
#   Health data
# ------------------------------------

health_data = {
    "age": [25,30,35,40,28,32,45,38,29,50],
    "weight": [65,70,75,80,68,72,85,78,69,90],
    "bmi": [22,24,26,28,23,25,30,27,24,31],
    "systolic_bp": [110,120,130,140,115,125,150,135,118,155],
    "cholesterol": [180,190, 200, 220, 185,195,230,210,188, 240],
    "glucose": [85,90,95,105,88,92,115,100,89,120]
}

np.round(np.corrcoef(list(health_data.values())), 2)

# ------------------------------------
#   Employee data
# ------------------------------------

employee_data = {
    "experince_years": [1,3,5,7,2,4,6,8,3,5],
    "training_hours": [20,30,40,50,25,35,45,552,28,38],
    "performace_score": [60,70,80,90,65,75,85,95,68,78],
    "projects_completed": [2,4,6,8,3,5,7,9,4,6],
    "salary": [30000,40000,50000,60000,35000,45000,55000,65000,38000,48000],
    "promotion_score": [50,65,75,85,55,70,80,90,60,72]
}

np.round(np.corrcoef(list(employee_data.values())), 2)

# ------------------------------------
#   Industry data
# ------------------------------------

industry_data = {
    "machine_hours": [6,8,7,9,10,5,8,9,7,6],
    "energy_consumption": [200,250,230,280,300,180,260,290,220,210],
    "output_limits": [500,650,600,700,750,480,670,720,610,530],
    "defect_rate": [3.5,3.0,3.2,2.8,2.5,3.8,2.9,2.6,3.1,3.4],
    "maintenance_cost": [1000,1200,1100,1300,1400,900,1250,1350,1150,1050],
    "efficiency": [85,88,87,90,92,80,89,91,86,84]
}

np.round(np.corrcoef(list(industry_data.values())), 2)

# ------------------------------------
#   IT data
# ------------------------------------

it_data = {
    "cpu_usage": [50,60,55,70,75,45,65,72,58,52],
    "memory_usage": [60,65,62,75,80,55,68,78,64,59],
    "disk_io": [100,120,110,140,150,90,130,145,115,105],
    "response_time": [200,250,220,300,320,180,270,310,230,210],
    "network_latentency": [20,25,22,30,35,18,27,32,23,21],
    "error_rate": [1.5,1.8,1.6,2.0,2.2,1.3,1.9,2.1,1.7,1.4]
}

np.round(np.corrcoef(list(it_data.values())), 2)

# ------------------------------------
#   MT CARS
# ------------------------------------

# The mtcars dataset is not available by default in Python.
# You can load it using seaborn or statsmodels library if needed.
# For example:
# import seaborn as sns
# mtcars = sns.load_dataset('mpg').dropna()  # mpg dataset is similar but not the same
# np.round(mtcars.corr(), 2)
