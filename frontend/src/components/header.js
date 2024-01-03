import React from "react";
import { Link } from "react-router-dom";
import logo from '../assets/images/nameplate_recolor2.png';

function Header() {
    return (
        <header id="top">
            <a href="https://yaledailynews.com/" target="_blank" rel="noreferrer"><img src={logo} alt="The Yale Daily News" className="logo" /></a>

            <nav>
                <Link to="/" className="pages">Home</Link>
                <Link to="/top10" className="pages">Top 10 Rules</Link>
                <Link to="/stylebook" className="pages">Stylebook</Link>
                <Link to="/edits" className="pages">Edits</Link>
                <a href="https://www.apstylebook.com/" className="pages" target="_blank" rel="noreferrer">AP Style</a>
                <Link to="/staff" className="pages">Copy Staff</Link>
            </nav>
        </header>
    )
};

export default Header;
