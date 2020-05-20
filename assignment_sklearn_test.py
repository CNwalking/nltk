import numpy as np
from sklearn.metrics import confusion_matrix
import matplotlib.pyplot as plt

# y_true = ["aaa", "bbb", "ddd"]
# y_prediction = ["ccc", "ddd", "ooo"]
# cnf_matrix = confusion_matrix(y_true, y_prediction)
# print(cnf_matrix)
#
# FP = cnf_matrix.sum(axis=0) - np.diag(cnf_matrix)
# FN = cnf_matrix.sum(axis=1) - np.diag(cnf_matrix)
# TP = np.diag(cnf_matrix)
# TN = cnf_matrix.sum() - (FP + FN + TP)
#
# FP = FP.astype(float)
# FN = FN.astype(float)
# TP = TP.astype(float)
# TN = TN.astype(float)
# # Fall out or false positive rate
# FPR = FP/(FP+TN)
# print(FPR)

# # Sensitivity, hit rate, recall, or true positive rate
# TPR = TP/(TP+FN)
# # Specificity or true negative rate
# TNR = TN/(TN+FP)
# # Precision or positive predictive value
# PPV = TP/(TP+FP)
# # Negative predictive value
# NPV = TN/(TN+FN)
# # False negative rate
# FNR = FN/(TP+FN)
# # False discovery rate
# FDR = FP/(TP+FP)
# # Overall accuracy
# ACC = (TP+TN)/(TP+FP+FN+TN)

# x_article = ["aaa", "bbb", "ccc"]
# fpr_list = {'aaa': 0.5, 'bbb': 0.7, 'ccc': 0.6}
# ax = plt.subplots()
# for article in x_article:
#     performance = fpr_list[article]
#     plt.bar(article, performance, align="center")
#
# plt.xlabel("Article")
# plt.ylabel("FPR")
# plt.show()


y_article = ["Are we using ventilators too much?",
             "Criminal records shut small biz owners out of aid",
             "Former UCLA soccer coach to plead guilty",
             "Iran's Guard says it launched satellite amid US tensions",
             "Man angry about stimulus check set shed on fire",
             "Map: Tracking the spread of coronavirus in the US",
             "Mar-a-Lago furloughs 153 servers, cooks over virus",
             "Senate panel backs Russian interference assessment",
             "Trump hits Virginia on gun control amid pandemic",
             "US OKs 1st virus test allowing self-swab at home",
             "What comes next amid Kim Jong Un health reports",
             "World on brink of 'a hunger pandemic': UN chief",
             ]
# fpr_list = {'Are we using ventilators too much?': 0.53,
#             'Criminal records shut small biz owners out of aid': 0.77,
#             'Former UCLA soccer coach to plead guilty': 0.46,
#             "Iran's Guard says it launched satellite amid US tensions": 0.67,
#             'Man angry about stimulus check set shed on fire': 0.62,
#             'Map: Tracking the spread of coronavirus in the US': 0.44,
#             'Mar-a-Lago furloughs 153 servers, cooks over virus': 0.30,
#             'Senate panel backs Russian interference assessment': 0.45,
#             'Trump hits Virginia on gun control amid pandemic': 0.89,
#             'US OKs 1st virus test allowing self-swab at home': 0.42,
#             'What comes next amid Kim Jong Un health reports': 0.33,
#             "World on brink of 'a hunger pandemic': UN chief": 0.54,
#             }
# fig, ax = plt.subplots()
# for article in y_article:
#     performance = fpr_list[article]
#     plt.bar(performance, article, align="center")
# plt.title("FPR of all News article")
# plt.xlabel("FPR")
# plt.ylabel("Article")
# plt.show()

import matplotlib.pyplot as plt

# FPR data
data = [0.19, 0.78, 0.41, 0.34, 0.67, 0.29, 0.54, 0.33, 0.63, 0.85, 0.66, 0.39]
fig, ax = plt.subplots()
b = ax.barh(range(len(y_article)), data, color='#6699CC')
y_article.reverse()
# Add data labels to the right of the horizontal horizontal bar chart
for rect in b:
    w = rect.get_width()
    ax.text(w, rect.get_y() + rect.get_height() / 2, '%.2f' % float(w), ha='left', va='center')

# Set the tick labels on the ordinate of the Y axis
ax.set_yticks(range(len(y_article)))
ax.set_yticklabels(y_article)

plt.xticks((0, 0.25, 0.5, 0.75, 1))

plt.title('FPR of all News', loc='center', fontsize='25',
          fontweight='bold', color='red')
plt.show()