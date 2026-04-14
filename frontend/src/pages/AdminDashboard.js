import React, { useEffect, useState } from "react";
import API from "../services/api";

const AdminDashboard = () => {
  const [loans, setLoans] = useState([]);

  useEffect(() => {
    API.get("/loan/all")
      .then((res) => setLoans(res.data))
      .catch(() => alert("Failed to load loans. Admin access required."));
  }, []);

  const updateStatus = (id, status) => {
    API.put(`/loan/update/${id}`, { status })
      .then(() => {
        alert("Status updated!");
        setLoans(
          loans.map((loan) =>
            loan.id === id ? { ...loan, status } : loan
          )
        );
      })
      .catch(() => alert("Failed to update loan status."));
  };

  return (
    <div className="container">
      <h2>Admin Dashboard</h2>
      {loans.length === 0 && <p>No loan applications available.</p>}
      {loans.map((loan) => (
        <div key={loan.id} className="loan-list-item">
          <p>
            Loan Amount: {loan.loan_amount} | User ID: {loan.user_id} | Status:{" "}
            <span
              className={
                loan.status === "Approved"
                  ? "status-approved"
                  : loan.status === "Rejected"
                  ? "status-rejected"
                  : "status-pending"
              }
            >
              {loan.status}
            </span>
          </p>
          <div style={{ marginTop: "5px" }}>
            <button
              className="approve"
              onClick={() => updateStatus(loan.id, "Approved")}
            >
              Approve
            </button>
            <button
              className="reject"
              style={{ marginLeft: "10px" }}
              onClick={() => updateStatus(loan.id, "Rejected")}
            >
              Reject
            </button>
          </div>
        </div>
      ))}
    </div>
  );
};

export default AdminDashboard;
