import { useEffect, useState } from "react";
import { getHistory } from "../api/history";
import { useNavigate } from "react-router-dom";

export default function History() {
  const [scans, setScans] = useState([]);
  const [error, setError] = useState("");
  const navigate = useNavigate();

  useEffect(() => {
    loadHistory();
  }, []);

  async function loadHistory() {
    try {
      const data = await getHistory();
      setScans(data);
    } catch (err) {
      setError("Failed to load history");
    }
  }

  return (
    <div className="min-h-screen flex justify-center items-center bg-gradient-to-br from-indigo-200 to-purple-300 p-4">
      <div className="bg-white p-8 rounded-2xl shadow-2xl w-full max-w-5xl">

        {/* HEADER */}
        <div className="flex flex-wrap justify-between items-center mb-6 gap-3">
          <h2 className="text-3xl font-bold text-indigo-700 flex items-center gap-2">
            📜 Scan History Dashboard
          </h2>

          <button
            onClick={() => navigate("/")}
            className="bg-gradient-to-r from-blue-600 to-purple-600 text-white px-5 py-2 rounded-lg font-semibold shadow hover:scale-105 transition"
          >
            ⬅ Back to Scan
          </button>
        </div>

        {/* ERROR */}
        {error && (
          <div className="bg-red-100 text-red-700 p-3 rounded mb-4 text-center font-semibold">
            ❌ {error}
          </div>
        )}

        {/* NO DATA */}
        {scans.length === 0 ? (
          <p className="text-gray-500 text-center text-lg">No scans found.</p>
        ) : (
          <div className="overflow-x-auto">
            <table className="w-full border rounded-lg overflow-hidden">
              <thead className="bg-indigo-700 text-white">
                <tr>
                  <th className="p-3 text-left">URL</th>
                  <th className="p-3 text-center">Verdict</th>
                  <th className="p-3 text-center">Risk</th>
                  <th className="p-3 text-center">Date</th>
                </tr>
              </thead>

              <tbody className="divide-y">
                {scans.map((scan) => (
                  <tr
                    key={scan.id}
                    className="hover:bg-indigo-50 transition"
                  >
                    {/* URL */}
                    <td className="p-3 break-all text-blue-600 underline">
                      {scan.url}
                    </td>

                    {/* VERDICT */}
                    <td
                      className={`p-3 font-bold text-center ${
                        scan.verdict === "Safe"
                          ? "text-green-600"
                          : scan.verdict === "Suspicious"
                          ? "text-yellow-600"
                          : "text-red-600"
                      }`}
                    >
                      {scan.verdict || "N/A"}
                    </td>

                    {/* RISK */}
                    <td className="p-3 text-center font-semibold">
                      {scan.risk_score !== null && scan.risk_score !== undefined
                        ? `${scan.risk_score}%`
                        : "N/A"}
                    </td>

                    {/* DATE */}
                    <td className="p-3 text-center text-sm text-gray-600">
                      {scan.created_at
                        ? new Date(scan.created_at).toLocaleString()
                        : "N/A"}
                    </td>
                  </tr>
                ))}
              </tbody>
            </table>
          </div>
        )}

      </div>
    </div>
  );
}
