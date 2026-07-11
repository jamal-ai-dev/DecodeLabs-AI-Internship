"""
DecodeLabs AI Internship - Project 2
Data Classification Using AI (E-Commerce Order Status Prediction)

Dataset: Dataset_for_Data_Analytics.xlsx (provided by DecodeLabs)
Goal: Predict OrderStatus (Cancelled, Returned, Pending, Shipped, Delivered)
      based on order details such as Product, Quantity, UnitPrice,
      PaymentMethod, CouponCode, and ReferralSource.

Pipeline (IPO framework):
  INPUT   -> Load dataset, select features, encode categorical columns, scale
  PROCESS -> Train/test split, train a KNN classifier
  OUTPUT  -> Evaluate with confusion matrix + F1 score (not just accuracy)
"""

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import confusion_matrix, classification_report, f1_score, accuracy_score

DATA_FILE = "Dataset_for_Data_Analytics.xlsx"

# Columns that are IDs or free text -- not useful signals for prediction
DROP_COLUMNS = ["OrderID", "CustomerID", "TrackingNumber", "ShippingAddress", "Date"]

TARGET_COLUMN = "OrderStatus"


def load_data(path=DATA_FILE):
    """
    STEP 1: INPUT - Load and understand the dataset.
    """
    df = pd.read_excel(path)
    print("=== Dataset Preview ===")
    print(df.head())
    print(f"\nTotal rows: {len(df)}")
    print(f"\nOrderStatus distribution:\n{df[TARGET_COLUMN].value_counts()}\n")
    return df


def prepare_features(df):
    """
    STEP 2: Clean and encode the data.
    - Drop ID/free-text columns that carry no predictive signal
    - Fill missing CouponCode with 'NONE' (missing = no coupon used)
    - Encode categorical columns as numbers (models need numeric input)
    """
    df = df.drop(columns=DROP_COLUMNS)

    # Missing CouponCode genuinely means "no coupon used" -- keep that as its own category
    df["CouponCode"] = df["CouponCode"].fillna("NONE")

    # Separate features (X) from the target (y)
    X = df.drop(columns=[TARGET_COLUMN])
    y = df[TARGET_COLUMN]

    # Encode categorical columns to numbers using LabelEncoder
    categorical_cols = X.select_dtypes(include="object").columns.tolist() + \
        X.select_dtypes(include="string").columns.tolist()
    categorical_cols = list(set(categorical_cols))

    encoders = {}
    for col in categorical_cols:
        le = LabelEncoder()
        X[col] = le.fit_transform(X[col].astype(str))
        encoders[col] = le

    # Encode the target labels too
    target_encoder = LabelEncoder()
    y_encoded = target_encoder.fit_transform(y)

    return X, y_encoded, target_encoder


def split_data(X, y, test_size=0.2, random_state=42):
    """
    STEP 3: PROCESS - Split into training and testing sets (80/20, stratified).
    """
    return train_test_split(X, y, test_size=test_size, random_state=random_state, stratify=y)


def scale_features(X_train, X_test):
    """
    Scale features so no single feature (e.g. UnitPrice) dominates
    just because its numeric range is bigger than others.
    """
    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test)
    return X_train_scaled, X_test_scaled


def train_model(X_train, y_train, k=5):
    """
    STEP 4: PROCESS - Apply a simple classification algorithm (KNN).
    """
    model = KNeighborsClassifier(n_neighbors=k)
    model.fit(X_train, y_train)
    return model


def evaluate_model(model, X_test, y_test, target_encoder):
    """
    STEP 5: OUTPUT - Evaluate using accuracy, F1 score, and confusion matrix.
    """
    predictions = model.predict(X_test)

    accuracy = accuracy_score(y_test, predictions)
    f1 = f1_score(y_test, predictions, average="weighted")
    cm = confusion_matrix(y_test, predictions)
    labels = target_encoder.classes_

    print("=== Model Evaluation ===")
    print(f"Accuracy: {accuracy:.2%}")
    print(f"F1 Score (weighted): {f1:.2f}\n")
    print("Confusion Matrix:")
    print(pd.DataFrame(cm, index=labels, columns=labels))
    print("\nClassification Report:")
    print(classification_report(y_test, predictions, target_names=labels))

    return accuracy, f1, cm


def main():
    df = load_data()
    X, y, target_encoder = prepare_features(df)
    X_train, X_test, y_train, y_test = split_data(X, y)
    X_train_scaled, X_test_scaled = scale_features(X_train, X_test)
    model = train_model(X_train_scaled, y_train, k=5)
    evaluate_model(model, X_test_scaled, y_test, target_encoder)


if __name__ == "__main__":
    main()