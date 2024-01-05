import React, { useContext } from "react";
import { QueryContext } from "../contexts/QueryContext";

function Searchbar() {
    const { query, setQuery } = useContext(QueryContext);

    // update query if user changes an input value
    const handleChange = (event) => {
        const name = event.target.name;
        let value;
        
        if (name === "f") {
            value = (event.target.checked ? 1 : 0);
        }
        else {
            value = event.target.value;
        }
        
        console.log(name, " : ", value);
        setQuery(values => ({...values, [name]: value}))
    }

    return (
        <form className="search" onSubmit={e => {e.preventDefault();}}>

            <select name="t" id="searchtype" value={query.t} onChange={handleChange}>
                <option className="dropdown" value="keyword">Keyword</option>
                <option className="dropdown" value="term">Term</option>
                <option className="dropdown" value="entry">Entry</option>
            </select>

            <input type="text" id="keyword" name="q" className="searchbar" 
                   onInput={handleChange} placeholder="Search the Stylebook" autoComplete="off" />

            <div className="check" title="Match full words only" onChange={handleChange}>
                <input type="checkbox" id="full" name="f" />
                <label className="checkmark" htmlFor="full">✔</label>
            </div>

        </form>
    )
}

export default Searchbar;