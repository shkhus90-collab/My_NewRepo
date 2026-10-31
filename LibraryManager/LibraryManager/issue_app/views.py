from django.shortcuts import render,redirect
from .models import IssuedBook
# Create your views here.

def issue_book(req):
    #Step 1: show the form, and keep the submitted data in the session.
    if req.method == 'POST':
        req.session['issue_data'] = {                #Session = temporary box that carries data between pages.
            'student_roll_number': req.POST.get('student_roll_number'),
            'library_card_number': req.POST.get('library_card_number'),
            'book_title': req.POST.get('book_title'),
            'author_name': req.POST.get('author_name'),
            'issue_date': req.POST.get('issue_date'),
        }
        """
        Each line copies one form field into the slip. The left side is the label ('book_title').
        The right side reads what the user typed in the input with that name.
        """

        return redirect('issue_confirmation') #The slip is ready, so send the user to the confirmation page.

    return render(req, 'issue_app/issue_book.html') #This line runs only when it is not POST, so it shows the empty form.


def issue_confirmation(req):
    #Step 2: show the saved details; save to the database on Confirm.
    data = req.session.get('issue_data')

    # If there is nothing in the session, the user skipped step 1
    if not data:
        return redirect('issue_book')

    if req.method == 'POST':
        IssuedBook.objects.create(
          student_roll_number=data['student_roll_number'],
          library_card_number=data['library_card_number'],
          book_title=data['book_title'],
          author_name=data['author_name'],
          issue_date=data['issue_date'],
        )
        req.session['last_title'] = data['book_title'] #Writes the book title on a small new note,so the success page can show it later.
        del req.session['issue_data']      # clear the box
        return redirect('issue_success')

    return render(req, 'issue_app/issue_confirmation.html', data)


def issue_success(req):
    """Step 3: show the result."""
    title = req.session.pop('last_title', None)
    return render(req, 'issue_app/issue_success.html', {'book_title': title})


