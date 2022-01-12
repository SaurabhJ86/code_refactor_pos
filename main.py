from pos_system.order import Order
from pos_system.system import POSSystem

def main() -> None:
    #Create the POS System and setup Payment Processor
    system = POSSystem()
    system.setup_payment_processor("https://api.zoho.com/v2")


    #Create an order
    order = Order(12345,customer_name="Geralt Sharma",customer_address="309, Sector XC1, Noida",customer_zip_code="411XCV",customer_city="Noida",customer_country="India",customer_email_address="some@aol.com",customer_phone_number="9076131xcs")
    order.create_line_item("IPhone",1,92000)
    order.create_line_item("Homer Socks",5,200)
    order.create_line_item("Ball Pens",10,100)

    #register and process the order
    system.register_order(order)
    system.process_order(order)


if __name__ == "__main__":
    main()