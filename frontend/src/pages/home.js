import React from "react";
import { QueryProvider } from "../contexts/QueryContext";
import Searchbar from "../components/searchbar";
import Results from "../components/results";

function Home() {

    return (
        <main>

            <br />
            <h1>STYLEBOOK OF THE YALE DAILY NEWS</h1>

            <QueryProvider>
                <Searchbar />

                <Results />
            </QueryProvider>

        </main>
    )
};

export default Home;
