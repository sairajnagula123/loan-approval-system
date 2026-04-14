import React, { useState } from "react";
import API from "../services/api";

const LoanApplication = () => {
  const [form, setForm] = useState({
    age: "",
    income: "",
    loan_amount: "",
    credit_score: "",
  });

  const handleChange = (e) =>
    setForm({ ...form, [e.target.name]: e.target.value });

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      const token = localStorage.getItem("token");
      await API.post("/loan/apply", form, {
        headers: { Authorization: `Bearer ${token}` },
      });
      alert("Loan application submitted successfully!");
    } catch (err) {
      alert("Failed to submit loan application");
      console.error(err);
    }
  };

  return (
    <div className="container">
      <h2>Apply for Loan</h2>
      <form onSubmit={handleSubmit}>
        <input
          type="number"
          name="age"
          placeholder="Age"
          value={form.age}
          onChange={handleChange}
          required
        />
        <input
          type="number"
          name="income"
          placeholder="Income"
          value={form.income}
          onChange={handleChange}
          required
        />
        <input
          type="number"
          name="loan_amount"
          placeholder="Loan Amount"
          value={form.loan_amount}
          onChange={handleChange}
          required
        />
        <input
          type="number"
          name="credit_score"
          placeholder="Credit Score"
          value={form.credit_score}
          onChange={handleChange}
          required
        />
        <button type="submit">Submit Loan</button>
      </form>
    </div>
  );
};

export default LoanApplication;
