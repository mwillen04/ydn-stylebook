import React, { useState, useEffect } from "react";
import Rule from "../components/rule";

function Top10() {

    const [rules, setRules] = useState([]);

    useEffect(() => {

        fetch('/top10')
          .then(response => response.json())
          .then(data => {
            setRules(data.rules);
          })
          .catch(error => console.error('Error:', error));
    }, []);

    return (
        <main>
            <br />
            <h1>Top 10 Rules</h1>
            <br />

            <ol className="top10" style={{margin: "0px 50px"}}>
                {rules.map(rule => <Rule rule={rule}/>)}
            </ol>
        </main>
    )
}

export default Top10;