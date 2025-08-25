from django.core.mail import send_mail
from django.core.mail import EmailMessage
from django.shortcuts import render, redirect
from django.conf import settings

# Create your views here.
# def index_view(request):
#   return render(request, "index.html"
# def index_view(request):
#   if request.method == "POST":
#       full_name = request.POST.get("full_name")
#       email = request.POST.get("email")
#       phone = request.POST.get("phone")
#       company = request.POST.get("company")
#       product = request.POST.get("product")
#       quantity = request.POST.get("quantity")
#       notes = request.POST.get("notes")

#       subject = f"New Stock Inquiry from {full_name}"
#       message = f"""
#       You have received a new inquiry:

#       Full Name: {full_name}
#       Email: {email}
#       Phone: {phone}
#       Company: {company}
#       Product of Interest: {product}
#       Quantity Needed: {quantity}
#       Notes: {notes}
#       """

#       send_mail(
#           subject,
#           message,
#           settings.DEFAULT_FROM_EMAIL,  # sender (your cPanel email)
#           ["inquiry@skaalmeats.com"],   # recipient
#           fail_silently=False,
#       )

#       return render(request, "index.html", {"success": True})

#   return render(request, "index.html")


def index_view(request):
  if request.method == "POST":
      full_name = (request.POST.get("full_name") or "").strip()
      email = (request.POST.get("email") or "").strip()
      phone = (request.POST.get("phone") or "").strip()
      company = (request.POST.get("company") or "").strip()
      product = (request.POST.get("product") or "").strip()
      quantity = (request.POST.get("quantity") or "").strip()
      notes = (request.POST.get("notes") or "").strip()

      subject = f"New Stock Inquiry from {full_name}"
      message = f"""
      You have received a new inquiry:

      Full Name: {full_name}
      Email: {email}
      Phone: {phone}
      Company: {company}
      Product of Interest: {product}
      Quantity Needed: {quantity}
      Notes: {notes}
      """

      send_mail(
          subject,
          message,
          settings.DEFAULT_FROM_EMAIL,  # sender (your cPanel email)
          ["inquiry@skaalmeats.com"],   # recipient
          fail_silently=False,
      )

      # redirect with success flag + anchor
      return redirect("/?success=1#inquiry")

  success = request.GET.get("success") == "1"
  return render(request, "index.html", {"success": success})



def about_us_view(request):
  return render(request, "about.html")


# def contact_us_view(request):
#   return render(request, "contact.html")

def contact_us_view(request):
  success = False
  if request.method == "POST":
      name = request.POST.get("name")
      email = request.POST.get("email")
      message = request.POST.get("message")

      full_message = f"Name: {name}\nEmail: {email}\n\nMessage:\n{message}"

      send_mail(
          subject=f"New Contact Inquiry from {name}",
          message=full_message,
          from_email=settings.DEFAULT_FROM_EMAIL,
          recipient_list=["inquiry@skaalmeats.com"],
          fail_silently=False,
      )

      # redirect with anchor so browser jumps to the form section
      return redirect("/pages/contact-us/#reachout?success=1")

  success = request.GET.get("success") == "1"
  return render(request, "contact.html", {"success": success})


# def shop_view(request):
#   if request.method == "POST":
#     name = (request.POST.get("name") or "").strip()
#     email = (request.POST.get("email") or "").strip()
#     phone = (request.POST.get("phone") or "").strip()
#     company = (request.POST.get("company") or "").strip()
#     product = (request.POST.get("product") or "").strip()
#     quantity = (request.POST.get("quantity") or "").strip()
#     msg = (request.POST.get("message") or "").strip()

#     subject = f"New Contact/Booking from {name} — {product or 'No product selected'}"
#     body = (
#         "You received a new contact form submission:\n\n"
#         f"Name: {name}\n"
#         f"Email: {email}\n"
#         f"Phone: {phone}\n"
#         f"Company: {company}\n"
#         f"Product of Interest: {product}\n"
#         f"Quantity (KG): {quantity}\n\n"
#         f"Message:\n{msg}\n"
#     )

#     email_msg = EmailMessage(
#       subject=subject,
#       body=body,
#       from_email=settings.DEFAULT_FROM_EMAIL,
#       to=["sales@skaalmeats.com"],   # destination
#       reply_to=[email] if email else None,  # reply goes to the user
#     )
#     email_msg.send(fail_silently=False)

#     return render(request, "shop.html", {"success": True})
#   return render(request, "shop.html")


def shop_view(request):
    if request.method == "POST":
        name = (request.POST.get("name") or "").strip()
        email = (request.POST.get("email") or "").strip()
        phone = (request.POST.get("phone") or "").strip()
        company = (request.POST.get("company") or "").strip()
        product = (request.POST.get("product") or "").strip()
        quantity = (request.POST.get("quantity") or "").strip()
        msg = (request.POST.get("message") or "").strip()

        subject = f"New Contact/Booking from {name} — {product or 'No product selected'}"
        body = (
            "You received a new contact form submission:\n\n"
            f"Name: {name}\n"
            f"Email: {email}\n"
            f"Phone: {phone}\n"
            f"Company: {company}\n"
            f"Product of Interest: {product}\n"
            f"Quantity (KG): {quantity}\n\n"
            f"Message:\n{msg}\n"
        )

        email_msg = EmailMessage(
            subject=subject,
            body=body,
            from_email=settings.DEFAULT_FROM_EMAIL,
            to=["inquiry@skaalmeats.com"],
            reply_to=[email] if email else None,
        )
        email_msg.send(fail_silently=False)

        # redirect to same page with anchor + success flag
        return redirect("/pages/pricing/?success=1#bookings")

    success = request.GET.get("success") == "1"
    return render(request, "shop.html", {"success": success})


def more_info_view(request):
  content_id = request.GET.get("content", "1")  # Default to content 1 if missing
  return render(request, "more-info.html", {"content_id": content_id})


def error_404_view(request, exception=None):
  return render(request, "404.html", status=404)