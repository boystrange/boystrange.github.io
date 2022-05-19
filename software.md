---
layout: page
title: Software
---

<ul class="fa-ul compact">
  {% for item in site.data.software %}
	<li>
	  <i class="fa-li far fa-save"></i>
	  {% if item.href %}
		<a href="{{ item.href }}">{{ item.title }}</a>
	  {% else %}
		{{ item.title }}
	  {% endif %}
	  <br/>
	  {{ item.desc | markdownify | remove: '<p>' | remove: '</p>' }}
	</li>
  {% endfor %}
</ul>
