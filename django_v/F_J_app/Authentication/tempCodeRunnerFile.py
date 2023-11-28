auth = Auth()
auth.register()
c = Customer(
    name=auth.name,
    username=auth.user_name,
    password=auth.password,
    email_address=auth.email_address,
)
c.save()