import express from "express";

const router = express.Router();

router.use("/admin", (req, res) => {
  res.send("This is the admin route");
});

export default router;
