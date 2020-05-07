import numpy as np
from sklearn.metrics import confusion_matrix
import matplotlib.pyplot as plt


y_true = [1, -1,  0,  0,  1, -1,  1,  0, -1,  0,  1, -1,  1,  0,  0, -1,  0]
y_prediction = [-1, -1,  1,  0,  0,  0,  0, -1,  1, -1,  1,  1,  0,  0,  1,  1, -1]
cnf_matrix = confusion_matrix(y_true, y_prediction)
# print(cnf_matrix)
# [1 1 3]
# [3 2 2]
# [1 3 1]

FP = cnf_matrix.sum(axis=0) - np.diag(cnf_matrix)
FN = cnf_matrix.sum(axis=1) - np.diag(cnf_matrix)
TP = np.diag(cnf_matrix)
TN = cnf_matrix.sum() - (FP + FN + TP)

FP = FP.astype(float)
FN = FN.astype(float)
TP = TP.astype(float)
TN = TN.astype(float)

# Sensitivity, hit rate, recall, or true positive rate
TPR = TP/(TP+FN)
# Specificity or true negative rate
TNR = TN/(TN+FP)
# Precision or positive predictive value
PPV = TP/(TP+FP)
# Negative predictive value
NPV = TN/(TN+FN)
# Fall out or false positive rate
FPR = FP/(FP+TN)
print(FPR)
# False negative rate
FNR = FN/(TP+FN)
# False discovery rate
FDR = FP/(TP+FP)
# Overall accuracy
ACC = (TP+TN)/(TP+FP+FN+TN)

x_article = ["aaa", "bbb", "ccc"]
fpr_list = {'aaa': 0.5, 'bbb': 0.7, 'ccc': 0.6}
ax = plt.subplots()
for article in x_article:
    performance = fpr_list[article]
    plt.bar(article, performance, align="center")

plt.xlabel("Article")
plt.ylabel("FPR")
plt.show()