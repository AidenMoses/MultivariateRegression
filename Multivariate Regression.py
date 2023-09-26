import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from sklearn import linear_model
import statsmodels.api as sm

# Read the data from a CSV file
df1 = pd.read_csv("Advertising.csv")

# Explore and describe the data
print(df1.describe())
print(df1.head())
print("Data Shape:", df1.shape)

# Visualize data relationships using pair plots
sns.pairplot(df1)

# Linear regression using TV and radio as features
X = df1[['TV', 'radio']].values
y = df1['sales'].values

ols = linear_model.LinearRegression()
model = ols.fit(X, y)
r2 = model.score(X, y)
print("Model Score (R^2):", round(r2, 4))

# Create a meshgrid for 3D visualization
x_pred = np.linspace(0.7, 300, 30)
y_pred = np.linspace(0, 50, 30)
xx_pred, yy_pred = np.meshgrid(x_pred, y_pred)

# Transform data for model testing
model_viz = np.array([xx_pred.flatten(), yy_pred.flatten()]).T
predicted = model.predict(model_viz)

# Reshape predicted values
sales_predicted = predicted.reshape(-1, 1)

# Display the results in a table
print("\033[1m\033[94m{:>12} {:>12} {:>18}\033[0m".format("TV", "radio", "Sales"))
for i in range(10):
    print("{:<12.4f} {:<12.4f} {:<18.4f}".format(x_pred[i], y_pred[i], sales_predicted[i][0]))

# 3D visualization
%matplotlib notebook
fig = plt.figure(figsize=(10, 5))
ax1 = fig.add_subplot(131, projection='3d')
ax2 = fig.add_subplot(132, projection='3d')
ax3 = fig.add_subplot(133, projection='3d')

axes = [ax1, ax2, ax3]

for ax in axes:
    ax.plot(X[:, 0], X[:, 1], y, color='k', zorder=15, linestyle='none', marker='o', alpha=0.5)
    ax.scatter(xx_pred.flatten(), yy_pred.flatten(), predicted, facecolor=(0, 0, 0, 0), s=20, edgecolor='#70b3f0')
    ax.set_xlabel('TV', fontsize=8)
    ax.set_ylabel('radio', fontsize=8)
    ax.set_zlabel('Sales', fontsize=8)
    ax.locator_params(nbins=4, axis='x')
    ax.locator_params(nbins=5, axis='x')

ax1.view_init(elev=28, azim=120)
ax2.view_init(elev=20, azim=150)
ax3.view_init(elev=40, azim=-150)

fig.suptitle('Effect of TV and Radio on Sales\n$R^2 = %.4f$' % r2, fontsize=15)
fig.tight_layout()

plt.show()
