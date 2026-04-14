import React, { useEffect, useState } from "react";
import API from "../services/api";

const MyLoans = () => {
  const [loans, setLoans] = useState([]);

  useEffect(() => {
    API.get("/loan/my-loans")
      .then((res) => setLoans(res.data))
      .catch(() => alert("Failed to load loans"));
  }, []);

  return (
    <div style={{ padding: "20px" }}>
      <h2>My Loans</h2>
      <ul>
        {loans.map((loan) => (
          <li key={loan.id}>
            Loan Amount: {loan.loan_amount} | Status: {loan.status} | Score:{" "}
            {loan.prediction_score}
          </li>
        ))}
      </ul>
    </div>
  );
};

export default MyLoans;
