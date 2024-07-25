import React from "react";
import Entry from "./entry";

function Section({section}) {

    return (
        <section id={section[0]}>
            <br /><hr />
            <h2>{section[0]}</h2>
            <hr /><br />

            {section[1].map(entry => <Entry entry={entry}/>)}

            <p style={{textAlign : "center"}}>
                — <a href="#top" className="letters">^</a> —
            </p>
        </section>
    )
}

export default Section;