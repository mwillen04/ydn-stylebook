import React from "react";
import { Link } from "react-router-dom";

function DefaultHome() {
    return (
        <div id="home_default">
            <h3>Ask an Editor</h3>

            <p>Have a question and can’t find an answer in the Stylebook? Submit a question on our <Link to="ask">Q&A page</Link> and we’ll get back to you as soon as we can!</p>

            <br />
            <h3>Rule of the Day:</h3>
        </div>
    )
}

export default DefaultHome;