from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app import database, models, schemas
from app.ml.predictor import predict_loan
from app.routes.auth_utils import get_current_user  # ensures only logged-in users can apply

router = APIRouter(prefix="/loan", tags=["Loan"])

@router.post("/apply", response_model=dict)
def apply_loan(
    application: schemas.LoanApplicationCreate,
    db: Session = Depends(database.get_db),
    current_user: models.User = Depends(get_current_user)
):
    """
    Endpoint for users to apply for a loan.
    The system predicts approval score using the trained ML model.
    """

    # 1️⃣ Predict using ML model
    score = predict_loan({
        "age": application.age,
        "income": application.income,
        "loan_amount": application.loan_amount,
        "credit_score": application.credit_score
    })

    # 2️⃣ Simple logic: Approve if score >= 50%
    status = "Approved" if score >= 50 else "Rejected"

    # 3️⃣ Save to database
    new_loan = models.LoanApplication(
        user_id=current_user.id,            # ✅ Link loan to user
        age=application.age,
        income=application.income,
        loan_amount=application.loan_amount,
        credit_score=application.credit_score,
        prediction_score=score,
        status=status
    )

    db.add(new_loan)
    db.commit()
    db.refresh(new_loan)

    # 4️⃣ Return result to frontend
    return {
        "message": "Loan application submitted successfully.",
        "prediction_score": f"{score}%",
        "status": status
    }
