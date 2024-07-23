import React, { useState, useEffect, useContext } from "react";
import { QueryContext } from "../contexts/QueryContext";
import DefaultHome from "./home_default";
import Entry from "./entry";

function Results() {

    const { query } = useContext(QueryContext);
    const [results, setResults] = useState([]);

    // get list of search results from backend
    useEffect(() => {

        // setup link
        let url = '/search?t=' + encodeURIComponent(query.t) + '&f=' + encodeURIComponent(query.f) + '&q=' + encodeURIComponent(query.q);
        console.log(url);
        
        // fetch data from server
        fetch(url)
          .then(response => response.json())
          .then(data => {
            console.log('# of Results: ', data.results.length);
            setResults(data.results);
          })
          .catch(error => console.error('Error:', error));
    }, [query]);

    // return base page if results is empty
    if (results.length === 0) {
        return (
            <DefaultHome />
        )
    };

    // return formatted results
    return (
        <div id="results">

            {results.map(result => <Entry entry={result}/>)}
            <br /><br />

        </div>
    )

}

export default Results;