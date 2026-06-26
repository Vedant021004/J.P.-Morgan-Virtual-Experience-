
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression

# Load loan data
df = pd.read_csv("Task 3 and 4_Loan_Data.csv")

# Features
X = df[
    [
        "credit_lines_outstanding",
        "loan_amt_outstanding",
        "total_debt_outstanding",
        "income",
        "years_employed",
        "fico_score"
    ]
]

# Target
y = df["default"]

# Train/Test Split
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

# Train model
model = LogisticRegression(max_iter=1000)
model.fit(X_train, y_train)

# Function to estimate expected loss
def expected_loss(
    credit_lines_outstanding,
    loan_amt_outstanding,
    total_debt_outstanding,
    income,
    years_employed,
    fico_score,
    recovery_rate=0.10
):

    borrower = pd.DataFrame({
        "credit_lines_outstanding":[credit_lines_outstanding],
        "loan_amt_outstanding":[loan_amt_outstanding],
        "total_debt_outstanding":[total_debt_outstanding],
        "income":[income],
        "years_employed":[years_employed],
        "fico_score":[fico_score]
    })

    # Probability of Default
    pd_estimate = model.predict_proba(borrower)[0][1]

    # Loss Given Default
    lgd = 1 - recovery_rate

    # Expected Loss
    expected_loss = (
        pd_estimate
        * lgd
        * loan_amt_outstanding
    )

    return {
        "Probability of Default": round(pd_estimate, 4),
        "Expected Loss": round(expected_loss, 2)
    }


# Example

result = expected_loss(
    credit_lines_outstanding=2,
    loan_amt_outstanding=50000,
    total_debt_outstanding=70000,
    income=90000,
    years_employed=8,
    fico_score=700
)

print(result)
