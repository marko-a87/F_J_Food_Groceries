import mongoose from "mongoose";

//Creates a customer model using Schema
const customerSchema = new mongoose.Schema({
  username: {
    type: String,
    required: true,
  },
  password: {
    type: String,
    required: true,
  },

  email: {
    type: String,
    required: true,
  },
});

//Creates a customer model
const Customer = mongoose.model("Customer", customerSchema);

//Makes the model available to all other files to be imported
export default Customer;
