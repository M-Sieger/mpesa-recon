import './Header.css';

import React from 'react';

const Header = () => {
  return (
    <header className="header">
      <div className="header-content">
        <img
          src="https://upload.wikimedia.org/wikipedia/commons/4/49/Flag_of_Kenya.svg"
          alt="Kenya Flag"
          className="flag"
        />
        <h1 className="title">M‑PESA Reconciliation Tool</h1>
        <p className="subtitle">
          🇰🇪 Made for Kenyan entrepreneurs – Analyze your M‑PESA statements easily, securely & for free.
        </p>
      </div>
    </header>
  );
};

export default Header;
