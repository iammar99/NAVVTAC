# =========================================
# 🔷 1. Import Libraries
# =========================================
import pandas as pd
import numpy as np

from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier, plot_tree
from sklearn.metrics import confusion_matrix, classification_report, roc_curve, auc
from sklearn.impute import SimpleImputer
import matplotlib.pyplot as plt

# =========================================
# 🔷 2. Load Data
# =========================================
mydata = pd.read_csv("G:\\Courses\\NAVVTAC\\3rd Month\\Practice\\Heart data\\heart_failure_clinical_records_dataset.csv")

# Target variable
mydata['DEATH_EVENT'] = mydata['DEATH_EVENT'].astype(int)

# =========================================
# 🔷 3. Handle Missing Values
# =========================================
imputer = SimpleImputer(strategy='mean')
X = mydata.drop('DEATH_EVENT', axis=1)
y = mydata['DEATH_EVENT']

X = pd.DataFrame(imputer.fit_transform(X), columns=X.columns)

# =========================================
# 🔷 4. Train-Test Split
# =========================================
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=123, stratify=y
)

# =========================================
# 🌳 5. Train Decision Tree Model
# =========================================
tree_model = DecisionTreeClassifier(
    criterion='gini',
    max_depth=None,
    ccp_alpha=0.01,   # pruning parameter (like cp in R)
    random_state=123
)

tree_model.fit(X_train, y_train)

# =========================================
# 🌳 6. Plot Decision Tree
# =========================================
plt.figure(figsize=(20,10))
plot_tree(tree_model,
          feature_names=X.columns,
          class_names=["0","1"],
          filled=True)
plt.title("Decision Tree")
plt.show()

# =========================================
# 🔮 7. Predictions (Train)
# =========================================
train_pred = tree_model.predict(X_train)

print("\nTRAIN CONFUSION MATRIX")
print(confusion_matrix(y_train, train_pred))
print(classification_report(y_train, train_pred))

# =========================================
# 🔮 8. Predictions (Test)
# =========================================
test_pred = tree_model.predict(X_test)

print("\nTEST CONFUSION MATRIX")
print(confusion_matrix(y_test, test_pred))
print(classification_report(y_test, test_pred))

# =========================================
# 📊 9. ROC Curve + AUC
# =========================================
y_prob = tree_model.predict_proba(X_test)[:,1]

fpr, tpr, thresholds = roc_curve(y_test, y_prob)
roc_auc = auc(fpr, tpr)

plt.figure()
plt.plot(fpr, tpr, label=f"AUC = {roc_auc:.3f}")
plt.plot([0,1],[0,1],'--')
plt.xlabel("False Positive Rate")
plt.ylabel("True Positive Rate")
plt.title("ROC Curve")
plt.legend()
plt.show()

# =========================================
# 📊 10. Feature Importance
# =========================================
importances = pd.Series(tree_model.feature_importances_, index=X.columns)
importances.sort_values().plot(kind='barh', title="Feature Importance")
plt.show()
