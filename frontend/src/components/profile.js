import React from "react";
import photo from "../assets/images/editors/generic.jpg";

function Profile({editor}) {

    return (
        <figure>
            <img className="profile" src={photo} alt="Editor" />
            <figcaption>{editor}</figcaption>
        </figure>
    )
}

export default Profile;