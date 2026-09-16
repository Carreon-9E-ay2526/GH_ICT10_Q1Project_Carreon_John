#Receipt Generator
from pyscript import display, document


def create_order(e):
    item1 = document.getElementById("item1").checked
    item1_price = float(document.getElementById("item1").value)
    item2 = document.getElementById("item2").checked
    item2_price = float(document.getElementById("item2").value)
    item3 = document.getElementById("item3").checked
    item3_price = float(document.getElementById("item3").value)
    item4 = document.getElementById("item4").checked
    item4_price = float(document.getElementById("item4").value)
    item5 = document.getElementById("item5").checked
    item5_price = float(document.getElementById("item5").value)

    subtotal = (item1 * item1_price) + (item2 * item2_price) + (item3 * item3_price) + (item4 * item4_price) + (item5 * item5_price)


    document.getElementById("showsubtotal").innerHTML = ""

    display("Subtotal: ₱" + str(subtotal), target="showsubtotal")

    tax = subtotal * 0.12

    document.getElementById("showtax").innerHTML = ""

    display("Tax: ₱" + str(tax), target="showtax")

    total = subtotal + tax

    document.getElementById("showtotal").innerHTML = ""

    display("Total: ₱" + str(total), target="showtotal")

def create_sku(e):
    Category1 = document.getElementById("category").value
    Product1 = document.getElementById("product").value
    Stock1 = document.getElementById("stock").value

    SKU = Category1[0:2] + "-" + Product1[0:3] + "-" + Stock1

    document.getElementById("output").innerHTML = ""

    display(SKU, target="output")