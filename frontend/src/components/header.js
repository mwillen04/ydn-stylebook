import React from "react";
import { Link, useLocation } from "react-router-dom";
import logo from '../assets/images/ydn_logo.png';

function Header() {

    let location = useLocation().pathname.split('/');
    if (location.length === 1) location = location[0];
    else location = location[1];

    const isCurrent = (page) => {
        return location === page ? " current_page" : "";
    }

    return (
        <header id="top">
            <a href="https://yaledailynews.com/" style={{display: "contents"}} target="_blank" rel="noreferrer"><img src={logo} alt="The Yale Daily News" className="logo" /></a>

            <div className="title"><Link to="/" className="pages">Copy Stylebook</Link></div>

            <nav>
                <Link to="/" className={"pages" + isCurrent("")}>Home</Link>
                <Link to="/top10" className={"pages" + isCurrent("top10")}>Top 10 Rules</Link>
                <Link to="/stylebook" className={"pages" + isCurrent("stylebook")}>Stylebook</Link>
                <Link to="/ask" className={"pages" + isCurrent("ask")}>Q&A</Link>
                <a href="https://www.apstylebook.com/" className="pages" target="_blank" rel="noreferrer">AP Style</a>
                <Link to="/about" className={"pages" + isCurrent("about")}>About</Link>
            </nav>
        </header>
    )
};

export default Header;
