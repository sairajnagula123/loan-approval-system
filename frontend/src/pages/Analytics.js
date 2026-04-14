import React, { useEffect, useState } from "react";
import API from "../services/api";

const Analytics = () => {
  const [stats, setStats] = useState(null);

  useEffect(() => {
    API.get("/analytics/stats")
      .then((res) => setStats(res.data))
      .catch(() => alert("Error fetching stats"));
  }, []);

  return (
    <div>
      <h2>Analytics</h2>
      {stats && (
        <div>
          <p>Total Loans: {stats.total_loans}</p>
          <p>Approved: {stats.approved}</p>
          <p>Rejected: {stats.rejected}</p>
          <p>Pending: {stats.pending}</p>
          <p>Average Loan Amount: {stats.average_loan_amount}</p>
          <p>Average Credit Score: {stats.average_credit_score}</p>
        </div>
      )}
    </div>
  );
};

export default Analytics;
