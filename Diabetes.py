Diabetes Dataset Analysis example

# Import pandas library
import pandas as pd
filename = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0101EN-SkillsNetwork/labs/Module%205/data/diabetes.csv"

async def download(url, filename):
    response = await pyfetch(url)
    if response.status == 200:
        with open(filename, "wb") as f:
            f.write(await response.bytes())

await download(filename, "diabetes.csv")
df = pd.read_csv("diabetes.csv")

# show the first 5 rows using dataframe.head() method
print("The first 5 rows of the dataframe") 
df.head(5)
df.shape
df.info()
df.describe()


Identify and handle missing values

We use Python's built-in functions to identify these missing values. There are two methods to detect missing data:

.isnull()

.notnull()


missing_data = df.isnull()
missing_data.head(5)

"True" stands for missing value, while "False" stands for not missing value.

Count missing values in each column
for column in missing_data.columns.values.tolist():
    print(column)
    print (missing_data[column].value_counts())
    print("")  


Correct data format

Check all data is in the correct format (int, float, text or other).

In Pandas, we use

.dtype() to check the data type

.astype() to change the data type

Numerical variables should have type 'float' or 'int'.


df.dtypes

Visualization

# import libraries
import matplotlib.pyplot as plt
import seaborn as sns
labels= 'Diabetic','Not Diabetic'
plt.pie(df['Outcome'].value_counts(),labels=labels,autopct='%0.02f%%')
plt.legend()
plt.show()
