const API_BASE = "https://phishing-url-ypra.onrender.com/api";

export async function getHistory() {
  const res = await fetch(`${API_BASE}/history/?format=json`);

  if (!res.ok) {
    const txt = await res.text();
    throw new Error(txt);
  }

  return res.json();
}
