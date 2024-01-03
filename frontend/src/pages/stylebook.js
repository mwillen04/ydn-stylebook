import React, { useEffect, useState } from "react";
import Section from "../components/section";

function Stylebook() {

    const [results, setResults] = useState({});

    useEffect(() => {

        fetch('/stylebook')
          .then(response => response.json())
          .then(data => {
            setResults(data.dictionary);
          })
          .catch(error => console.error('Error:', error));
    }, []);

    return (
        <main>
            <div>
                <br />
                <h1>STYLEBOOK OF THE YALE DAILY NEWS</h1>
                <h2 style={{marginBottom : 1.5 + "lh"}}>Fourth Edition, Produced January 2024</h2>

                <p style={{marginLeft : 150 + "px", marginRight : 150 + "px", textAlign : "justify"}}>
                    The Stylebook of the Yale Daily News takes precedence over the <a href="http://www.apstylebook.com/" target="_blank" rel="noreferrer">AP Stylebook</a>, and the AP Stylebook takes precedence over the <a href="http://www.merriam-webster.com/" target="_blank" rel="noreferrer">Merriam-Webster Dictionary</a> in cases of disagreement. If no entry exists for a question encountered during production, please keep note of the issue and report the matter to a copy editor.
                </p>
                <br />
                <p style={{textAlign : "center"}}>
                    —&nbsp;
                    {Object.keys(results).map(letter => <><a href={"#" + letter} class="letters">{letter}</a>&nbsp;</>)}
                    —
                </p>
            </div>

            {Object.entries(results).filter(section => section[1].length > 0).map(section => <Section section={section} />)}

        </main>
    )
};

export default Stylebook;