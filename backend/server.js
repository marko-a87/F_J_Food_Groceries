import express from "express";
import dotenv from "dotenv";
import userRoutes from ".//routes/userRoutes.js";
import adminRoutes from "../backend/routes/adminRoutes.js";
import { connectDB } from "./database/db.js";
import { notFound } from "./middleware/errorHandler.js";

//Loads the .env file(.env stores sensitive informative)
dotenv.config();

//Creates an express application
const app = express();

app.get("/", (req, res) => {
  res.send("Hello World");
});

//Connect to the database
connectDB();

//Uses userRoutes from routes folder
app.use("/", userRoutes);
app.use("/", adminRoutes);
app.use(notFound);
//Sets the Port
const PORT = process.env.PORT || 3000;

//Listens for a port
app.listen(PORT, () =>
  console.log(`Server listening on http://localhost:${PORT}`)
);
