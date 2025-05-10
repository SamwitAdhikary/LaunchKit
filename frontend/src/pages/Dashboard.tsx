import React, { useEffect, useState } from "react";
import api from "../api/client";
import CommonButton from "../components/CommonButton";

export default function Dashboard() {
  const [status, setStatus] = useState<string>("loading");

  useEffect(() => {
    api.get("/health")
      .then((res) => setStatus(res.data.status))
      .catch(() => setStatus("error"));
  }, []);

  return (
    <div style={{ padding: "2rem" }}>
      <h1>🚀 LaunchKit Dashboard</h1>
      <p>
        API Health: <strong>{status}</strong>
      </p>
      <CommonButton label="Refresh" onClick={() => window.location.reload()} />
    </div>
  );
}
