import React, { createContext, useState } from 'react';

const QueryContext = createContext({query: {q: "", t: "keyword", f: 0}, setQuery: () => {}});

function QueryProvider({children}) {
    const [query, setQuery] = useState({q: "", t: "keyword", f: 0});

    return (
        <QueryContext.Provider value={{query, setQuery}}>
            {children}
        </QueryContext.Provider>
    )
}

export {QueryContext, QueryProvider}
