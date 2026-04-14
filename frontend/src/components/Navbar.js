import React from "react";
import { Link } from "react-router-dom";
import "./Navbar.css";

const Navbar = () => {
  return (
    <nav className="navbar">
      <h2>LoanApp</h2>
      <div>
        <Link to="/">Home</Link>
        <Link to="/apply">Apply Loan</Link>
        <Link to="/my-loans">My Loans</Link>
        <Link to="/analytics">Analytics</Link>
        <Link to="/login">Login</Link>
      </div>
    </nav>
  );
};

export default Navbar;
