-- arbitrary site processing

-- merge heads
heads = HTML.select(page, "head")
if Table.has_key(heads, 2) then
  content = HTML.clone_content(heads[2])
  HTML.append_child(heads[1], content)
  HTML.delete(heads[2])
end

-- replace footer
footers = HTML.select(page, "footer")
if Table.has_key(footers, 2) then
  content = HTML.clone_content(footers[1])
  HTML.replace_content(footers[2], content)
  HTML.delete(footers[1])
end

-- dedupe bodies
bodies = HTML.select(page, "body")
if Table.has_key(bodies, 2) then
  content = HTML.clone_content(bodies[2])
  HTML.append_child(HTML.parent(bodies[2]), content)
  HTML.delete(bodies[2])
end

-- add active class on title page
if(page_url == "/") then
  title = HTML.select_one(page, "h1 a")
  HTML.add_class(title, "active")
end