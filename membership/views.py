from django.shortcuts import render, redirect, get_object_or_404
from .forms import MemberForm, RejectionForm
from django.contrib.auth.decorators import login_required, user_passes_test
from .models import Member
# Create your views here.


def register_member(request):
    if request.method == 'POST':
        form = MemberForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('registration_success')
    else:
        form = MemberForm()
    return render(request, 'membership/htmlfiles/register.html', {'form': form})


def registration_success(request):
    return render(request, 'membership/htmlfiles/success.html')


def is_officer(user):
    return user.is_staff or user.groups.filter(name='Officer').exists()


@login_required
@user_passes_test(is_officer)
def pending_members(request):
    members = Member.objects.filter(approved=False)
    return render(request, 'membership/htmlfiles/pending_list.html', {'members': members})


@login_required
@user_passes_test(is_officer)
def approve_member(request, member_id):
    member = get_object_or_404(Member, id=member_id)
    member.approve(request.user)
    return redirect('pending_members')


def approved_members(request):
    life_members = Member.objects.filter(approved=True, membership_type='Life')
    ordinary_members = Member.objects.filter(
        approved=True, membership_type='Ordinary')
    return render(request, 'membership/htmlfiles/approved_members.html', {
        'life_members': life_members,
        'ordinary_members': ordinary_members,
    })


@login_required
@user_passes_test(is_officer)
def reject_member(request, member_id):
    member = get_object_or_404(Member, id=member_id)
    if request.method == 'POST':
        form = RejectionForm(request.POST)
        if form.is_valid():
            member.reject(form.cleaned_data['reason'])
            return redirect('pending_members')
    else:
        form = RejectionForm()
    return render(request, 'membership/htmlfiles/reject_member.html', {'form': form, 'member': member})
