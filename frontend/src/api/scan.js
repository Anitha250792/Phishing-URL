const API_BASE =
  import.meta.env.VITE_API_BASE || "https://phishing-url-ypra.onrender.com/api";

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
