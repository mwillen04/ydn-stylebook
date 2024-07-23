import React, { useState, useEffect } from "react";
import { Link } from "react-router-dom";
import parse from 'html-react-parser';

function DefaultHome() {

    const [entry, setEntry] = useState([])

    useEffect(() => {
        
        fetch('/random')
          .then(response => response.json())
          .then(data => {
            setEntry(data.entry);
          })
          .catch(error => console.error('Error:', error));
    }, []);

    console.log(entry[0], " : ", entry[1]);
    
    if (entry.length === 0) {
        return (
            <div id="home_default">
            <h3>Ask an Editor</h3>

            <p>Have a question and can’t find an answer in the Stylebook? Submit a question on our <Link to="ask">Q&A page</Link> and we’ll get back to you as soon as we can!</p>

            <br />
            <h3>Rule of the Day:</h3>
        </div>
        )
    }

    return (
        <div id="home_default">
            <h3>Ask an Editor</h3>

            <p>Have a question and can’t find an answer in the Stylebook? Submit a question on our <Link to="ask">Q&A page</Link> and we’ll get back to you as soon as we can!</p>

            <br />
            <h3>Rule of the Day: {entry[0]}</h3>

            {parse(entry[1])}
        </div>
    )
}

export default DefaultHome;