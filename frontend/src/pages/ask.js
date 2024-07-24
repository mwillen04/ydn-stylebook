import React from "react";
import AskForm from "../components/askform";

function Ask() {
    return (
        <main>
            <br />
            <h1>Ask the Editors!</h1>
            <br />

            <div style={{margin: "0px 150px"}}>
                
                <p>Have a question and can't find an answer in the Stylebook? Submit a question and we'll get back to you as soon as we can!</p>

                <AskForm />

                <h3>Recent Questions</h3>

                <p><i>Q: TBA!</i></p>

                <p><b>A: TBA!</b></p>

            </div>
        </main>
    )
}

export default Ask;