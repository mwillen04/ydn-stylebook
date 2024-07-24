import React from "react";

function AskForm() {

    return (
        <form onSubmit={e => {e.preventDefault();}}>

            <input type="text" className="question" name="e" placeholder="Email" /><br />
            <input type="text" className="question" name="q" placeholder="Ask your question here..." /><br />
            <input className="question" type="submit" />

        </form>
    )
}

export default AskForm;