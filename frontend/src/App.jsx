import React from 'react';
import { Routes, Route } from 'react-router-dom';
import Home from './Home/home'
import SIPCalculator from './SIPCalculator/SIPCalculator';
import { BrowserRouter } from 'react-router-dom';
import Login from './login/login';
import Register from './Register/Register';

function App() {
  return (
   <BrowserRouter>
   <Routes>
    <Route path='/' element={<Home />} />
    <Route path='/login' element={<Login />} />
    <Route path='/register' element={<Register />} />
    <Route path='/sip' element={<SIPCalculator />} />
    {/* <Route path='/' element={<Home />} />
    <Route path='/' element={<Home />} /> */}
    
   </Routes>
   </BrowserRouter>
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
