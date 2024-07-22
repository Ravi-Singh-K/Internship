Book_Status = (
    ('Available', 'Available'),
    ('Not Available', 'Not Available')
)

AVAILABLE = 'Available'
NOT_AVAILABLE = 'Not Available'
BOOK_CHOICES = (
    (AVAILABLE, AVAILABLE),
    (NOT_AVAILABLE, NOT_AVAILABLE)
)


RETURNED = 'Returned'
PENDING = 'Pending'
RETURNED_STATUS_CHOICES = (
    (RETURNED, RETURNED),
    (PENDING, PENDING)
)

Returned_Status = [
    ('Returned', 'Returned'),
    ('Pending', 'Pending')
]

# def auto_printing_func():
#     print("Hello world")


GOOD ='Good'
BAD = 'Bad'

RATING_CHOICES = (
    (GOOD, GOOD),
    (BAD, BAD)
)