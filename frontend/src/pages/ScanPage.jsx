import { useState } from "react";
import { createScan, getScanResult } from "../api/scan";
import { Link } from "react-router-dom";

export default function ScanPage() {
  const [url, setUrl] = useState("");
  const [loading, setLoading] = useState(false);
  const [result, setResult] = useState(null);
  const [error, setError] = useState("");

  async function handleScan() {
    if (!url.trim()) {
      setError("Please enter a valid URL");
      return;
    }

    try {
      setLoading(true);
      setError("");
      setResult(null);

      const scan = await createScan(url);

      let count = 0;
      const timer = setInterval(async () => {
        try {
          const res = await getScanResult(scan.id);

          // ✅ FIX: SUPPORT BOTH RESPONSE TYPES
          const finalResult = res.result ? res.result : res;

          setResult(finalResult);
          setLoading(false);
          clearInterval(timer);

        } catch {
          count++;
          if (count > 10) {
            setError("Scan timeout. Please try again.");
            setLoading(false);
            clearInterval(timer);
          }
        }
      }, 1200);

    } catch {
      setError("Backend not responding!");
      setLoading(false);
    }
  }

  return (
    <div className="min-h-screen flex justify-center items-center bg-gradient-to-br from-indigo-200 to-purple-300">
      <div className="bg-white p-8 rounded-2xl shadow-xl w-[380px]">

        <h1 className="text-3xl font-bold text-center text-indigo-700 mb-2">
          🔐 Phishing Detector
        </h1>
        <p className="text-center text-gray-500 mb-4">
          AI-powered website scanner
        </p>

        <input
          className="w-full border p-2 rounded mb-3 focus:ring-2 focus:ring-indigo-400"
          placeholder="Enter website URL"
          value={url}
          onChange={(e) => setUrl(e.target.value)}
        />

        <button
          onClick={handleScan}
          disabled={loading}
          className="w-full py-2 rounded bg-gradient-to-r from-blue-600 to-purple-600 text-white font-bold hover:opacity-90 disabled:opacity-60"
        >
          {loading ? "🔍 Scanning..." : "Scan Website"}
        </button>

        <Link
          to="/history"
          className="block text-center mt-4 text-blue-700 font-semibold hover:underline"
        >
          📜 View History
        </Link>

        {error && (
          <div className="mt-4 p-3 bg-red-100 text-red-700 rounded text-sm">
            ❌ {error}
          </div>
        )}

        {/* ✅ RESULT CARD */}
        {result && (
          <div
            className={`mt-4 p-4 rounded-lg border text-sm ${
              result.verdict === "Safe"
                ? "bg-green-100 border-green-500"
                : result.verdict === "Suspicious"
                ? "bg-yellow-100 border-yellow-500"
                : "bg-red-100 border-red-500"
            }`}
          >
            <p><b>Verdict:</b> {result.verdict}</p>
            <p><b>Risk:</b> {result.risk_score}%</p>
            <p><b>Reason:</b> {result.reason}</p>
          </div>
        )}

      </div>
    </div>
  );
}
