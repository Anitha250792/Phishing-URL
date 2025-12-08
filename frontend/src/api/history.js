const API_BASE =
  import.meta.env.VITE_API_BASE || "http://127.0.0.1:8000/api";

export async function getHistory() {
  const res = await fetch(`${API_BASE}/history/?format=json`);

  if (!res.ok) {
    throw new Error("Failed to load history");
  }

  return await res.json();
}
