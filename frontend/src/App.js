import React from "react";
import "./App.css";
import { BrowserRouter as Router, Routes, Route, NavLink } from "react-router-dom";

import Signup from "./pages/Signup";
import Login from "./pages/Login";
import LoanApplication from "./pages/LoanApplication";
import MyLoans from "./pages/MyLoans";
import AdminDashboard from "./pages/AdminDashboard";

const App = () => {
  return (
    <Router>
      {/* Navigation Bar */}
      <nav>
        <NavLink to="/" end>Home</NavLink>
        <NavLink to="/signup">Signup</NavLink>
        <NavLink to="/login">Login</NavLink>
        <NavLink to="/apply">Apply Loan</NavLink>
        <NavLink to="/my-loans">My Loans</NavLink>
        <NavLink to="/admin">Admin</NavLink>
      </nav>

      {/* Routes */}
      <Routes>
        <Route path="/" element={<h2 style={{ textAlign: "center", marginTop: "80px" }}>Welcome to Loan Approval System</h2>} />
        <Route path="/signup" element={<Signup />} />
        <Route path="/login" element={<Login />} />
        <Route path="/apply" element={<LoanApplication />} />
        <Route path="/my-loans" element={<MyLoans />} />
        <Route path="/admin" element={<AdminDashboard />} />
      </Routes>
    </Router>
  );
};

export default App;
