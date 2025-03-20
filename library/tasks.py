from celery import shared_task
from django.core.mail import send_mail
from django.conf import settings
from django.utils import timezone
from .models import Loan


@shared_task
def send_loan_notification(loan_id):
    try:
        loan = Loan.objects.get(id=loan_id)
        member_email = loan.member.user.email
        book_title = loan.book.title
        send_mail(
            subject="Book Loaned Successfully",
            message=f'Hello {loan.member.user.username},\n\nYou have successfully loaned "{book_title}".\nPlease return it by {loan.due_date}.',
            from_email=settings.DEFAULT_FROM_EMAIL,
            recipient_list=[member_email],
            fail_silently=False,
        )
    except Loan.DoesNotExist:
        pass


@shared_task
def check_overdue_loans():
    today = timezone.now().date()
    overdue_loans = Loan.objects.filter(
        is_returned=False, due_date__lt=today
    ).select_related("member__user", "book")

    for loan in overdue_loans:
        member_email = loan.member.user.email
        book_title = loan.book.title
        days_overdue = (today - loan.due_date).days

        send_mail(
            subject="Overdue Book Notification",
            message=f'Hello {loan.member.user.username},\n\nThe book "{book_title}" is overdue by {days_overdue} days.\nPlease return it as soon as possible.',
            from_email=settings.DEFAULT_FROM_EMAIL,
            recipient_list=[member_email],
            fail_silently=False,
        )

    return f"Sent {overdue_loans.count()} overdue notifications"
