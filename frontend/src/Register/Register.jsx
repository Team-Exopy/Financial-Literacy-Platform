import React, { useState } from 'react';
import { Link, useNavigate } from 'react-router-dom';
import './Register.css';
// import Apple from '../assets/Apple.svg';
// import Apple  from '../assets/Apple.svg' 
import password from '../assets/password.svg';
import google from '../assets/google.svg';
import email from '../assets/email.svg';
import user from '../assets/user.svg';
// import { registerUser } from '../../services/api';

function Sign() {
  const [formData, setFormData] = useState({
    "email": "",
    "username": "",
    "first_name": "",
    "last_name": "",
    "password": "",
    "password2": ""
}
);

  const [error, setError] = useState('');
  const navigate = useNavigate();

  const handleChange = (e) => {
    setFormData({ ...formData, [e.target.name]: e.target.value });
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      const response = await registerUser(formData);
      console.log('Registration successful', response);
      alert('Registration successful');
      navigate('/Log'); // Navigate to the homepage
    } catch (error) {
      console.error('Error registering user', error.response ? error.response.data : error.message);
      setError(error.response ? error.response.data.detail : error.message);
    }
  };

  return (
    <div>
      <form className="sign-in-form" onSubmit={handleSubmit}>
        <div className="sign-in-flex-column">
          <label className="sign-in-label">First Name</label>
        </div>
        <div className="sign-in-inputForm">
          <img src={user} alt="user" />
          <input
            type="text"
            className="sign-in-input"
            name="first_name"
            placeholder="Enter your First Name"
            value={formData.first_name}
            onChange={handleChange}
          />
        </div>

        <div className="sign-in-flex-column">
          <label className="sign-in-label">Last Name</label>
        </div>
        <div className="sign-in-inputForm">
          <img src={user} alt="user" />
          <input
            type="text"
            className="sign-in-input"
            name="last_name"
            placeholder="Enter your Last Name"
            value={formData.last_name}
            onChange={handleChange}
          />
        </div>

        <div className="sign-in-flex-column">
          <label className="sign-in-label">User Name</label>
        </div>
        <div className="sign-in-inputForm">
          <img src={user} alt="user" />
          <input
            type="text"
            className="sign-in-input"
            name="username"
            placeholder="Enter your User Name"
            value={formData.username}
            onChange={handleChange}
          />
        </div>

        <div className="sign-in-flex-column">
          <label className="sign-in-label">Email</label>
        </div>
        <div className="sign-in-inputForm">
          <img src={email} alt="email" />
          <input
            type="text"
            className="sign-in-input"
            name="email"
            placeholder="Enter your Email"
            value={formData.email}
            onChange={handleChange}
          />
        </div>

        <div className="sign-in-flex-column">
          <label className="sign-in-label">Password</label>
        </div>
        <div className="sign-in-inputForm">
          <img src={password} alt="password" />
          <input
            type="password"
            className="sign-in-input"
            name="password"
            placeholder="Enter your Password"
            value={formData.password}
            onChange={handleChange}
          />
        </div>

        <div className="sign-in-flex-column">
          <label className="sign-in-label">Confirm Password</label>
        </div>
        <div className="sign-in-inputForm">
          <img src={password} alt="password" />
          <input
            type="password"
            className="sign-in-input"
            name="password2"
            placeholder="Confirm your Password"
            value={formData.password2}
            onChange={handleChange}
          />
        </div>

        <div className="sign-in-flex-row">
          <div>
            <input type="checkbox" />
            <label className="sign-in-label">Remember me</label>
          </div>
          <span className="sign-in-span">Forgot password?</span>
        </div>
        <button className="sign-in-button-submit" type="submit">
          Sign Up
        </button>
        {error && <p className="error-message">{error}</p>}
        <p className="sign-in-p">
          Already have an account?{' '}
          <span className="sign-in-span">
            <Link to="/login">Sign In</Link>
          </span>
        </p>
        <p className="sign-in-p sign-in-line">Or With</p>
        <div className="sign-in-flex-row">
          <button className="sign-in-btn sign-in-google">
            <img src={google} alt="Google" />
            Google
          </button>
          <button className="sign-in-btn sign-in-apple">
            <img src={google} alt="Apple" />
            Apple
          </button>
        </div>
      </form>
    </div>
  );
}

export default Sign;


