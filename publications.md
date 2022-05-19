---
layout: page
title: Publications
---

{% assign current_year = 'now' | date: "%Y" %}
{% assign current_year = 2022 %}
{% for y in (2001..current_year) %}
{% assign year = current_year | minus: y | plus: 2001 %}
<h2>{{ year }}</h2>

<ul class="fa-ul">
{% for entry in site.data.bibliography %}
{% assign entryyear = entry.issued.date-parts[0][0] | plus: 0 %}
{% if entryyear == year %}
  <li>
{% case entry.type %}
  {% when "article-journal" %}
    <i class="fa-li fas fa-file-alt type"></i>
  {% when "book" %}
    <i class="fa-li fas fa-book type"></i>
  {% when "paper-conference" %}
    <i class="fa-li far fa-file-alt type"></i>
  {% when "chapter" %}
    <i class="fa-li fas fa-file type"></i>
  {% else %}
    <i class="fa-li fas fa-question-circle type"></i>
{% endcase %}

<span id="{{ entry.id }}">
  {% if entry.author %}
    {% for person in entry.author %}
      {{ person.given }} {{ person.family }},
    {% endfor %}
  {% elsif entry.editor %}
    {% for person in entry.editor %}
      {{ person.given }} {{ person.family }},
    {% endfor %}
  {% endif %}
</span>

<strong>{{ entry.title }}</strong>,

{% if entry.container-title %}
  <em>{{ entry.container-title }}</em>,
{% endif %}

{% if entry.page %}
  pages {{ entry.page }},
{% endif %}

{{ entryyear }}.

{% assign extra = site.data.bibliography_extra[entry.id] %}

  <div class="frow inline">
{% if entry.DOI %}
    <a class="btn" type="button" href="http://dx.doi.org/{{ entry.DOI }}">doi></a>
{% endif %}

{% if extra.html %}
    <a class="btn" type="button" href="{{ extra.html }}">.html</a>
{% endif %}

{% if extra.pdf %}
    <a class="btn" type="button" href="{{ extra.pdf }}">.pdf</a>
{% endif %}

{% if extra.preprint %}
    <a class="btn" type="button" href="{{ extra.preprint }}">.pdf (preprint)</a>
{% endif %}

{% if extra.long %}
    <a class="btn" type="button" href="{{ extra.long }}">.pdf (long version)</a>
{% endif %}

{% if extra.slides %}
    <a class="btn" type="button" href="assets/talks/{{ extra.slides }}.pdf">.pdf (slides)</a>
{% endif %}

{% if entry.abstract %}
    <a class="btn" type="button" onclick="$('#abstract-{{ entry.id }}').toggle(100);">abstract</a>
{% endif %}

{% if extra.award %}
    <button class="btn tag">{{ extra.award }}</button>
{% endif %}
  </div>

{% if entry.abstract %}
<div id="abstract-{{ entry.id }}" class="hidden">
  <p>{{ entry.abstract }}</p>
</div>
{% endif %}
  </li>

{% endif %}

{% endfor %}
</ul>

{% endfor %}
