# Data Classification Using AI — Order Status Prediction (Project 2)

## Description
A supervised learning classification model built in Python as part of the DecodeLabs AI Internship (Week 2, Project 2). The model uses the **e-commerce order dataset** provided by DecodeLabs (`Dataset_for_Data_Analytics.xlsx`, 1,200 orders) and a **K-Nearest Neighbors (KNN)** algorithm to predict `OrderStatus` (Cancelled, Returned, Pending, Shipped, or Delivered) based on order features such as Product, Quantity, UnitPrice, PaymentMethod, CouponCode, and ReferralSource.

The project follows the full supervised learning pipeline: load data → clean & encode categorical features → scale numeric features → split into train/test sets → train the model → evaluate using accuracy, F1 score, and a confusion matrix.

## Features
- Loads and previews the dataset (1,200 rows, 5 balanced order status classes)
- Drops ID/free-text columns (`OrderID`, `CustomerID`, `TrackingNumber`, `ShippingAddress`, `Date`) that carry no predictive signal
- Handles missing `CouponCode` values by treating them as their own category ("NONE" = no coupon used)
- Encodes categorical columns (`Product`, `PaymentMethod`, `CouponCode`, `ReferralSource`) numerically
- Scales features using `StandardScaler`
- Splits data into 80% training / 20% testing (stratified)
- Trains a KNN classifier (`k=5`)
- Evaluates using accuracy, F1 score, confusion matrix, and a full classification report

## How to Run
1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
2. Navigate to the project folder:
   ```bash
   cd Project2-DataClassification
   ```
3. Run the script:
   ```bash
   python order_status_classifier.py
   ```

## Results & Key Finding
```
Accuracy: 21.67%
F1 Score (weighted): 0.21
```

With 5 balanced classes, random guessing would score about 20% — so this model performs only marginally better than chance. **This is an important and honest finding, not a bug**: it indicates that the available features (Product, Quantity, UnitPrice, PaymentMethod, CouponCode, ReferralSource) do not contain a strong predictive signal for `OrderStatus` in this dataset. Real-world order outcomes are typically driven by factors not captured here (e.g. warehouse/fulfillment events, carrier delays, actual delivery data) rather than by what was ordered or how it was paid for.

This mirrors a real skill in applied ML: knowing when a low score means "the model needs work" versus "the data doesn't support this prediction task" — and reporting that clearly instead of hiding it.

## Tech Stack
- Python 3
- pandas, scikit-learn, openpyxl

## Possible Extensions
- Test whether a different target column (e.g. `PaymentMethod` or `Product`) is more predictable from the numeric features
- Engineer new features from `Date` (e.g. day of week, month) to see if timing affects status
- Compare KNN against `LogisticRegression` or `RandomForestClassifier` to confirm the low signal isn't algorithm-specific

## Author
DecodeLabs AI Internship — Batch 2026