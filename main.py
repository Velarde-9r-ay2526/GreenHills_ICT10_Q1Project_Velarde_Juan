from pyscript import document, display

# SKU Generator
def generate_sku(event):
    document.getElementById("sku_output").innerHTML = ""
    
    category = document.getElementById("category").value
    prod_name = document.getElementById("prod_name").value
    stock_qty = document.getElementById("stock_qty").value
    
    # Process string using basic methods
    clean_name = prod_name.strip().upper().replace("'", "").replace(" ", "")
    name_code = clean_name[:3]
    qty_code = str(stock_qty).strip()
    
    # Combine strings
    sku = category + "-" + name_code + "-" + qty_code
    
    display(f"Generated SKU: {sku}", target="sku_output")

#  Receipt Generator
def create_order(event):
    document.getElementById("receipt_output").innerHTML = ""
    
    price = float(document.getElementById("coffee").value)
    qty = float(document.getElementById("quantity").value)
    
    total = price * qty
    summary = "Total Amount: ₱" + str(total)
    
    display(summary, target="receipt_output")