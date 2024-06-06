import React from 'react';
import ReactDOM from 'react-dom/client';
import './index.css';
import { BrowserRouter, Routes, Route } from "react-router-dom";
import App from './App';
import reportWebVitals from './reportWebVitals';
import Chat from './pages/chat'
import Contact from './pages/contact';
import Login from './pages/login';
import Nav from './components/nav/Nav'

const root = ReactDOM.createRoot(document.getElementById('root'));

root.render(
  
  <BrowserRouter>
    
    <Nav/>
   
    <Routes>
        <Route path='/' element={<App/>}/>
        <Route  path='/chat' element={<Chat/>}/>
        <Route  path='/contact' element={<Contact/>}/>
        <Route  path='/login' element={<Login/>}/>
    </Routes>
   
  </BrowserRouter>
);

// If you want to start measuring performance in your app, pass a function
// to log results (for example: reportWebVitals(console.log))
// or send to an analytics endpoint. Learn more: https://bit.ly/CRA-vitals
reportWebVitals();
