from flask import Flask, render_template, request
from model.entity import *
from controller import *

app = Flask(__name__,static_folder="view/assets", template_folder="view")


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/user", methods=["GET", "POST"])
def users():
    if request.method == "POST":
        UserController.save(
            request.form.get("name"),
            request.form.get("family"),
            request.form.get("birth_date"),
            request.form.get("phone"),
            request.form.get("email"),
            request.form.get("address"),
            request.form.get("role")
        )

    return render_template("user.html",user_list=UserController.find_all())


@app.route("/shipping", methods=["GET", "POST"])
def shippings():
    if request.method == "POST":
        ShippingController.save(
            request.form.get("id"),
            request.form.get("recipient_name"),
            request.form.get("address"),
            request.form.get("city"),
            request.form.get("postalcode"),
        )

    return render_template("shipping.html")



@app.route("/order", methods=["GET", "POST"])
def orders():
    if request.method == "POST":
        OrderController.save(
            request.form.get("order_type"),
            request.form.get("order_status"),
            request.form.get("total_cost"),
            request.form.get("customer_id"),
            request.form.get("shipping_id"),

        )

    return render_template("order.html")




if __name__ == "__main__":
    app.run(debug=True)
