import { Routes, Route } from "react-router-dom";
import ScanPage from "./pages/ScanPage";
import HistoryPage from "./pages/HistoryPage";

export default function App() {
  return (
    <Routes>
      <Route path="/" element={<ScanPage />} />
      <Route path="/history" element={<HistoryPage />} />
    </Routes>
  );
}
