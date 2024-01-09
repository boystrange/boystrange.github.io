---
layout: page
title: Astrophotography Logbook
---

I like to think of myself as an amateur astrophotographer and this
page provides a selection of the photos I took. Targets are sorted
by their inverse (maximum) distance from Earth, with more distant
objects occurring first. For each target, photos are listed in
reverse chronological order, with more recent (and usually better)
photos occurring first. The quality of photos varies a lot. My
experience in taking and processing astrophotos is still limited
and, in several cases, I've used inadequate equipment. This diary is
a way for me to quickly glance at the progress I (hopefully) make.

Thumbnails are not clickable and high resolution versions of the
photos are not available from this site.

<div class="frow">
	{% assign targets = site.data.astro | sort: "distance" | reverse %}
	{% for target in targets %}
	<!-- <div class="col-md-1-4"> -->
	<!-- 	<h3>{{ section.title }}</h3> -->
	<!-- </div> -->
    {% assign photos = target.pictures | sort: "date" | reverse %}
	{% for photo in photos %}
	{% unless photo.hidden %}
	<div class="pr-5 col-md-1-3">
	  <div class="astro-container">
		<img class="rounded shadow-dark" src='/assets/astro/{{ target.key }}-{{ photo.date }}.small.jpg' alt="{{ section.key }}" width="100%"/>
		{%- if photo.title -%}
		<div class="astro-title">{{ photo.title }}</div>
		{%- else -%}
		<div class="astro-title">{{ target.title }}</div>
		{%- endif -%}
		<div class="astro-date">{{ photo.date | date: "%b %d, %Y" }}</div>
		<div class="astro-distance">
			{% if target.distance >= 1000000 %}
				{{ target.distance | divided_by: 1000000.0 | round: 2 | append: " Mly" | replace: ".0 ", " " }}
			{% elsif target.distance >= 1000 %}
				{{ target.distance | divided_by: 1000.0 | round: 2 | append: " kly " | replace: ".0 ", " " }}
			{% elsif target.distance >= 1 %}
				{{ target.distance | round: 2 | append: " ly" }}
			{% else %}
				{{ target.distance | times: 63240 | round: 2 | append: " AU" | replace: ".0 ", " " }}
			{% endif %}
		</div>
	  </div>
	</div>
	{% endunless %}
	{% endfor %}
	{% endfor %}
</div>
