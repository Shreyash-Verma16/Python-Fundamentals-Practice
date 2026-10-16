message = "Customer C-104 contacted us. Verify C-104 before refunding."
customer_id = "C-104"

redacted_message = message.replace(customer_id, "[REDACTED]")

print(redacted_message)