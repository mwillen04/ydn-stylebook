import React from "react";
import photo from "../assets/images/editors/generic.jpg";

function Profile({editor}) {

    return (
        <figure>
            <img className="profile" src={photo} alt="Editor" />
            <figcaption><b>{editor[0]}</b><br />{editor[1]}</figcaption>
        </figure>
    )
}

export default Profile;