const API_BASE = import.meta.env.VITE_API_BASE;

export async function getHistory() {
  const res = await fetch(`${API_BASE}/history/`);

  if (!res.ok) {
    const txt = await res.text();
    throw new Error(txt);
  }

  return await res.json();
}
