import { BrowserRouter, Routes, Route } from "react-router-dom";
import Layout from "./pages/layout";
import Home from './pages/home';
import Stylebook from "./pages/stylebook";
import Edits from "./pages/edits";
import Staff from "./pages/staff";
import NoPage from "./pages/nopage";

function App() {
  return (
    <div className="App">
      <BrowserRouter>
        <Routes>
          <Route path="/" element={<Layout />}>
            <Route index element={<Home />} />
            {/* <Route path="top10" element={<Top10 />} /> */}
            <Route path="stylebook" element={<Stylebook />} />
            <Route path="edits" element={<Edits />} />
            <Route path="staff" element={<Staff />} />
            <Route path="*" element={<NoPage />} />
          </Route>
        </Routes>
      </BrowserRouter>
    </div>
  );
}

export default App;
