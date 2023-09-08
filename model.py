# Import necessary libraries
import pandas as pd  # For data handling
import pickle       # For saving the trained model
from sklearn.model_selection import train_test_split  # For splitting data
from sklearn.linear_model import LinearRegression #For Fitting the model

# Load the dataset from a CSV file
df = pd.read_csv('Ecommerce Customers.csv')

# Define the features (input) and label (output) columns
features = ['Avg. Session Length', 'Time on App', 'Time on Website', 
'Length of Membership']
label = "Yearly Amount Spent"

# Extract input features (X) and output labels (y)
X = df[features]
y = df[label]

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.4,
 random_state=42)

# Create a Linear Regression model
Regression_model = LinearRegression()

# Train the model on the training data
Regression_model.fit(X_train, y_train)

# Make predictions using the trained model
predictions = Regression_model.predict(X_test)

# Print the model's predictions
print(predictions)

# Save the trained model to a file named "model.pkl"
pickle.dump(Regression_model, open("model.pkl", "wb"))