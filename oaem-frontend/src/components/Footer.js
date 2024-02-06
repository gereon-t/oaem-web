import React from 'react';
import './Footer.css';

const Footer = () => {
    return <footer className='footer'>
        <div className='footer-items'>
            <a href='https://github.com/gereon-t/oaem-web'>gereon-t/oaem-web</a>
            <div className='footer-divider'></div>
            <a href='/privacy'>Datenschutzerklärung</a>
        </div>
    </footer>
}

export default Footer;