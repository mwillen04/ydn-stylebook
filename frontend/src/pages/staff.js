import React, { useState, useEffect } from "react";
import Profile from "../components/profile";

function Staff() {

    const [editors, setEditors] = useState([])

    useEffect(() => {
        
        fetch('/staff')
          .then(response => response.json())
          .then(data => {
            setEditors(data.editors);
          })
          .catch(error => console.error('Error:', error));
    }, []);

    return (
        <main>
            <br />
            <h1>Copy Desk Editors</h1>

            <div className="profiles">

                {editors.map(editor => <Profile editor={editor} />)}

            </div>
        </main>
    )
}

export default Staff