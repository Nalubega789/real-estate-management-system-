from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required  # ADD THIS IMPORT
from .models import Agent


def agent_list(request):
    agents = Agent.objects.filter(is_active=True)
    return render(request, 'agent_list.html', {'agents': agents})


def agent_detail(request, agent_id):
    agent = get_object_or_404(Agent, id=agent_id)
    return render(request, 'detail.html', {'agent': agent})


def contact_agent(request, agent_id):
    agent = get_object_or_404(Agent, id=agent_id)

    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')

        if name and email and message:
            messages.success(request, f'Message sent to {agent.user.username} successfully!')
            return redirect('agent_detail', agent_id=agent.id)

    return render(request, 'contact.html', {'agent': agent})


# ADD THESE NEW VIEWS BELOW YOUR EXISTING ONES

@login_required
def manage_agent_profile(request):
    """Allow agents to manage their own profile"""
    try:
        agent = Agent.objects.get(user=request.user)
    except Agent.DoesNotExist:
        messages.error(request, "You are not registered as an agent.")
        return redirect('agent_list')

    if request.method == 'POST':
        # Update agent profile
        agent.phone = request.POST.get('phone', agent.phone)
        agent.email = request.POST.get('email', agent.email)
        agent.bio = request.POST.get('bio', agent.bio)
        agent.specialization = request.POST.get('specialization', agent.specialization)
        agent.years_experience = request.POST.get('years_experience', agent.years_experience)
        agent.license_number = request.POST.get('license_number', agent.license_number)
        agent.save()
        messages.success(request, "Profile updated successfully!")
        return redirect('manage_agent_profile')

    return render(request, 'Agent/manage_profile.html', {'agent': agent})


@login_required
def agent_dashboard(request):
    """Agent dashboard showing their properties and stats"""
    try:
        agent = Agent.objects.get(user=request.user)
        agent_properties = agent.apartments.all()  # This will show properties assigned to this agent
        return render(request, 'Agent/agent_dashboard.html', {
            'agent': agent,
            'properties': agent_properties
        })
    except Agent.DoesNotExist:
        messages.error(request, "You are not registered as an agent.")
        return redirect('agent_list')