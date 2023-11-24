# F_J_Food_Groceries

A program that allows customers to order or choose delivery.

# Project Structure

# Application

  Classes:
  
    App.py
  
  This runs the driver code for the application.
  
# Customer Interface

  This is the presentation layer for the customers.
  
  When a user presses a button it passes control to the authentication layer.

# Authentication layer
  Classes:
  
    Customer.py
    
    System_UI.py
    
  Authenticates the customer based on credentials.
  
  Passes control to the database layer.
  
  Passes control the Business_Logic layer once authenticated.

# Business_Logic 

  Classes:
  
    Order.py
    
    Product.py
    
    Shopping_Cart.py
    
    Category.py

# Data_mangement_security

  Classes:
  
    Database.py

  Holds user data and secures it.
  
  Passes control back to authentication.
