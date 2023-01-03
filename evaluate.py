def get_metrics(X_train, y_train):
    
    y_pred = knn.predict(X_train)
    
    TN, FP, FN, TP = confusion_matrix(y_train, y_pred).ravel()
    ALL = TP + FP + FN + TN
    accuracy = (TP + TN)/ALL

    true_pos_rate = TP/(FN+TP)
    false_pos_rate = FP/(TN+FP)
    true_neg_rate = TN/(TN+FP)
    false_neg_rate = FN/(TP+FN)

    precision = TP/(TP+FP)
    recall = TP/(TP+FN)
    f1_formula = TP/(TP+(.5*(FP+FN)))
    support_pos = TP + FN
    support_neg = FP + TN
    
    print(f"Accuracy: {accuracy:.2f}")
    print(f"True Positive Rate: {true_pos_rate:.2f}")
    print(f"False Positive Rate: {false_pos_rate:.2f}")
    print(f"True Negative Rate: {true_neg_rate:.2f}")
    print(f"False Negative Rate: {false_neg_rate:.2f}")
    print(f"Precision: {precision:.2f}")
    print(f"Recall: {recall:.2f}")
    print(f"F1: {f1_formula:.2f}")
    print(f"Support: {support_pos}")