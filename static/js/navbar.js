import React from 'react';
import { AppBar, Toolbar, Typography, Button } from '@mui/material';

const Navbar = () => {
  return (
    <AppBar position="static" sx={{ backgroundColor: '#333' }}>
      <Toolbar>
        <Typography variant="h6" sx={{ flexGrow: 1 }}>
          Compania Ta
        </Typography>
        <Button color="inherit" href="/">Home</Button>
        <Button color="inherit" href="/services">Servicii</Button>
        <Button color="inherit" href="/contact">Contact</Button>
      </Toolbar>
    </AppBar>
  );
};

export default Navbar;
