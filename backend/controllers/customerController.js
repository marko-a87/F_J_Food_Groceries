import { express } from "express";
import Customer from "../models/customerModel";
//Allows customer to enter register to website and provide private information
const registerCustomer = (req, res) => {
  const { username, password, email } = req.body;
};

//Allows customer to login to website by checking credentials against database
const loginCustomer = (req, res) => {
  const { username, password } = req.body;
};

//Allows customer to logout of website
const signoutCustomer = (req, res) => {};

export default { registerCustomer, loginCustomer, signoutCustomer };
