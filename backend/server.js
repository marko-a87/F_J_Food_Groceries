import express from "express";
import dotenv from "dotenv";

dotenv.config();
const app = express();

app.get("/", (res, req) => {
  res.send("Hello World");
});
const PORT = process.env.PORT || 3000;
app.listen(PORT, () =>
  console.log(`Server listening on http://localhost:${PORT}`)
);
