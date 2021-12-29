nav = HTML.select_one(page, "#secondary-nav")
dirs = {}

function capitalize(str)
    head = strsub(str, 1, 1)
    tail = strsub(str, 2)
    upper_head = strupper(head)
    joined = String.join("", {upper_head, tail})
    return joined
end

function split(str, delimiter)
    local loop_index, match_index, result = 1, 0, {}

    while 1 do
        local search_from_index = match_index + 1
        match_index = strfind(str, delimiter, search_from_index)

        -- No more of the pattern to find
        if match_index == nil then
            -- Check if there is more string to return
            if strlen(str) > search_from_index then
                result[loop_index] = String.trim(strsub(str, search_from_index))
            end
            return result
        -- Get the substring and add it to the table
        else
            result[loop_index] = String.trim(strsub(str, search_from_index, match_index))
            loop_index = loop_index + 1
        end
    end
end

-- dir is /site/widgets/label
function create_nav_item(i)
    tokens = split(dirs[i], "/")
    primary_nav = tokens[2]
    secondary_nav = tokens[3]
    href = String.join("", {"/", primary_nav, secondary_nav})
    text = capitalize(secondary_nav)
    a = HTML.create_element("a", text)
    HTML.set_attribute(a, "href", href)
    HTML.append_child(nav, a)
end

if page_url ~= "/" then
    url_tokens = split(page_url, "/")
    nav_menu = Regex.replace(url_tokens[2], "/$", "")
    path = String.join("/", {"site", nav_menu})
    cmd = String.join(" ", {"find", path, "-type", "d", "-depth", "1"})
    output = Sys.get_program_output(cmd)
    dirs = split(output, "\n")
    Table.iter(create_nav_item, dirs)
end

