from database.db import Session
from models.invoices import Invoice
from datetime import datetime


    
def unpaid_invoices()-> list[Invoice] | None:
    with Session() as session:
        invoices= session.query(Invoice).filter(Invoice.is_paid == False).all()
        if invoices:
            return invoices
            
        else:
            return None
        

def cancel_unpaid_bookings() -> None:
    with Session() as session:    
        invoices= session.query(Invoice).filter(Invoice.is_paid == False).all()
        
        if invoices:
            for invoice in invoices:
                if invoice.end_date < datetime.utcnow():
                    invoice.is_cancelled = True

                    if invoice.booking:
                        invoice.booking.is_cancelled= True
            
            
            session.commit()

def pay_invoice(invoice: Invoice) -> None:
    if invoice:
        invoice.is_paid=True

        
    

        