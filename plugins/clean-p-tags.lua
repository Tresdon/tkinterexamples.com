-- clean p tags (un-nest images from p tags)
-- todo: cmark shouldn't do this ideally
p_tags = HTML.select(page, "p")

function clean_p_tags(i)
  p_tag = p_tags[i]
  nested_element = HTML.select_any_of(p_tag, {"img"})
  if HTML.is_element(nested_element) then
    -- change p to figure
    HTML.set_tag_name(p_tag, "figure")
  end
end

Table.iter(clean_p_tags, p_tags)