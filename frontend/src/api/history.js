const API_BASE = import.meta.env.VITE_API_BASE;

export async function getHistory() {
  const res = await fetch(`${API_BASE}/history/`);

  if (!res.ok) {
    throw new Error("Failed to load history");
  }

  return await res.json();
}
