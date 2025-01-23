// script.js
document.addEventListener('DOMContentLoaded', function() {
    let index = 0;
    const testimonials = document.querySelectorAll('.testimonial');
    const totalTestimonials = testimonials.length;

    setInterval(function() {
        testimonials[index].style.display = 'none';
        index = (index + 1) % totalTestimonials;
        testimonials[index].style.display = 'block';
    }, 3000); // Schimbă fiecare 3 secunde
});

import React from 'react';
import Navbar from './navbar'; // Importă navbar-ul
import { Container, CssBaseline } from '@mui/material';

function App() {
  return (
    <div>
      <CssBaseline /> {/* Normalizează stilurile */}
      <Navbar /> {/* Afișează navbar-ul */}
      <Container>
        <h1>Bine ai venit pe site-ul nostru!</h1>
        <p>Servicii contabile pentru afaceri mici și mari.</p>
      </Container>
    </div>
  );
}

export default App;
document.querySelector('.dropbtn').addEventListener('click', function(e) {
  e.preventDefault();
  const dropdown = document.querySelector('.dropdown-content');
  dropdown.style.display = dropdown.style.display === 'block' ? 'none' : 'block';
});

