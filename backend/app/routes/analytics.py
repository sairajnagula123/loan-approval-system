from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from .. import database, models
from .auth_utils import get_current_user
  # reuse token validation

router = APIRouter()

@router.get("/stats")
def get_loan_stats(db: Session = Depends(database.get_db),
                   current_user: models.User = Depends(get_current_user)):
    # Only admins can view analytics
    if current_user.role != "admin":
        raise HTTPException(status_code=403, detail="Admins only")

    total_loans = db.query(models.LoanApplication).count()
    approved = db.query(models.LoanApplication).filter(models.LoanApplication.status == "Approved").count()
    rejected = db.query(models.LoanApplication).filter(models.LoanApplication.status == "Rejected").count()
    pending = db.query(models.LoanApplication).filter(models.LoanApplication.status == "Pending").count()

    avg_amount = db.query(models.LoanApplication.loan_amount).all()
    avg_amount = round(sum([a[0] for a in avg_amount if a[0]]) / total_loans, 2) if total_loans else 0

    avg_credit = db.query(models.LoanApplication.credit_score).all()
    avg_credit = round(sum([c[0] for c in avg_credit if c[0]]) / total_loans, 2) if total_loans else 0

    return {
        "total_loans": total_loans,
        "approved": approved,
        "rejected": rejected,
        "pending": pending,
        "average_loan_amount": avg_amount,
        "average_credit_score": avg_credit
    }
