import React, { useState } from 'react';

const SIPCalculator = () => {
  const [investmentType, setInvestmentType] = useState('Monthly');
  const [monthlyInvestment, setMonthlyInvestment] = useState(1000);
  const [annualReturnRate, setAnnualReturnRate] = useState(10);
  const [years, setYears] = useState(5);
  const [futureValue, setFutureValue] = useState(null);

  const calculateSIP = () => {
    let periodsPerYear;
    switch (investmentType) {
      case 'Monthly':
        periodsPerYear = 12;
        break;
      case 'Quarterly':
        periodsPerYear = 4;
        break;
      case 'Semi-Annually':
        periodsPerYear = 2;
        break;
      case 'Annually':
        periodsPerYear = 1;
        break;
      default:
        periodsPerYear = 12;
    }

    const periodRate = (annualReturnRate / periodsPerYear) / 100;
    const totalPeriods = years * periodsPerYear;
    const futureValue =
      (monthlyInvestment * (Math.pow(1 + periodRate, totalPeriods) - 1) / periodRate) *
      (1 + periodRate);

    setFutureValue(futureValue.toFixed(2));
  };

  const totalInvestedAmount = monthlyInvestment * years * (investmentType === 'Monthly' ? 12 : investmentType === 'Quarterly' ? 4 : investmentType === 'Semi-Annually' ? 2 : 1);

  return (
    <div style={styles.container}>
      <h2 style={styles.heading}>Calculate SIP Mutual Fund Returns</h2>
      <div style={styles.options}>
        {['Monthly', 'Annually', 'Semi-Annually', 'Quarterly'].map(type => (
          <label key={type} style={styles.radioLabel}>
            <input
              type="radio"
              value={type}
              checked={investmentType === type}
              onChange={(e) => setInvestmentType(e.target.value)}
            />
            {type}
          </label>
        ))}
      </div>

      <div style={styles.inputGroup}>
        <label>Monthly investment amount (₹): </label>
        <input
          type="number"
          value={monthlyInvestment}
          onChange={(e) => setMonthlyInvestment(Number(e.target.value))}
          style={styles.input}
        />
      </div>

      <div style={styles.inputGroup}>
        <label>Expected Annual Return (%): </label>
        <input
          type="number"
          value={annualReturnRate}
          onChange={(e) => setAnnualReturnRate(Number(e.target.value))}
          style={styles.input}
        />
      </div>

      <div style={styles.inputGroup}>
        <label>Years: </label>
        <input
          type="number"
          value={years}
          onChange={(e) => setYears(Number(e.target.value))}
          style={styles.input}
        />
      </div>

      <button onClick={calculateSIP} style={styles.button}>Calculate</button>

      {futureValue && (
        <div style={styles.results}>
          <p>Invested Amount: ₹ {totalInvestedAmount}</p>
          <p>Resultant Amount: ₹ {futureValue}</p>
        </div>
      )}
    </div>
  );
};

const styles = {
  container: {
    padding: '20px',
    maxWidth: '600px',
    margin: '0 auto',
    backgroundColor: '#f9f9f9',
    borderRadius: '8px',
    boxShadow: '0 0 10px rgba(0, 0, 0, 0.1)',
  },
  heading: {
    textAlign: 'center',
    marginBottom: '20px',
  },
  options: {
    display: 'flex',
    justifyContent: 'space-around',
    marginBottom: '20px',
  },
  radioLabel: {
    cursor: 'pointer',
  },
  inputGroup: {
    marginBottom: '15px',
  },
  input: {
    width: '100%',
    padding: '8px',
    fontSize: '16px',
    borderRadius: '4px',
    border: '1px solid #ccc',
  },
  button: {
    width: '100%',
    padding: '10px',
    fontSize: '16px',
    color: '#fff',
    backgroundColor: '#007bff',
    border: 'none',
    borderRadius: '4px',
    cursor: 'pointer',
    marginTop: '10px',
  },
  results: {
    marginTop: '20px',
    textAlign: 'center',
  },
};

export default SIPCalculator;
