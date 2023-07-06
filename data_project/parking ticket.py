import billing_machine_api
import payment_gateway_api
import database_api

def generate_ticket(parking_slot_number):
    ticket_number = billing_machine_api.generate_ticket(parking_slot_number)
    start_time = get_current_time()
    end_time = None
    amount_charged = None
    
    payment_gateway_api.process_payment(amount_charged)
    
    database_api.store_ticket_info(ticket_number, parking_slot_number, start_time, end_time, amount_charged)
    
    return ticket_number
    
def pay_parking_fee(ticket_number):
    ticket_info = database_api.get_ticket_info(ticket_number)
    amount_charged = ticket_info['amount_charged']
    
    payment_gateway_api.process_payment(amount_charged)
    
    database_api.update_ticket_info(ticket_number, end_time=get_current_time())
