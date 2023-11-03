const notFound = (req, res, next) => {
  const error = new Error(`Not Found - ${req.originalUrl}`);
  if (error) {
    console.log(error);
    return res.status(404).json({ Error: `Not Found - ${req.originalUrl}` });
  }
  next(error);
};

export { notFound };
