import express from "express";

const router = express.Router();
router.use("/", (req, res) => {
  res.send("This is the user route");
});
export default router;
