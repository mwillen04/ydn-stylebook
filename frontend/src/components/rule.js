import React from "react";
import parse from 'html-react-parser';

function Rule({rule}) {
    return (
        <div>
            <li>{rule[0]}</li>

            {parse(rule[1])}
            <br /><br />
        </div>
    )
}

export default Rule;