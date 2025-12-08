import { useEffect, useState } from "react";
import { fetchHistory } from "../api/scan";

export default function HistoryPage() {
  const [data, setData] = useState([]);

  useEffect(() => {
    fetchHistory().then(setData);
  }, []);

  return (
    <div className="p-10">
      <h1 className="text-3xl font-bold mb-4">Scan History</h1>

      <table className="w-full border">
        <thead>
          <tr>
            <th className="border p-2">URL</th>
            <th className="border p-2">Verdict</th>
            <th className="border p-2">Risk</th>
          </tr>
        </thead>
        <tbody>
          {data.map((s) => (
            <tr key={s.id}>
              <td className="border p-2">{s.url}</td>
              <td className="border p-2">{s.result?.verdict}</td>
              <td className="border p-2">{s.result?.risk_score}%</td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
}
