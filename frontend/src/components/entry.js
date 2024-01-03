import React from "react";
import parse from 'html-react-parser';

function Entry({entry}) {
    return (
        <table className="entry" id={entry[0]}>
            <tbody>
                <tr>
                    <td className="term"><b>{entry[0]}</b></td>
                    <td>|</td>
                    <td className="definition">
                        {parse(entry[1])}
                    </td>
                </tr>
            </tbody>
        </table>
    )
}

export default Entry;