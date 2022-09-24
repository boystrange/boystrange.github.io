---
layout: page
title: Teaching
---

<i class="fas fa-exclamation-circle"></i> Il **ricevimento studenti**
avviene **previo appuntamento** da prenotare usando <a href=""
onclick="Calendly.initPopupWidget({url:
'https://calendly.com/luca-padovani/ricevimento'});return
false;">questo servizio</a>.  Il ricevimento dell'insegnamento *x* è
**sospeso** nei tre giorni lavorativi precedenti un appello di *x*.

{% assign current_year = 'now' | date: "%Y" %}
{% for y in (2001..current_year) %}
  {% assign year = current_year | minus: y | plus: 2001 %}
  {% assign next = year | plus: 1 %}
  {% assign counter = 0 %}
  {% for course in site.data.courses %}
    {% if course.year == year %}
	  {% assign counter = counter | plus: 1 %}
	{% endif %}
  {% endfor %}
  {% if counter != 0 %}

  <h2>A.A. {{ year }}-{{ next }}</h2>
  <ul class="fa-ul compact courses">
	{% for course in site.data.courses %}
	{% if course.year == year %}
	  <li>
		<i class="fa-li fas fa-graduation-cap"></i>
		{{ course.code }},
		{% case course.kind %}
		  {% when "unito-triennale" %}
			<a href="http://laurea.educ.di.unito.it/index.php/offerta-formativa/insegnamenti/elenco-completo/elenco-completo/scheda-insegnamento?cod={{ course.code }}&year={{ course.year }}">{{ course.title }}</a>,
		  {% when "unito-matematica" %}
			<a href="{{ course.url }}">{{ course.title }}</a>,
		  {% else %}
			{{ course.title }},
		{% endcase %}
		{% if course.info %}
		  {{ course.info }}
		{% endif %}
	  </li>
	{% endif %}
	{% endfor %}
  </ul>
  {% endif %}
{% endfor %}
