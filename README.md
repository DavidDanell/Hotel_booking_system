# Hotel Booking System

A command-line hotel management system built with SQLAlchemy and MySQL. Handles the full booking lifecycle: guest registration, availability search, room assignment with automatic extra-bed allocation, invoicing, and cancellations.

Built as an assignment for a course. The interface is in Swedish.

## What it does

**Booking menu**
- Register a new guest, with name and email format validation
- Search available rooms for a date range and party size
- Create a booking — the system excludes rooms already occupied in the requested window, filters by capacity, and derives the required number of extra beds from party size and bed type
- Bookings must start at least one day ahead

**Admin menu**
- Cancel a booking (allowed up to one day before check-in); cancelling also voids the invoice and flags a refund if already paid
- Register a payment against an outstanding invoice
- List cancelled bookings
- List active bookings with payment status

Unpaid bookings are swept automatically at startup.

## Architecture

```
├── models/           SQLAlchemy ORM models
│   ├── base.py       declarative base
│   ├── guest.py
│   ├── rooms.py
│   ├── bookings.py
│   ├── invoices.py
│   └── typings.py    Bed_type / Extra_beds enums
├── services/         business logic, kept out of the models
│   ├── guest_service.py
│   ├── room_service.py
│   ├── booking_service.py
│   ├── invoice_service.py
│   └── seeding.py
├── database/
│   └── db.py         engine and Session factory
├── alembic/          schema migrations
├── alembic.ini
└── main.py           CLI entry point
```

The separation matters here: `main.py` handles input and display only, `services/` owns the rules (availability, pricing, extra-bed logic), and `models/` describes the schema. Room and bed types are enums rather than strings, so invalid states are unrepresentable.

## Data model

- **Guest** — first name, last name, email
- **Room** — bed type (single/double), possible extra beds, price per night
- **Booking** — guest, room, check-in, check-out, party size, extra beds, cancellation flag
- **Invoice** — one per booking, total amount, paid and cancelled flags

Availability is computed with an overlap query — a room is taken if an active booking starts before your check-out and ends after your check-in.

## Running it

Requires Python 3.12+ (uses `datetime.UTC`) and a MySQL server.

```bash
pip install -r requirements.txt
```

Configure the database URL in `alembic.ini` and `database/db.py`, then create the schema:

```bash
alembic upgrade head
python main.py
```

On first run the system seeds 100 rooms and 50 guests so there's something to book against.

## Notes

Seeding runs on every startup. If you want a clean slate, `main.py` contains a commented-out block that truncates the tables and resets the auto-increment counters.