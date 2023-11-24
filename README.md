# F_J_Food_Groceries

A program that allows customers to order or choose delivery.

# Project Structure

# Application
  -App.py
  
  This runs the driver code for the application
  
# Customer Interface
  -This is the presentation layer for the customers
  
  -When a user presses a button it passes control the next layer

# Authentication layer
  Classes:
  
    -Customer.py
    
    -System_UI.py
    
  Authenticates the customer based on customer information
  
  Passes control to the database layer

# Business_Logic 

  Classes:
  
    -Order.py
    
    -Product.py
    
    -Shopping_Cart.py
    
    -Category.py

# Data_mangement_security

  Classes:
  
    -Database.py
