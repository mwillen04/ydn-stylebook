import React, { useState, useEffect } from "react";
import Profile from "../components/profile";

function About() {

    const [editors, setEditors] = useState([])

    useEffect(() => {
        
        fetch('/about')
          .then(response => response.json())
          .then(data => {
            setEditors(data.editors);
          })
          .catch(error => console.error('Error:', error));
    }, []);

    return (
        <main>
            <br />
            <h1>The Copy Desk</h1>

            <br />
            <div style={{margin: "0px 150px"}}>
                <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.</p>
                <p><b>Heel the Copy Desk!</b> Join our mailing list <a href="/">here</a>.</p>
                <p>Questions? Email <a href="mailto:michael.willen@yale.edu">michael.willen@yale.edu</a></p>

                <br />
                <div className="profiles">

                    {editors.map(editor => <Profile editor={editor} />)}

                </div>
            </div>
        </main>
    )
}

export default About;