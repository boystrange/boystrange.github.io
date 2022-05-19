---
layout: page
title:  Projects
---

{% assign current_year = 'now' | date: "%Y" | plus: 0 %}

<ul class="fa-ul compact">
  {% for project in site.data.projects %}
	<li>
	  {% if project.start <= current_year and current_year <= project.end %}
		<i class="fa-li fas fa-handshake"></i>
	  {% else %}
		<i class="fa-li far fa-handshake"></i>
	  {% endif %}
	  <a href="{{ project.href }}">{{ project.title }}</a>
	  <br/>
	  {{ project.code }},
	  {{ project.roles | markdownify | remove: '<p>' | remove: '</p>' }}
	</li>
  {% endfor %}
</ul>
