import React, { useEffect, useState } from "react";
import { fetchHistory } from "../api/scan";
import { Link } from "react-router-dom";

export default function HistoryPage() {
  const [items, setItems] = useState([]);
  const [error, setError] = useState("");

  useEffect(() => {
    async function load() {
      try {
        const data = await fetchHistory();
        setItems(data);
      } catch (err) {
        setError("Failed to load history");
        console.error(err);
      }
    }
    load();
  }, []);

  return (
    <div className="min-h-screen bg-gradient-to-br from-indigo-100 to-purple-200 p-6">
      <div className="max-w-4xl mx-auto bg-white rounded-xl shadow-lg p-6">

        <div className="flex justify-between items-center mb-6">
          <h1 className="text-2xl font-bold text-indigo-600">
            📜 Scan History Dashboard
          </h1>

          <Link
            to="/"
            className="bg-blue-600 text-white px-4 py-2 rounded hover:bg-blue-700 transition"
          >
            ⬅ Back to Scan
          </Link>
        </div>

        {error && (
          <div className="bg-red-100 text-red-700 p-3 rounded mb-4">
            {error}
          </div>
        )}

        {items.length === 0 && (
          <div className="text-gray-500 text-center">
            No scans found.
          </div>
        )}

        <div className="space-y-4">
          {items.map((item) => (
            <div
              key={item.id}
              className="border rounded-lg p-4 shadow-sm bg-gray-50"
            >
              <p className="text-sm text-gray-500">
                {new Date(item.created_at).toLocaleString()}
              </p>

              <p className="mt-1 font-medium">
                🔗 <span className="text-blue-600">{item.url}</span>
              </p>

              {item.result ? (
                <div className="mt-3 p-3 rounded bg-green-100 border border-green-300">
                  <p>
                    ✅ <b>Verdict:</b> {item.result.verdict}
                  </p>
                  <p>
                    ⚠️ <b>Risk:</b> {item.result.risk_score}%
                  </p>
                  <p>
                    📝 <b>Reason:</b> {item.result.reason}
                  </p>
                </div>
              ) : (
                <div className="mt-3 text-sm text-orange-600">
                  ⏳ Still processing...
                </div>
              )}
            </div>
          ))}
        </div>
      </div>
    </div>
  );
}
