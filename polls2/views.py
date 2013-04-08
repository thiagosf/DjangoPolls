# Create your views here.
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.core.urlresolvers import reverse

from polls2.models import Poll, Choice

def index(request):
    latest_poll_list = Poll.objects.all().order_by('-pub_date')[:5]
    context = {'latest_poll_list': latest_poll_list}
    return render(request, 'polls/index.html', context)

def detail(request, poll_id):
    poll = get_object_or_404(Poll, pk=poll_id)
    return render(request, 'polls/detail.html', {'poll': poll})

def results(request, poll_id):
    poll = get_object_or_404(Poll, pk=poll_id)

    choices = list(poll.choice_set.all())
    total_votes = sum(c.votes for c in choices)

    for choice in choices:
        vote = choice.votes
        vote_percentage = int(vote*100.0/total_votes)
        choice.percentage = vote_percentage

    return render(request, 'polls/results.html', {'poll': poll, 'total_votes': total_votes})

def vote(request, poll_id):
    p = get_object_or_404(Poll, pk=poll_id)
    try:
        selected_choice = p.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the poll voting form.
        return render(request, 'polls/detail.html', {
            'poll': p,
            'error_message': "Selecione uma alternativa para computar seu voto!",
            })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('polls2:results', args=(p.id,)))