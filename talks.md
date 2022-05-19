---
layout: page
title: Talks
---

<div class="frow gutters">
  {% for item in site.data.talks %}
  {% unless item.hidden == true %}
  <div class="col-md-1-3">
	<a href="/assets/talks/{{ item.file }}">
	  <img class="rounded shadow-light" src='/assets/talks/{{ item.file | replace: ".pdf", ".png" }}' alt="{{ item.title }}" width="100%"/>
	</a>
	<br/>
	{% assign flag = site.data.flags[item.country] %}
	<span class="shadowed-text">{{ flag }}</span>
	<span class="small-label">
	  {{ item.city }},
	  {% if item.venue %}{{ item.venue }}{% endif %}
	  {{ item.year }}
	</span>
  </div>
  {% endunless %}
  {% endfor %}
  {% assign rest = site.data.talks.size | modulo: 4 %}
  {% assign a = 4 | minus: rest | modulo: 4 %}
  {% for i in (1..a) %}
	<div class="is-col is-25"></div>
  {% endfor %}
</div>
