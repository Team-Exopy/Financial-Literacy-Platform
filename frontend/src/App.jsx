import React from 'react';
import SIPCalculator from './SIPCalculator/SIPCalculator';

function App() {
  return (
    <div>
      <h1 style={styles.title}>SIP Calculator App</h1>
      <SIPCalculator />
    </div>
  );
}

const styles = {
  title: {
    textAlign: 'center',
    marginTop: '20px',
    fontSize: '24px',
  },
};

export default App;
