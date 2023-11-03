import mongoose from "mongoose";

//Creates a product model using Schema
const productSchema = new mongoose.Schema({
  name: {
    type: String,
    required: true,
  },
  stock: {
    type: Number,
    required: true,
  },
  price: {
    type: Number,
    required: true,
  },
  quantity: {
    type: Number,
    required: true,
  },
});

//Creates a model for the product using the schema
const Product = mongoose.model("Product", productSchema);

//Makes the product model available to all the other files to be imported
export default Product;
