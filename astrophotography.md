---
layout: page
title: Astrophotography Logbook
---

I like to think of myself as an amateur astrophotographer and this
page provides a fairly complete diary of the photos I took.  For
each target, photos are listed in reverse chronological order, with
more recent (and usually better) photos occurring first. The
qualities of photos varies a lot. My experience in taking and
processing astrophotos is still limited and, in several cases, I've
used inadequate equipment. This diary is a way for me to quickly
glance at the progress I (hopefully) make.

Thumbnails are not clickable and high resolution versions of the
photos are not available from this site.

<div class="frow">
	{% for section in site.data.astro %}
	<!-- <div class="col-md-1-4"> -->
	<!-- 	<h3>{{ section.title }}</h3> -->
	<!-- </div> -->
    {% assign targets = section.targets | sort: "date" | reverse %}
	{% for target in targets %}
	<div class="pr-5 col-md-1-3">
	  <div class="astro-container">
		<img class="rounded shadow-dark" src='/assets/astro/{{ section.key }}-{{ target.date }}.small.jpg' alt="{{ section.key }}" width="100%"/>
		{%- if target.title -%}
		<div class="astro-title">{{ target.title }}</div>
		{%- else -%}
		<div class="astro-title">{{ section.title }}</div>
		{%- endif -%}
		<div class="astro-date">{{ target.date | date: "%b %d, %Y" }}</div>
	  </div>
	</div>
	{% endfor %}
	{% endfor %}
</div>
