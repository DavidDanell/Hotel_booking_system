from database.db import Session
from models.invoices import Invoice


with Session() as session:
    
    def unpaid_invoices()-> list[Invoice] | None:
        invoice= session.query(Invoice).filter(Invoice.is_paid == False).all()
        if invoice:
            return invoice
        
        else:
            return None
        

    def cancel_unpaid_bookings(unpaid= unpaid_invoices()) -> None:
        ...
    

        