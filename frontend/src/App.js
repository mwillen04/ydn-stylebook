import { BrowserRouter, Routes, Route } from "react-router-dom";
import Layout from "./pages/layout";
import Home from './pages/home';
import Top10 from "./pages/top10";
import Stylebook from "./pages/stylebook";
import Ask from "./pages/ask";
import About from "./pages/about";
import NoPage from "./pages/nopage";

function App() {
  return (
    <div className="App">
      <BrowserRouter>
        <Routes>
          <Route path="/" element={<Layout />}>
            <Route index element={<Home />} />
            <Route path="top10" element={<Top10 />} />
            <Route path="stylebook" element={<Stylebook />} />
            <Route path="ask" element={<Ask />} />
            <Route path="about" element={<About />} />
            <Route path="*" element={<NoPage />} />
          </Route>
        </Routes>
      </BrowserRouter>
    </div>
  );
}

export default App;
