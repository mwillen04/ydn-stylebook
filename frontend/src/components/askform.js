import React from "react";

function AskForm() {

    return (
        <form onSubmit={e => {e.preventDefault();}}>

            <input type="text" className="ask email" name="e" placeholder="Email" /><br />
            <textarea type="text" className="ask question" name="q" placeholder="Ask your question here..." /><br />
            <input className="ask submission" type="submit" />

        </form>
    )
}

export default AskForm;