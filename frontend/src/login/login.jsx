import React,{ useState}from 'react';
import { Link,useNavigate } from 'react-router-dom';
import './login.css';
// import Apple from '../assets/apples.svg';  
import password from '../assets/password.svg';
import google from '../assets/google.svg';
import email from '../assets/email.svg';
// import { loginUser } from '../../services/api';

function Log() {
 
    const [formData, setFormData] = useState({
     "email": "",
  "password": ""
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
        const response = await loginUser(formData);
        console.log('Registration successful', response);
        alert('login successful');
        navigate('/'); // Navigate to the homepage
      } catch (error) {
        console.error('Error registering user', error.response ? error.response.data : error.message);
        setError(error.response ? error.response.data.detail : error.message);
      }
    };

  return (
    <div>
      <form className="form" onSubmit={handleSubmit}>
        <div className="flex-column">
          <label>Email</label>
        </div>
        <div className="inputForm">
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

        <div className="flex-column">
          <label>Password</label>
        </div>
        <div className="inputForm">
          <img src={password} alt="password" />
          <input
            type="password"
            className="sign-in-input"
            name="password"
            placeholder="Enter your Password"
            value={formData.password}
            onChange={handleChange}
          />
          <svg viewBox="0 0 576 512" height="1em" xmlns="http://www.w3.org/2000/svg">
            <path d="M288 160a64 64 0 1064 64 64.072 64.072 0 00-64-64zm0 104a40 40 0 1140-40 40.045 40.045 0 01-40 40zm192-24c0 48.6-64 128-192 128S96 288.6 96 240s64-128 192-128 192 79.4 192 128zm-32 0c0-36.4-58.6-96-160-96s-160 59.6-160 96 58.6 96 160 96 160-59.6 160-96z" />
          </svg>
        </div>

        <div className="flex-row">
          <div>
            <input type="checkbox" />
            <label>Remember me</label>
          </div>
          <span className="span">Forgot password?</span>
        </div>
        <button className="button-submit">
          Sign In
        </button>
        {error && <p className="error-message">{error}</p>}
        <p className="p">
          Don't have an account? <span className="span">
            <Link to="/sign">Sign Up</Link>
          </span>
        </p>
        <p className="p line">Or With</p>
        <div className="flex-row">
          <button className="btn google">
            <img src={google} alt="Google" />
            Google
          </button>
          <button className="btn apple">
            <img src={google} alt="Apple" />
            Apple
          </button>
        </div>
      </form>
    </div>
  );
}

export default Log;
