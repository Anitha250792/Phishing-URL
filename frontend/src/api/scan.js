const API_BASE =
  import.meta.env.VITE_API_BASE || "http://127.0.0.1:8000/api";

// ✅ CREATE SCAN
export async function createScan(url) {
  const res = await fetch(`${API_BASE}/scan/`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ url }),
  });

  if (!res.ok) {
    const txt = await res.text();
    throw new Error(txt);
  }

  return await res.json();
}

// ✅ GET SINGLE SCAN RESULT
export async function getScanResult(scanId) {
  const res = await fetch(`${API_BASE}/scan/${scanId}/`);

  if (!res.ok) {
    throw new Error("Result not ready");
  }

  return await res.json();
}
