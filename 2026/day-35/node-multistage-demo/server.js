const express = require("express");
const app = express();

app.get("/", (req, res) => {
  res.send("<h1>Multi-Stage Builds</h1><p>Simple Node.js app to practice Docker multi-stage builds.</p>");
});

app.listen(3000, () => console.log("Running on port 3000"));
